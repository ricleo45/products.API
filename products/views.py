from django.shortcuts import get_object_or_404
from os import stat
from django.urls import is_valid_path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarSerializer
from .models import Product
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def products_list(request):
    
    if request.method == 'GET':
        cars = Product.objects.all()
        serializers = ProductsSerializer(cars, many=True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        serializer = ProductsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'GET':
        serializer = ProductsSerializer(car)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductsSerializer(car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)