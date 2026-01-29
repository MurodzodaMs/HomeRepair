from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'description', 'is_active', 'created_at']
        read_only_fields = ['id']


class ServicePhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServicePhoto
        fields = ['id', 'photo']

 

class ServiceSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(write_only=True)
    category = serializers.CharField(source='category.title')
    class Meta:
        model = Service
        fields = ['id', 'title', 'category', 'description', 
            'base_price', 'created_at', 'is_active']


class ServiceDetailSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(write_only=True)
    category = serializers.CharField(source='category.title')
    photos = ServicePhotoSerializer(many=True)
    class Meta:
        model = Service
        fields = ['id', 'title', 'category', 'description', 
            'base_price', 'created_at', 'photos', 'is_active', 'brigade']


class ServiceCreateSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(write_only=True)
    class Meta:
        model = Service
        fields = ['id', 'title', 'category', 'description',
            'base_price', 'created_at', 'is_active', 'brigade']

    def create(self, validated_data):
        photos = validated_data.pop('photos')
        service = Service.objects.create(**validated_data)

        for photo in photos:
            ServicePhoto.objects.create(service=service, photo=photo)

        return service