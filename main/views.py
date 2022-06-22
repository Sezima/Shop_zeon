import random
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_multiple_model.views import ObjectMultipleModelAPIView

from .models import *
from .permissions import IsUser
from .serializers import CollectionSerializer, PublicSerializer, \
    NewSerializer, HelpSerializer, \
    AboutSerializer, AboutImageSerializer, \
    ProductSerializer, FooterSerializer, \
    FooterTwoSerializer, HelpImageSerializer, \
    NewProductSerializer, MainSerializer, \
    AdvantagesSerializer, HitProductSerializer, \
    DetailSerializer, BackCallSerializer, \
    UserSerializer, OrderSerializer, \
    CaseSerializer, FavoriteSerializer


class PaginationClass(PageNumberPagination):
    page_size = 8


class PaginClass(PageNumberPagination):
    page_size = 5


class PaginationsClass(PageNumberPagination):
    page_size = 12


class CollectionListView(generics.ListAPIView):
    """Коллекция"""
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [AllowAny, ]
    pagination_class = PaginationClass


class PublicListView(generics.ListAPIView):
    """Публичная оферта"""
    queryset = Public.objects.all()
    serializer_class = PublicSerializer
    permission_classes = [AllowAny, ]


class NewListView(generics.ListAPIView):
    """Новинки"""
    queryset = New.objects.all()
    serializer_class = NewSerializer
    permission_classes = [AllowAny, ]
    pagination_class = PaginationClass


class HelpAPIView(ObjectMultipleModelAPIView):
    querylist = [
        {
            'queryset': HelpImage.objects.all(),
            'serializer_class': HelpImageSerializer
        },
        {
            'queryset': Help.objects.all(),
            'serializer_class': HelpSerializer
        },
    ]


class AboutAPIView(ObjectMultipleModelAPIView):
    """ О нас"""
    querylist = [
        {
            'queryset': AboutImage.objects.all(),
            'serializer_class': AboutImageSerializer
        },
        {
            'queryset': About.objects.all(),
            'serializer_class': AboutSerializer
        },
    ]


class ProductListView(generics.ListAPIView):
    """Товар"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny, ]
    pagination_class = PaginationClass


class Search(generics.ListAPIView):
    """Поиск"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']



    def list(self, request, *args, **kwargs):
        """5шт рандомные товары"""
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset:
            queryset = set(Product.objects.values_list('collections', flat=True))
            queryset = [random.choice(Product.objects.filter(collections=i)) for i in queryset]
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class FooterAPIView(ObjectMultipleModelAPIView):
    """Футер"""
    querylist = [
        {'queryset': Footer.objects.all(),
         'serializer_class': FooterSerializer},
        {'queryset': FooterTwo.objects.all(),
         'serializer_class': FooterTwoSerializer},
    ]


class NewProductListView(generics.ListAPIView):
    """Новинки"""
    queryset = Product.objects.filter(new=True)
    serializer_class = NewProductSerializer
    permission_classes = [AllowAny, ]
    pagination_class = PaginationClass


class HitProductListView(generics.ListAPIView):
    """Хит"""
    queryset = Product.objects.filter(hit=True)
    serializer_class = HitProductSerializer
    permission_classes = [AllowAny, ]
    pagination_class = PaginationClass


class MainSiteAPIView(ObjectMultipleModelAPIView):
    """Главная страница апи"""
    querylist = [
        {
            'queryset': Main.objects.all(),
            'serializer_class': MainSerializer
        },
        {
            'queryset': Product.objects.filter(new=True),
            'serializer_class': NewProductSerializer
        },
        {
            'queryset': Collection.objects.all(),
            'serializer_class': CollectionSerializer
        },
        {
            'queryset': Advantages.objects.all(),
            'serializer_class': AdvantagesSerializer
        },
    ]


class FavoriteViewSet(viewsets.ModelViewSet):
    """Нравится"""
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAuthenticated, ]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsUser, ]
        else:
            permissions = []
        return [permission() for permission in permissions]


    def list(self, request, *args, **kwargs):
        """5шт рандомные товары"""
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset:
            queryset = set(Product.objects.values_list('collections', flat=True))
            queryset = [random.choice(Product.objects.filter(collections=i)) for i in queryset]
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class DetailListView(generics.RetrieveAPIView):
    """Товары одной коллекции"""
    queryset = Collection.objects.all()
    serializer_class = DetailSerializer
    pagination_class = PaginClass



class BackCallViewSet(viewsets.ModelViewSet):
    """Обратный звонок"""
    queryset = BackCall.objects.all()
    serializer_class = BackCallSerializer


class UserListView(generics.RetrieveAPIView):
    """Информация юзера"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderAPIView(ObjectMultipleModelAPIView):
    querylist = [
        {
            'queryset': User.objects.all(),
            'serializer_class': UserSerializer
        },
        {
            'queryset': Order.objects.all(),
            'serializer_class': OrderSerializer
        },
    ]


class CaseViewSet(viewsets.ModelViewSet):
    """Корзина"""
    queryset = Case.objects.all()
    serializer_class = CaseSerializer


# class CartListView(generics.ListAPIView):
#     queryset = Order.objects.filter(id=1)
#     serializer_class = CartSerializer
#
#
# class CartinfoAPIView(ObjectMultipleModelAPIView):
#     querylist = [
#         {'queryset': Case.objects.all(),
#          'serializer_class': CaseSerializer},
#         {'queryset': Order.objects.all(),
#          'serializer_class': OrderSerializer},
#     ]





