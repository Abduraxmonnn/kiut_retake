from rest_framework.permissions import BasePermission


class IsDeanOrAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and not request.user.is_anonymous and request.user.is_dean or request.user.is_staff)
