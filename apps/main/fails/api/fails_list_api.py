# Django
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend

# Rest-Framework
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from apps.user.custom_permissions import IsStudentOrReadOnly
from rest_framework import viewsets

# Project
from apps.main.fails.models import Fail
from apps.main.fails.serializers import FailListSerializer, FailOfStudentListSerializer


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


class FailOfStudentListViewSet(viewsets.ModelViewSet):
    queryset = (Fail.objects.all()
                .select_related('user', 'user__department', 'user__univer_group', 'user__univer_group__faculty_dirs', 'subject'))
    serializer_class = FailOfStudentListSerializer
    permission_classes = [IsAuthenticated, IsStudentOrReadOnly]
    lookup_field = 'pk'

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = [
        'subject__name',
    ]
    ordering_fields = ['score', 'subject_credit', 'semester']
    ordering = ['-id']

    def get_queryset(self):
        queryset = super().get_queryset()
        from apps.user.models import User
        for obj in queryset:
            user = User.objects.get(id=obj.user.id)
            obj.full_name = user.full_name
        return queryset
