import datetime
import re
from .models import Dwelling, DwellingType, OccupiedDate, City, Photo, Review
from .serializer import CitySerializer, DwellingSerializer, DwellingTypeSerializer, OccupiedDateSerializer, PhotoSerializer, UserSerializer, ReviewSerializer
from rest_framework import viewsets, permissions, generics
from django.contrib.auth import get_user_model
from .permissions import IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyNoAuth
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


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
    permission_classes = [IsOwnerOrReadOnlyNoAuth,]

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
    permission_classes = [IsOwnerOrReadOnlyNoAuth,]
    
def card_verification(card_number, expiration_date, cvv):
    if not card_number or not expiration_date or not cvv:
        return False

    if not card_number.isdigit() or len(card_number) != 16:
        return False

    if not re.match(r'\d{2}/\d{2}', expiration_date):
        return False

    expiration_month, expiration_year = map(int, expiration_date.split('/'))
    current_date = datetime.datetime.today()
    if current_date.year > 2000 + expiration_year or (current_date.year == 2000 + expiration_year and current_date.month > expiration_month):
        return False

    if not cvv.isdigit() or len(cvv) != 3:
        return False

    return True
    
class PaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        card_number = request.data.get('card_number')
        expiration_date = request.data.get('expiration_date')
        cvv = request.data.get('cvv')
        user_id = self.request.user
        dwelling_req = Dwelling.objects.filter(id=request.data.get('dwelling')).first()
        check_in_req = request.data.get('check_in')
        check_out_req = request.data.get('check_out')
        if dwelling_req == None:
            return Response({'message': 'The operation was rejected due to invalid dwelling.'}, status=status.HTTP_400_BAD_REQUEST)
        elif card_verification(card_number, expiration_date, cvv):
            occupied_date = OccupiedDate.objects.create(user=user_id, check_in=check_in_req, check_out=check_out_req)
            occupied_date.save()
            dwelling_req.occupied_dates.add(occupied_date)
            dwelling_req.save()
            return Response({'message': f'Booking at the {dwelling_req.title} for the dates from {check_in_req} to {check_out_req} is confirmed'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'The operation was rejected due to invalid data.'}, status=status.HTTP_400_BAD_REQUEST)