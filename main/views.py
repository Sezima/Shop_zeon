from requests import Response
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from drf_multiple_model.views import ObjectMultipleModelAPIView
from .models import *
from .serializers import CollectionSerializer, PublicSerializer, NewSerializer, HelpSerializer, \
    AboutSerializer, AboutImageSerializer, ProductSerializer, FooterSerializer, \
    FooterTwoSerializer, HelpImageSerializer, NewProductSerializer, \
    MainSerializer, AdvantagesSerializer, HitProductSerializer, \
    DetailSerializer, BackCallSerializer, UserSerializer, OrderSerializer, CaseSerializer, FavoritesSerializer, \
     CartSerializer


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


class FooterAPIView(ObjectMultipleModelAPIView):
    """Футер"""
    querylist = [
        {'queryset': Footer.objects.all(), 'serializer_class': FooterSerializer},
        {'queryset': FooterTwo.objects.all(), 'serializer_class': FooterTwoSerializer},
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
        {'queryset': Main.objects.all(), 'serializer_class': MainSerializer},
        {'queryset': Product.objects.filter(new=True), 'serializer_class': NewProductSerializer},
        {'queryset': Collection.objects.all(), 'serializer_class': CollectionSerializer},
        {'queryset': Advantages.objects.all(), 'serializer_class': AdvantagesSerializer},
    ]


"""Нравится"""


class FavoritesViewSet(viewsets.ModelViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer


"""Товары одной коллекции"""


class DetailListView(generics.RetrieveAPIView):
    queryset = Collection.objects.all()
    serializer_class = DetailSerializer
    pagination_class = PaginClass


"""Обратный звонок"""


class BackCallViewSet(viewsets.ModelViewSet):
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
    querylist = list([
        {'queryset': User.objects.all(), 'serializer_class': UserSerializer},
        {'queryset': Order.objects.all(), 'serializer_class': OrderSerializer},
        {'queryset': Order.objects.filter(id=1), 'serializer_class': CartSerializer},
    ])


"""Корзина"""


class CaseListView(generics.ListAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer




class CartListView(generics.ListAPIView):
    queryset = Order.objects.filter(id=1)
    serializer_class = CartSerializer


class CartinfoAPIView(ObjectMultipleModelAPIView):
    querylist = [
        {'queryset': Case.objects.all(), 'serializer_class': CaseSerializer},
        {'queryset': Order.objects.filter(id=1), 'serializer_class': CartSerializer},
    ]