# Rest-Framework
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

# Project
from apps.main.fails.models import Fail
from apps.main.fails.serializers import FailSerializer
from apps.main.subjects.models import Subject


class FailUpdateAPIView(UpdateAPIView):
    queryset = (Fail.objects.all()
                .select_related('subject', 'user', 'user__univer_group', 'user__univer_group__faculty'))
    serializer_class = FailSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

    def update(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        subject_name = request.data.get('subject').upper()
        is_free = request.data.get('is_free')
        try:
            subject_instance = Subject.objects.get(name=subject_name)
            instance.subject = subject_instance
            instance.is_free = is_free
        except Subject.DoesNotExist:
            return Response({"message": "Subject does not Exists"}, 404)
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
