"""
URL configuration for django_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path
from api import views
from django.conf import settings
from .settings import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/dwellings/$', views.dwelling_list),
    re_path(r'^api/dwellings/(\d+)$', views.dwelling_detail),
    re_path(r'^api/dwellingstype/$', views.dwelling_type_list),
    re_path(r'^api/dwellingstype/(\d+)$', views.dwelling_type_detail),
    re_path(r'^api/cities/$', views.city_list),
    re_path(r'^api/cities/(\d+)$', views.city_detail),
    re_path(r'^api/photos/$', views.photo_list),
    re_path(r'^api/photos/(\d+)$', views.photo_detail),
    re_path(r'^api/occupieddates/$', views.occupied_date_list),
    re_path(r'^api/occupieddates/(\d+)$', views.occupied_date_detail),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)