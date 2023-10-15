from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *

@api_view(['GET', 'POST'])
def dwelling_type_list(request):
    if request.method == 'GET':
        dwelling_types = DwellingType.objects.all()
        serializer = DwellingTypeSerializer(dwelling_types, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DwellingTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def dwelling_type_detail(request, pk):
    try:
        dwelling_type = DwellingType.objects.get(pk=pk)
    except DwellingType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DwellingTypeSerializer(dwelling_type)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DwellingTypeSerializer(dwelling_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        dwelling_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def city_list(request):
    if request.method == 'GET':
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def city_detail(request, pk):
    try:
        city = City.objects.get(pk=pk)
    except City.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CitySerializer(city)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CitySerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def dwelling_list(request):
    if request.method == 'GET':
        dwellings = Dwelling.objects.all()
        serializer = DwellingSerializer(dwellings, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DwellingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def dwelling_detail(request, pk):
    try:
        dwelling = Dwelling.objects.get(pk=pk)
    except Dwelling.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DwellingSerializer(dwelling)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DwellingSerializer(dwelling, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        dwelling.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def photo_list(request):
    if request.method == 'GET':
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def photo_detail(request, pk):
    try:
        photo = Photo.objects.get(pk=pk)
    except Photo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PhotoSerializer(photo)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PhotoSerializer(photo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def occupied_date_list(request):
    if request.method == 'GET':
        occupied_dates = OccupiedDate.objects.all()
        serializer = OccupiedDateSerializer(occupied_dates, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OccupiedDateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def occupied_date_detail(request, pk):
    try:
        occupied_date = OccupiedDate.objects.get(pk=pk)
    except OccupiedDate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OccupiedDateSerializer(occupied_date)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OccupiedDateSerializer(occupied_date, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        occupied_date.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)