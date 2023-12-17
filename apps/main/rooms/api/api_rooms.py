# Django
from django_filters.rest_framework import DjangoFilterBackend

# RestFramework
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

# Project
from apps.main.rooms.models import Room
from apps.main.rooms.serializers import RoomSerializer


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [AllowAny]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = [
        'number',
    ]
    ordering_fields = ['number', '-id']
    ordering = ['-id']

    def create(self, request, *args, **kwargs):
        build = request.POST.get('build')
        number = request.POST.get('number')
        type_room = request.POST.get('type_room')

        query = Room.objects.filter(build=build, number=number)

        if query.exists():
            return Response({
                'message': 'This Room Exists, Please check or create another Room'
            }, status=status.HTTP_409_CONFLICT)

        created = Room.objects.create(
            build=build,
            number=number,
            type_room=type_room
        )
        created.save()
        return Response({
            'message': 'Object created successfully',
            'data':
                {
                    'id': created.id,
                    'build': created.build,
                    'number': int(created.number),
                    'type_room': created.type_room
                }
        }, status=status.HTTP_201_CREATED)
