# Rest-Framework
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAdminUser

# Project
from apps.main.fails.models import Fail
from apps.main.fails.serializers import FailSerializer


class FailUpdateAPIView(UpdateAPIView):
    queryset = (Fail.objects.all()
                .select_related('subject', 'user', 'user__univer_group', 'user__univer_group__faculty'))
    serializer_class = FailSerializer
    permission_classes = [IsAdminUser]
