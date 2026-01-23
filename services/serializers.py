from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'description', 'is_active', 'created_at']
        read_only_fields = ['id']


class ServiceSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(write_only=True)
    category = serializers.CharField(source='category.title')
    class Meta:
        model = Service
        fields = ['id', 'title', 'category', 'description', 'base_price', 'created_at', 'is_active']


class ServiceCreateSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(write_only=True)
    class Meta:
        model = Service
        fields = ['id', 'title', 'category', 'description', 'base_price', 'created_at', 'is_active']