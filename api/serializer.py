from rest_framework import serializers
from .models import City, Dwelling, Photo, OccupiedDate, DwellingType, User, Review
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

UserModel = get_user_model()

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class OccupiedDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OccupiedDate
        fields = '__all__'

class DwellingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DwellingType
        fields = '__all__'

class DwellingSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    dwelling_type = DwellingTypeSerializer()
    photos = PhotoSerializer(many=True)
    occupied_dates = OccupiedDateSerializer(many=True)

    class Meta:
        model = Dwelling
        fields = '__all__'
        
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password')
        
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        
class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']