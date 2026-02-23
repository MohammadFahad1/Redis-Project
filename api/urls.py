from django.urls import path, include
from api.views import ProductList, OrderList, PublishNotification


urlpatterns = [
    path('products/', ProductList.as_view(), name='products'),
    path('orders/', OrderList.as_view()),
    path('notification/', PublishNotification.as_view(), name='notification'),
]