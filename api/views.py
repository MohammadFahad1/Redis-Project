from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Product, Order
from api.serializers import ProductSerializer, OrderSerializer
from django.core.cache import cache
from api.rate_limiter import rate_limit
# Create your views here.

""" class ProductList(APIView):
    queryset = Product.objects.all()
    def get(self, request):
        cache_key = 'products'
        if cache.get(cache_key):
            print("Using Cache!")
            return Response(cache.get(cache_key), status=status.HTTP_200_OK)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        cache.set(cache_key, serializer.data, timeout=60*60) # Cache for 1 hour
        return Response(serializer.data, status=status.HTTP_200_OK) """
    
class ProductList(APIView):
    queryset = Product.objects.all()
    
    @rate_limit(max_requests=5, time_window=60)
    def get(self, request):
        cache_key = 'products'
        if cache.get(cache_key):
            print("Using cache to get products!")
            return Response(cache.get(cache_key), status=status.HTTP_200_OK)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        cache.set(cache_key, serializer.data, timeout=60*60)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class OrderList(APIView):
    queryset = Order.objects.all()
    def get(self, request):
        cache_key = 'orders'
        if cache.get(cache_key):
            print("Using cache to get orders!")
            return Response(cache.get(cache_key), status=status.HTTP_200_OK)
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        cache.set(cache_key, serializer.data, timeout=60*60)
        return Response(serializer.data, status=status.HTTP_200_OK)