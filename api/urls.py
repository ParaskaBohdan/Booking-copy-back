from django.urls import path, include
from api import views
from rest_framework import routers
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dwellings/', views.dwelling_list),
    path('dwellings/<int:pk>/', views.dwelling_detail),
    path('dwellingstype/', views.dwelling_type_list),
    path('dwellingstype/<int:pk>/', views.dwelling_type_detail),
    path('cities/', views.city_list),
    path('cities/<int:pk>/', views.city_detail),
    path('photos/', views.photo_list),
    path('photos/<int:pk>/', views.photo_detail),
    path('occupieddates/', views.occupied_date_list),
    path('occupieddates/<int:pk>/', views.occupied_date_detail),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
] + router.urls