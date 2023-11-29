from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsStudentOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and not request.user.is_anonymous and not request.user.is_dean)
