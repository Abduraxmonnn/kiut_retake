# Django
from django_filters.rest_framework import DjangoFilterBackend

# Rest-Framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

# Project
from apps.main.departments.models import Department
from apps.main.departments.serializers import DepartmentSerializer
from apps.user.custom_permissions.dean_permissions import IsDeanOrAdminOrReadOnly


class DepartmentViewSet(viewsets.ModelViewSet):
    model = Department
    queryset = model.objects.all().select_related('head_of_department')
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, IsDeanOrAdminOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = [
        '^name',
        'head_of_department__full_name'
    ]
    ordering_fields = ['name', '-id']
    ordering = ['-id']
