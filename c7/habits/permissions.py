from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsAdmin(BasePermission):
    """ Проверяет, является ли пользователь администратором """

    message = 'Вы не являетесь администратором!'

    def has_permission(self, request, view):
        if request.user.role == UserRoles.ADMIN:
            return True
        return False


class IsOwner(BasePermission):
    """ Проверяет к своей ли привычке запрашивает доступ пользователь """

    message = 'Вы не являетесь владельцем!'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner or request.user.is_superuser:
            return True
        return False
