from django.urls import path, include
from .views import CityDetailView, CityListView, DwellingDetailView, DwellingListView, DwellingTypeDetailView, DwellingTypeListView, OccupiedDateDetailView, OccupiedDateListView, PhotoDetailView, PhotoListView, ReviewDetailView, UserViewSet
from rest_framework import routers
from django.contrib import admin
from drf_spectacular.views import (
    SpectacularSwaggerView,
    SpectacularAPIView,
    SpectacularRedocView)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dwellings/', DwellingListView.as_view(), name='dwelling-list'),
    path('dwellings/<int:pk>/', DwellingDetailView.as_view(), name='dwelling-detail'),
    
    path('cities/', CityListView.as_view(), name='city-list'),
    path('cities/<int:pk>/', CityDetailView.as_view(), name='city-detail'),
    
    path('dwelling-types/', DwellingTypeListView.as_view(), name='dwelling-type-list'),
    path('dwelling-types/<int:pk>/', DwellingTypeDetailView.as_view(), name='dwelling-type-detail'),
    
    path('photos/', PhotoListView.as_view(), name='photo-list'),
    path('photos/<int:pk>/', PhotoDetailView.as_view(), name='photo-detail'),
    
    path('occupied-dates/', OccupiedDateListView.as_view(), name='occupied-date-list'),
    path('occupied-dates/<int:pk>/', OccupiedDateDetailView.as_view(), name='occupied-date-detail'),
    
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),
    path('redoc/', SpectacularRedocView.as_view(url_name='api-schema'), name='api-redoc'),
] + router.urls