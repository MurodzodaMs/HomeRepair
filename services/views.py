from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend  # type: ignore
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from .serializers import *
from .models import *
from .permissions import *


class ServicePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'size'
    max_page_size = 20


class CategoryAPIView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    serializer_class = CategorySerializer
    filterset_fields = ['title', 'description']
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'description']
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Category.objects.all()
        return Category.objects.filter(is_active=True)


class ServiceAPIView(ModelViewSet):
    pagination_class = ServicePagination
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    # serializer_class = ServiceSerializer
    filterset_fields = ['title', 'description']
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'description']
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        request_body=ServiceCreateSwaggerSerializer,
        manual_parameters=[
            openapi.Parameter(
                'photos',
                openapi.IN_FORM,
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_FILE),
                description='Upload photos'
            )
        ]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=ServiceCreateSwaggerSerializer,
        manual_parameters=[
            openapi.Parameter(
                'photos',
                openapi.IN_FORM,
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_FILE),
                description='Upload photos'
            )
        ]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=ServiceCreateSwaggerSerializer,
        manual_parameters=[
            openapi.Parameter(
                'photos',
                openapi.IN_FORM,
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_FILE),
                description='Upload photos'
            )
        ]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ServiceCreateSerializer
        if self.action == 'retrieve':
            return ServiceDetailSerializer
        else:
            return ServiceSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            qs = Service.objects.all()
        else:
            qs = Service.objects.filter(is_active=True)

        if self.action == 'retrieve':
            qs = qs.prefetch_related('photos')
        return qs

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if request.user.is_staff:
            categories = Category.objects.all()
        else:
            categories = Category.objects.filter(is_active=True)
        cat_serializer = CategorySerializer(categories, many=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            services_data = self.get_paginated_response(serializer.data).data
        else:
            serializer = self.get_serializer(queryset, many=True)
            services_data = serializer.data

        return Response(
            {
                'categories': cat_serializer.data,
                'services': services_data
            },
            status=status.HTTP_200_OK
        )
