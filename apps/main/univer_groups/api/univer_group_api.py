# Django
from django_filters.rest_framework import DjangoFilterBackend

# RestFramework
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

# Project
from apps.main.univer_groups.models import UniverGroup
from apps.main.univer_groups.serializers import UniverGroupSerializer, UniverGroupListSerializer


class UniverGroupViewSet(ModelViewSet):
    """
        A ViewSet for managing university groups.

        This ViewSet provides CRUD (Create, Retrieve, Update, Delete) operations
        for university groups within the system. It uses the UniversityGroupSerializer
        for serializing and deserializing group data.

        Supported actions:
        - List: Retrieve a list of all university groups.
        - Retrieve: Get details of a specific university group.
        - Create: Register a new university group.
        - Update: Modify details of an existing university group (by authorized members).
        - Delete: Remove a university group (by authorized members).

        Note that permissions are enforced based on the user's role and group membership.

        Endpoint:
        The API endpoints for this ViewSet are dynamically generated based on the URL routing.
        Common patterns include:
        - POST /api/university-groups/ : Create a new group
        - PUT /api/university-groups/{group_id}/ : Update a group
        - DELETE /api/university-groups/{group_id}/ : Delete a group

        For more details on the fields and data formats, refer to the UniversityGroupSerializer.
        """
    model = UniverGroup
    queryset = model.objects.all()
    serializer_class = UniverGroupSerializer
    permission_classes = [AllowAny]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = [
        '^name',
        'faculty__name'
    ]
    ordering_fields = ['name', '-id', 'faculty__name']
    ordering = ['-id']


class UniverGroupListViewSet(ModelViewSet):
    """
    A ViewSet for retrieving university group information.

    This ViewSet allows only read operations (GET and HEAD) for accessing
    details of university groups within the system. It uses the UniversityGroupSerializer
    for serializing group data.

    Supported actions:
    - List: Retrieve a list of all university groups.
    - Retrieve: Get details of a specific university group.

    Endpoint:
    The API endpoints for this ViewSet are dynamically generated based on the URL routing.
    Common patterns include:
    - GET api/v2/univer_groups_list/ : List all groups
    - GET /api/university-groups/{group_id}/ : Retrieve a group

    For more details on the fields and data formats, refer to the UniverGroupListSerializer.
    """
    model = UniverGroup
    queryset = model.objects.all().select_related('faculty', 'faculty__program', 'faculty__dean')
    serializer_class = UniverGroupListSerializer
    permission_classes = [AllowAny]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = [
        '^name',
        'faculty__name'
    ]
    ordering_fields = ['name', '-id', 'faculty__name']
    ordering = ['-id']
