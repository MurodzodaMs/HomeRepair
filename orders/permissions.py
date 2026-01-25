from rest_framework.permissions import BasePermission

class IsAdminOrIsOwnerRead(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user== obj.client or request.user.is_staff

