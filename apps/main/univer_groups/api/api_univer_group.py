# Django
from django_filters.rest_framework import DjangoFilterBackend

# RestFramework
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

# Project
from apps.main.univer_groups.models import UniverGroup
from apps.main.univer_groups.serializers import UniverGroupSerializer


class UniverGroupViewSet(ModelViewSet):
    model = UniverGroup
    queryset = model.objects.all()
    serializer_class = UniverGroupSerializer
    permission_classes = [AllowAny]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = [
        '^name',
        'faculty__name'
    ]
    ordering_fields = ['name', '-id', 'faculty__name']
    ordering = ['-id']
