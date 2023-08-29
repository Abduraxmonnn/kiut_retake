# Rest-Framework
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

# Project
from apps.main.fails.models import Fail
from apps.main.fails.serializers import FailSerializer
from apps.main.subjects.models import Subject


class FailDestroyAPIView(DestroyAPIView):
    queryset = (Fail.objects.all()
                .select_related('subject', 'user', 'user__univer_group', 'user__univer_group__faculty'))
    serializer_class = FailSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'
