# Rest-Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

# Project
from apps.user.models import User


class StudentDeleteAPIView(APIView):
    """
    Delete a student.

    This method deletes a specific student from the system based on the provided
    student_id. The student will be permanently removed from the database.

    Permissions:
    - Only authenticated users with appropriate permissions can delete a student.

    Args:
    request (rest_framework.request.Request): The DELETE request object.
    pk: student_id (not university id number).

    Returns:
    rest_framework.response.Response: A response indicating the success of the deletion.
    """
    permission_classes = (IsAdminUser, )

    def delete(self, request, pk=None):
        try:
            User.objects.get(pk=pk).delete()
            return Response({
                'message': 'User deleted successfully'
            }, 200)
        except User.DoesNotExist:
            return Response({
                'message': 'User does not exists'
            }, 400)
