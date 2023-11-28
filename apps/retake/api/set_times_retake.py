# Django
from django.shortcuts import get_object_or_404

# Rest-Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Project
from apps.main.rooms.models import Room
from apps.retake.models import Retake
from apps.retake.serializers.set_times_retake import SetTimesRetakeSerializer


class SetTimesRetakeAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, pk=None):
        serializer = SetTimesRetakeSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        student_ids = serializer.validated_data['student_id']
        retake_date = serializer.validated_data['retake_date']
        retake_time = serializer.validated_data['retake_time']
        retake_room = serializer.validated_data['retake_room']

        # Get all relevant Retake objects in a single query
        # retakes = Retake.objects.filter(user__student_id__in=student_ids)

        # Get all relevant Retake objects in a single query who retake Room data is null.
        retakes = Retake.objects.exclude(
            retake_date__isnull=False,
            retake_time__isnull=False,
            retake_room__isnull=False
        ).filter(user__student_id__in=student_ids)

        # Update retake details for all objects
        retakes.update(
            retake_date=retake_date,
            retake_time=retake_time,
            retake_room=get_object_or_404(
                Room,
                build=retake_room['build'],
                number=retake_room['number'],
                type_room=retake_room['type_room']
            )
        )

        return Response({
            'status': 'successfully',
            'message': 'Retake schedules have been successfully updated for the specified students.'
        }, status=status.HTTP_200_OK)
