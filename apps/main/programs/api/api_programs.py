# Django
from django_filters.rest_framework import DjangoFilterBackend

# RestFramework
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

# Project
from apps.main.programs.models import Program
from apps.main.programs.serializers import ProgramSerializer


class ProgramViewSet(ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [AllowAny]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = [
        '^name',
    ]
    ordering_fields = ['name', '-id']
    ordering = ['-id']
