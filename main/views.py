from rest_framework import generics, viewsets
from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from drf_multiple_model.views import ObjectMultipleModelAPIView

from .models import *
from .serializers import CollectionSerializer, PublicSerializer, NewSerializer, HelpSerializer, \
    AboutSerializer, AboutImageSerializer, ProductSerializer, FooterSerializer, \
    FooterTwoSerializer, HelpImageSerializer, FavoriteSerializer


class PaginationClass(PageNumberPagination):
    page_size = 8


class CollectionListView(generics.ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [AllowAny, ]
    pagination_class = PaginationClass


class PublicListView(generics.ListAPIView):
    queryset = Public.objects.all()
    serializer_class = PublicSerializer
    permission_classes = [AllowAny, ]


class News(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField()


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
    querylist = [
        {'queryset': Footer.objects.all(), 'serializer_class': FooterSerializer},
        {'queryset': FooterTwo.objects.all(), 'serializer_class': FooterTwoSerializer},
    ]

# class FavoriteListView(generics.ListAPIView):
#
#         queryset = Favorite.objects.all()
#         serializer_class = FavoriteSerializer
#         permission_classes = [AllowAny, ]


class FavoriteCreateView(generics.CreateAPIView, ListAPIView, DestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer




