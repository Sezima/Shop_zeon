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

from main.views import CollectionListView, PublicListView, NewListView, HelpListView, AboutListView, \
    AboutImageListView  # HelpImageListView

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
    path('api/v1/help/', HelpListView.as_view()),
    path('api/v1/about/', AboutListView.as_view()),
    path('api/v1/aboutimage/', AboutImageListView.as_view()),
    # path('api/v1/helpimage/', HelpImageListView.as_view()),
]
