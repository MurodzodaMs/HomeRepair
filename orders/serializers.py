from rest_framework import serializers
from .models import *

class OrderSerializer(serializers.ModelSerializer):
    client = serializers.CharField(source='client.username')

    class Meta:
        model=Order
        fields = ['id', 'client','phone', 'service', 'address', 'status', 'start_date', 'end_date', 'is_delete']


class OrderClientSerializer(serializers.ModelSerializer):
    client = serializers.CharField(source='client.username')

    class Meta:
        model=Order
        fields = ['id', 'client', 'phone', 'service', 'address', 'status', 'start_date', 'end_date']



class OrderCreateSerializer(serializers.ModelSerializer):
    client = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model=Order
        fields = ['client', 'phone', 'service', 'address', 'start_date', 'end_date']