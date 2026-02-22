from django.urls import path, include
from api.views import ProductList, OrderList


urlpatterns = [
    path('products/', ProductList.as_view(), name='products'),
    path('orders/', OrderList.as_view()),
]