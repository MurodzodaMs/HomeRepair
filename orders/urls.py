from django.urls import path
from .views import *

urlpatterns = [
    path('', OrderListCreateAPIView.as_view()),
    path('<int:pk>', OrderDetailAPIView.as_view())
]