from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny

from .models import *
from .serializers import CollectionSerializer, PublicSerializer, NewSerializer, HelpSerializer, \
    AboutSerializer, AboutImageSerializer  # HelpImageSerializer


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


class HelpListView(generics.ListAPIView):
    queryset = Help.objects.all()
    serializer_class = HelpSerializer
    permission_classes = [AllowAny, ]


# class HelpImageListView(generics.ListAPIView):
#     queryset = HelpImage.objects.all()
#     serializer_class = HelpImageSerializer
#     permission_classes = [AllowAny, ]


class AboutListView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [AllowAny, ]


class AboutImageListView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutImageSerializer
    permission_classes = [AllowAny, ]