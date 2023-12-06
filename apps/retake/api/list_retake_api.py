# Rest-Framework
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Project
from apps.retake.serializers import RetakeListSerializer, RetakeListForDeanSerializer
from apps.retake.models import Retake


class RetakeListViewSet(ModelViewSet):
    queryset = (Retake.objects.filter(is_hide=False)
                .select_related('user', 'user__department', 'user__univer_group', 'user__univer_group__faculty_dirs',
                                'case', 'subject', 'retake_room')
                .prefetch_related('subject__department'))
    serializer_class = RetakeListSerializer
    permission_classes = [IsAuthenticated]


class RetakeListForDeanViewSet(ModelViewSet):
    queryset = (Retake.objects.all()
                .select_related('user', 'user__univer_group', 'case', 'subject', 'retake_room'))
    serializer_class = RetakeListForDeanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.annotate(
            has_missing_data=(
                    Q(retake_date__isnull=True) | Q(retake_time__isnull=True) | Q(retake_room__isnull=True)
            )
        ).filter(has_missing_data=True and ~Q(is_hide=True))


class RetakeListOfSenderViewSet(ModelViewSet):
    queryset = (Retake.objects.all()
                .select_related('user', 'user__univer_group', 'user__department', 'case', 'subject', 'retake_room'))
    serializer_class = RetakeListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user and ~Q(is_hide=True))
