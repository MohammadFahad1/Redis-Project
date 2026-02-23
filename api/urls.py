from django.urls import path, include
from api.views import ProductList, OrderList, PublishNotification, LeaderBoardAPI


urlpatterns = [
    path('products/', ProductList.as_view(), name='products'),
    path('orders/', OrderList.as_view()),
    path('notification/', PublishNotification.as_view(), name='notification'),
    path('leaderboard/', LeaderBoardAPI.as_view(), name='leaderboard'),
]