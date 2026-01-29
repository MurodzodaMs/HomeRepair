from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import *
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


from .models import *
from .serializers import *
from .permissions import *


class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.filter(is_delete=False)
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(client=self.request.user, is_delete=False)

    def get_serializer_class(self):
        if self.request.method in ['GET', 'PUT', 'PATCH']:
            return OrderSerializer if self.request.user.is_staff else OrderClientSerializer
        return OrderCreateSerializer

class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.filter(is_delete=False)
    serializer_class = OrderSerializer
    permission_classes = [IsAdminOrIsOwnerRead]


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_delete = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)