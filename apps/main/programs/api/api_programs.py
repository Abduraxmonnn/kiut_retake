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
    """
    ViewSet for the Programs of University.

    The ProgramViewSet allows CRUD operations (Create, Retrieve, Update, and Delete) for instances
    of the Dean model. It uses the DeanSerializer to serialize and deserialize data between the
    Django model and JSON format.
    """
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [AllowAny]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = [
        '^name',
    ]
    ordering_fields = ['name', '-id']
    ordering = ['-id']
