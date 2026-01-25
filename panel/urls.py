from django.urls import path
from .views import UserListCreateAPIView, UserDetailAPIView, StatisticsAPIView

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view()),
    path('users/<int:pk>/', UserDetailAPIView.as_view()),
    path('dashboard/', StatisticsAPIView.as_view()),
]
