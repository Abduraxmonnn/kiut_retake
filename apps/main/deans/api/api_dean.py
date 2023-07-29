# Rest-Framework
from rest_framework import viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# Project
from apps.main.deans.models import Dean
from apps.main.deans.serializers import DeanSerializer


class DeanViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Deans of University.

    The DeanViewSet allows CRUD operations (Create, Retrieve, Update, and Delete) for instances
    of the Dean model. It uses the DeanSerializer to serialize and deserialize data between the
    Django model and JSON format.
    """
    model = Dean
    queryset = model.objects.all()
    serializer_class = DeanSerializer
    permission_classes = [AllowAny]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = [
        '^full_name',
    ]
    ordering_fields = ['full_name', '-id']
    ordering = ['-id']
