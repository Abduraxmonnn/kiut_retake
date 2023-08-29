# Django
from django_filters.rest_framework import DjangoFilterBackend

# Rest-Framework
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

# Project
from apps.main.fails.models import Fail
from apps.main.fails.serializers import FailListSerializer


class FailListAPIView(ListAPIView):
    queryset = (Fail.objects.all()
                .select_related('subject', 'user', 'user__univer_group', 'user__univer_group__faculty'))
    serializer_class = FailListSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = [
        '^subject__name',
        'user__student_id',
    ]
    ordering_fields = ['is_free', '-id']
    ordering = ['-id']


class FailRetrieveAPIView(RetrieveAPIView):
    queryset = (Fail.objects.all()
                .select_related('subject', 'user', 'user__univer_group', 'user__univer_group__faculty'))
    serializer_class = FailListSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'
