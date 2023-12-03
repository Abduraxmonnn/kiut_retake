# Django
from django_filters.rest_framework import DjangoFilterBackend

# Rest-Framework
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Project
from apps.main.univer_groups.models import UniverGroup
from apps.main.univer_groups.serializers import UniverGroupToDeanListSerializer
from apps.user.custom_permissions import IsStudentOrReadOnly


class UniverGroupToDeanListViewSet(viewsets.ModelViewSet):
    queryset = (UniverGroup.objects.all())
    serializer_class = UniverGroupToDeanListSerializer
    permission_classes = [IsAuthenticated, IsStudentOrReadOnly]
    lookup_field = 'pk'

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
