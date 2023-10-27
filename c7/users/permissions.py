from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsAdmin(BasePermission):
    message = "Вы не являетесь администратором!"

    def has_permission(self, request, view):
        if request.user.role == UserRoles.ADMIN:
            return True
        return False


class IsOwner(BasePermission):
    message = 'Вы не являетесь владельцем!'

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
