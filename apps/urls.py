# Django
from django.urls import path, include

# RestFramework
from rest_framework import routers

# Project
from apps.main.programs.api import ProgramViewSet
from apps.main.rooms.api import RoomViewSet
from apps.main.subjects.api import SubjectViewSet
from apps.main.faculties.api import FacultyViewSet

router = routers.DefaultRouter()

router.register('v1/programs', ProgramViewSet, basename='programs')
router.register('v1/rooms', RoomViewSet, basename='rooms')
router.register('v1/subjects', SubjectViewSet, basename='subjects')
router.register('v1/faculties', FacultyViewSet, basename='faculties')

urlpatterns = [
    path(r'', include(router.urls)),
]
