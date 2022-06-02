from django.db.models import Q
from django.views.generic import DeleteView
from requests import Response
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from drf_multiple_model.views import ObjectMultipleModelAPIView

from .models import *
from .serializers import CollectionSerializer, PublicSerializer, NewSerializer, HelpSerializer, \
    AboutSerializer, AboutImageSerializer, ProductSerializer, FooterSerializer, \
    FooterTwoSerializer, HelpImageSerializer, CollProductSerializer, NewProductSerializer, \
    MainSerializer, AdvantagesSerializer, HitProductSerializer


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
    """TEST"""
    queryset = New.objects.all()
    serializer_class = NewSerializer
    permission_classes = [AllowAny, ]
    pagination_class = PaginationClass


# class HelpListView(generics.ListAPIView):
#     queryset = Help.objects.all()
#     serializer_class = HelpSerializer
#     permission_classes = [AllowAny, ]
#
#
# class HelpImageListView(generics.ListAPIView):
#     queryset = HelpImage.objects.all()
#     serializer_class = HelpImageSerializer
#     permission_classes = [AllowAny, ]


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
    """Товар"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny, ]
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']
    pagination_class = PaginationClass






# class FooterListView(generics.ListAPIView):
#     queryset = Footer.objects.all()
#     serializer_class = FooterSerializer
#     permission_classes = [AllowAny, ]
#
#
# class FooterTwoListView(generics.ListAPIView):
#     queryset = FooterTwo.objects.all()
#     serializer_class = FooterTwoSerializer
#     permission_classes = [AllowAny, ]

class FooterAPIView(ObjectMultipleModelAPIView):
    """Футер"""
    querylist = [
        {'queryset': Footer.objects.all(), 'serializer_class': FooterSerializer},
        {'queryset': FooterTwo.objects.all(), 'serializer_class': FooterTwoSerializer},
    ]


# class FavoriteListView(generics.ListAPIView):
#
#         queryset = Favorite.objects.all()
#         serializer_class = FavoriteSerializer
#         permission_classes = [AllowAny, ]


class CollProductListView(generics.ListAPIView):
    """Коллекция(товар)"""
    queryset = Product.objects.all()
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
    pagination_class = PaginationClass




