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
    MainSiteAPIView, NewProductListView, HitProductListView, \
    DetailListView, Search, BackCallViewSet, UserListView, OrderListView, \
    FavoritesViewSet, CaseListView, CartListView, CartinfoAPIView, OrderAPIView

router = DefaultRouter()
router.register('звонок', BackCallViewSet)
router.register('избранные', FavoritesViewSet)
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
    path('api/v1/коллекция/', CollectionListView.as_view()),
    path('api/v1/оферта/', PublicListView.as_view()),
    path('api/v1/новости/', NewListView.as_view()),
    path('api/v1/товар/', ProductListView.as_view()),
    path('api/v1/помощь/', HelpAPIView.as_view()),
    path('api/v1/футер/', FooterAPIView.as_view()),
    path('api/v1/онас/', AboutAPIView.as_view()),
    path('api/v1/новинки/', NewProductListView.as_view()),
    path('api/v1/хит/', HitProductListView.as_view()),
    path('api/v1/главная/', MainSiteAPIView.as_view()),
    path('api/v1/коллекцият/<int:pk>/', DetailListView.as_view()),
    path('api/v1/заказщик/<int:pk>/', UserListView.as_view()),
    path('api/v1/корзина/', CaseListView.as_view()),
    path('api/v1/', include(router.urls)),
    path('api/v1/поиск/', Search.as_view()),
    path('api/v1/cartinfo/', CartinfoAPIView.as_view()),
    path('api/v1/заказ/', OrderAPIView.as_view()),

]
