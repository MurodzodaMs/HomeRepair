from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'description', 'is_active', 'created_at']
        read_only_fields = ['id']