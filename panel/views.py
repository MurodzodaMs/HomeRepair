from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.db.models import Sum

from accounts.serializers import UserSerializer
from accounts.models import CustomUser as User
from orders.models import Order
from services.models import Category, Service


class UserListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StatisticsAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        total_users = User.objects.filter(is_staff=False).count()
        active_users = User.objects.filter(
            is_active=True, is_staff=False).count()
        blocked_users = User.objects.filter(
            is_active=False, is_staff=False).count()
        total_order = Order.objects.count()
        total_service = Service.objects.count()
        total_category = Category.objects.count()
        total_completed_order = Order.objects.filter(
            status="completed").count()
        total_created_order = Order.objects.filter(status="created").count()
        total_in_progress_order = Order.objects.filter(
            status="in_progress").count()
        total_accepted_order = Order.objects.filter(status="accepted").count()
        company_profit = Order.objects.filter(
            status="completed"
        ).aggregate(total=Sum("service__base_price"))["total"] or 0

        return Response({
            "total_users": total_users,
            "active_users": active_users,
            "blocked_users": blocked_users,
            "total_order": total_order,
            "total_service": total_service,
            "total_category": total_category,
            "total_completed_order": total_completed_order,
            "total_created_order": total_created_order,
            "total_in_progress_order": total_in_progress_order,
            "total_accepted_order": total_accepted_order,
            "company_profit": company_profit,
        }, status=status.HTTP_200_OK)
