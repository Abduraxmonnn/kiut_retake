# Django
from django_filters.rest_framework import DjangoFilterBackend

# RestFramework
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

# Project
from apps.user.models import User
from apps.user.serializers import UserListSerializer


class StudentListViewSet(viewsets.ModelViewSet):
    """
       A ViewSet for listing student information.

       This ViewSet provides read-only operations (GET and HEAD) for accessing
       information about students within the system. It utilizes the UserListSerializer
       for serializing student data.

       Supported actions:
       - List: Retrieve a list of all students.
       - Retrieve: Get details of a specific student.

       Endpoint:
       The API endpoints for this ViewSet are dynamically generated based on the URL routing.
       Common patterns include:
       - GET api/students/list/ : List all students
       - GET api/students/{student_id}/ : Retrieve a student

       For more details on the fields and data formats, refer to the UserListSerializer.
       """
    queryset = User.objects.filter(is_staff=False, is_superuser=False).select_related('univer_group')
    serializer_class = UserListSerializer
    permission_classes = [IsAdminUser]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = [
        '^full_name',
        'student_id',
        'passport_number',
        'univer_group',
        'email_address',
    ]
    ordering_fields = ['full_name', '-id', 'univer_group']
    ordering = ['-id']
