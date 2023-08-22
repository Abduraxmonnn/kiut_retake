# Django
from django.urls import path, include

# RestFramework
from rest_framework import routers

# Project
from apps.main.programs.api import ProgramViewSet
from apps.main.rooms.api import RoomViewSet
from apps.main.subjects.api import SubjectViewSet
from apps.main.faculties.api import FacultyViewSet
from apps.main.univer_groups.api import UniverGroupViewSet

router = routers.DefaultRouter()

router.register('v2/programs', ProgramViewSet, basename='programs')
router.register('v2/rooms', RoomViewSet, basename='rooms')
router.register('v2/subjects', SubjectViewSet, basename='subjects')
router.register('v2/faculties', FacultyViewSet, basename='faculties')
router.register('v2/univer_groups', UniverGroupViewSet, basename='univer-groups')


urlpatterns = [
    path(r'', include(router.urls)),
    path('user/', include("apps.user.urls"))
]
