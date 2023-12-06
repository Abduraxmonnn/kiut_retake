# Django
from django_filters.rest_framework import DjangoFilterBackend

# RestFramework
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

# Project
from apps.main.faculties.models import Faculty
from apps.main.faculties.serializers import FacultySerializer, FacultyListSerializer


class FacultyViewSet(ModelViewSet):
    model = Faculty
    queryset = model.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [AllowAny]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = [
        '^name',
        'dean__full_name',
        'program__name'
    ]
    ordering_fields = ['name', '-id', 'program__name', 'dean__full_name']
    ordering = ['-id']


class FacultyListViewSet(ModelViewSet):
    model = Faculty
    queryset = model.objects.all().select_related('program', 'dean')
    serializer_class = FacultyListSerializer
    permission_classes = [AllowAny]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = [
        '^name',
        'dean__full_name',
        'program__name'
    ]
    ordering_fields = ['name', '-id', 'program__name', 'dean__full_name']
    ordering = ['-id']
