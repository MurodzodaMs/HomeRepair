from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend  # type: ignore


from .serializers import *
from .models import *
from .permissions import *


class ServicePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'size'
    max_page_size = 20


class CategoryAPIView(ModelViewSet):
    queryset = Category.objects.filter(is_active=True)
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    serializer_class = CategorySerializer
    filterset_fields = ['title', 'description']
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'description']


class ServiceAPIView(ModelViewSet):
    queryset = Service.objects.filter(is_active=True)
    pagination_class = ServicePagination
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    # serializer_class = ServiceSerializer
    filterset_fields = ['title', 'description']
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'description']

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return ServiceCreateSerializer
        else:
            return ServiceSerializer


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        categories = Category.objects.filter(is_active=True)
        cat_serializer = CategorySerializer(categories, many=True)
        ser_serializer = ServiceSerializer(queryset, many=True)
        return Response(
            {
                'categories':cat_serializer.data,
                'services':ser_serializer.data
            },
            status=status.HTTP_200_OK
        )


