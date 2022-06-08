import random
from rest_framework import generics, status, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework.response import Response
from .models import *
from .serializers import CollectionSerializer, PublicSerializer, NewSerializer, HelpSerializer, \
    AboutSerializer, AboutImageSerializer, ProductSerializer, FooterSerializer, \
    FooterTwoSerializer, HelpImageSerializer, CollProductSerializer, NewProductSerializer, \
    MainSerializer, AdvantagesSerializer, HitProductSerializer, FavProductSerializer, \
    DetailSerializer, BackCallSerializer, OrderSerializer, UserSerializer, CaseSerializer


class PaginationClass(PageNumberPagination):
    page_size = 8


class CollectionListView(generics.ListAPIView):
    """Коллекция"""
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [AllowAny, ]
    pagination_class = PaginationClass


class PaginClass(PageNumberPagination):
    page_size = 5


class CollectionNewListView(generics.ListAPIView):
    queryset = Product.objects.filter(new=True)
    serializer_class = CollProductSerializer
    permission_classes = [AllowAny, ]
    pagination_class = PaginClass


class PublicListView(generics.ListAPIView):
    """Публичная оферта"""
    queryset = Public.objects.all()
    serializer_class = PublicSerializer
    permission_classes = [AllowAny, ]


class NewListView(generics.ListAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    permission_classes = [AllowAny, ]
    pagination_class = PaginationClass


class HelpAPIView(ObjectMultipleModelAPIView):
    querylist = [
        {'queryset': HelpImage.objects.all(), 'serializer_class': HelpImageSerializer},
        {'queryset': Help.objects.all(), 'serializer_class': HelpSerializer},
    ]


class AboutAPIView(ObjectMultipleModelAPIView):
    """ О нас"""
    querylist = [
        {'queryset': AboutImage.objects.all(), 'serializer_class': AboutImageSerializer},
        {'queryset': About.objects.all(), 'serializer_class': AboutSerializer},
    ]


# class AboutListView(generics.ListAPIView):
#     queryset = About.objects.all()
#     serializer_class = AboutSerializer
#     permission_classes = [AllowAny, ]
#
#
# class AboutImageListView(generics.ListAPIView):
#     queryset = About.objects.all()
#     serializer_class = AboutImageSerializer
#     permission_classes = [AllowAny, ]


class PaginationsClass(PageNumberPagination):
    page_size = 12


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny, ]
    filter_backends = [SearchFilter]
    search_fields = ['title']
    pagination_class = PaginationClass


class FooterAPIView(ObjectMultipleModelAPIView):
    """Футер"""
    querylist = [
        {'queryset': Footer.objects.all(), 'serializer_class': FooterSerializer},
        {'queryset': FooterTwo.objects.all(), 'serializer_class': FooterTwoSerializer},
    ]


class CollProductListView(generics.ListAPIView):
    """Коллекция(товар)"""
    queryset = Collection.objects.all()
    serializer_class = CollProductSerializer
    permission_classes = [AllowAny, ]
    pagination_class = PaginationsClass


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
        {'queryset': Main.objects.all(), 'serializer_class': MainSerializer},
        {'queryset': Product.objects.filter(new=True), 'serializer_class': NewProductSerializer},
        {'queryset': Collection.objects.all(), 'serializer_class': CollectionSerializer},
        {'queryset': Advantages.objects.all(), 'serializer_class': AdvantagesSerializer},
    ]


"""Нравится"""


class FavProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(favorites=True)
    serializer_class = FavProductSerializer
    permission_classes = [AllowAny, ]
    pagination_class = PaginationsClass


"""Товары одной коллекции"""


class DetailListView(generics.RetrieveAPIView):
    queryset = Collection.objects.all()
    serializer_class = DetailSerializer
    pagination_class = PaginClass


"""Обратный звонок"""


class BackCallList(generics.ListAPIView):
    queryset = BackCall.objects.all()
    serializer_class = BackCallSerializer


"""Информация юзера"""


class UserListView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderAPIView(ObjectMultipleModelAPIView):
    querylist = [
        {'queryset': User.objects.all(), 'serializer_class': UserSerializer},
        {'queryset': Order.objects.all(), 'serializer_class': OrderSerializer},
    ]


"""Корзина"""


class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = [AllowAny, ]
