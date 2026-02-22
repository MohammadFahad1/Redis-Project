from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Product, Order
from api.serializers import ProductSerializer, OrderSerializer
# Create your views here.

class ProductList(APIView):
    queryset = Product.objects.all()
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class OrderList(APIView):
    queryset = Order.objects.all()
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)