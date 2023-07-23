# Django
from django.urls import path, include

# RestFramework
from rest_framework import routers

# Project
from apps.main.programs.api import ProgramViewSet
from apps.main.rooms.api import RoomViewSet
from apps.main.subjects.api import SubjectViewSet

router = routers.DefaultRouter()

router.register('programs', ProgramViewSet, basename='programs')
router.register('rooms', RoomViewSet, basename='rooms')
router.register('subjects', SubjectViewSet, basename='subjects')

urlpatterns = [
    path(r'api/v1/', include(router.urls)),
]
