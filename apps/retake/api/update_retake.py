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
from apps.retake.serializers.update_retake import UpdateRetakeSerializer


class UpdateRetakeAPIView(APIView):
    def put(self, request, pk=None):
        serializer = UpdateRetakeSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        retake_date = serializer.validated_data['retake_date']
        retake_time = serializer.validated_data['retake_time']
        retake_room = serializer.validated_data['retake_room']

        get_retake = Retake.objects.get(pk=pk)

        get_room = get_object_or_404(
            Room,
            build=retake_room['build'],
            number=retake_room['number'],
            type_room=retake_room['type_room']
        )

        get_retake.retake_date = retake_date
        get_retake.retake_time = retake_time
        get_retake.retake_room = get_room
        get_retake.save()

        return Response({
            'status': 'successfully',
            'message': 'Retake schedules have been successfully updated for the specified students.'
        }, status=status.HTTP_200_OK)
