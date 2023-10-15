from rest_framework import serializers
from .models import City, Dwelling, Photo, OccupiedDate, DwellingType

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
    dwelling_type = DwellingTypeSerializer()  # Додали серіалайзер для dwelling_type
    photos = PhotoSerializer(many=True)
    occupied_dates = OccupiedDateSerializer(many=True)

    class Meta:
        model = Dwelling
        fields = '__all__'