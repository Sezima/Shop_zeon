"""zeon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from main.views import CollectionListView, PublicListView, NewListView, \
    HelpAPIView, AboutAPIView, ProductListView, FooterAPIView, \
    CollProductListView, MainSiteAPIView, NewProductListView, HitProductListView, FavProductListView, \
    CollectionNewListView, DetailListView, BackCallList, OrderAPIView, OrderListView, UserListView, \
    CaseViewSet

router = DefaultRouter()
router.register('cart', CaseViewSet)
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui()),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/v1/collection/', CollectionListView.as_view()),
    path('api/v1/public/', PublicListView.as_view()),
    path('api/v1/news/', NewListView.as_view()),
    path('api/v1/product/', ProductListView.as_view()),
    path('api/v1/collectionnew/', CollectionNewListView.as_view()),
    path('api/v1/help/', HelpAPIView.as_view()),
    path('api/v1/footer/', FooterAPIView.as_view()),
    path('api/v1/about/', AboutAPIView.as_view()),
    path('api/v1/collproduct/', CollProductListView.as_view()),
    path('api/v1/newproduct/', NewProductListView.as_view()),
    path('api/v1/hitproduct/', HitProductListView.as_view()),
    path('api/v1/favorite/', FavProductListView.as_view()),
    path('api/v1/backcall/', BackCallList.as_view()),
    path('api/v1/mainsite/', MainSiteAPIView.as_view()),
    path('api/v1/detail/<int:pk>/', DetailListView.as_view()),
    path('api/v1/user/<int:pk>/', UserListView.as_view()),
    path('api/v1/item/', OrderListView.as_view()),
    path('api/v1/order/', OrderAPIView.as_view()),
    path('api/v1/', include(router.urls)),
    # path('api/v1/comon/', ComonListView.as_view()),
    # path('api/v1/case/', CaseListView.as_view()),



]
