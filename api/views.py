from .models import Dwelling, DwellingType, OccupiedDate, City, Photo, Review
from .serializer import CitySerializer, DwellingSerializer, DwellingTypeSerializer, OccupiedDateSerializer, PhotoSerializer, UserSerializer, ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions, generics
from django.contrib.auth import get_user_model
from .permissions import IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyNoAuth


class DwellingListView(generics.ListCreateAPIView):
    serializer_class = DwellingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Dwelling.objects.all()

class DwellingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dwelling.objects.all()
    serializer_class = DwellingSerializer
    permission_classes = [IsOwnerOrReadOnlyNoAuth,]

class CityListView(generics.ListCreateAPIView):
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return City.objects.all()

class CityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

class DwellingTypeListView(generics.ListCreateAPIView):
    serializer_class = DwellingTypeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return DwellingType.objects.all()

class DwellingTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DwellingType.objects.all()
    serializer_class = DwellingTypeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

class PhotoListView(generics.ListCreateAPIView):
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Photo.objects.all()

class PhotoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

class OccupiedDateListView(generics.ListCreateAPIView):
    serializer_class = OccupiedDateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return OccupiedDate.objects.all()

class OccupiedDateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OccupiedDate.objects.all()
    serializer_class = OccupiedDateSerializer
    permission_classes = [IsOwnerOrReadOnly,]
    
User = get_user_model()
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ReviewListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly,]