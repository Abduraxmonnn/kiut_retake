# Rest-Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Project
from apps.retake.models import Retake
from apps.user.custom_permissions import IsDeanOrAdminOrReadOnly


class DeleteRetakeAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser, IsDeanOrAdminOrReadOnly]

    def delete(self, request, pk=None):
        get_retake = Retake.objects.get(pk=pk)
        get_retake.is_hide = True
        get_retake.save()

        return Response({
            'status': 'successfully',
            'message': f'Deleted Retake with ID {pk}'
        })
