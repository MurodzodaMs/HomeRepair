from rest_framework import generics, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from .models import Brigade
from .serializers import BrigadeSerializer


class BrigadeAPIViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Brigade.objects.all()
    serializer_class = BrigadeSerializer
