from django.shortcuts import get_object_or_404
from os import stat
from django.urls import is_valid_path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def products_list(request):

    if request.method == 'GET':
        products = Product.objects.all()
        serializers = ProductSerializer(products, many=True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    products = get_object_or_404(products, pk=pk)
    if request.method == 'GET':
        serializer = ProductSerializer(products)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(products, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)