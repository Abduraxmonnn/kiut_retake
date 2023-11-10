# Django
from django.urls import path, include

# RestFramework
from rest_framework import routers

# Project
from apps.main.rooms.api import RoomViewSet
from apps.main.subjects.api import SubjectViewSet
from apps.main.faculties.api import FacultyViewSet, FacultyListViewSet
from apps.main.univer_groups.api import UniverGroupViewSet, UniverGroupListViewSet

router = routers.DefaultRouter()

router.register('rooms', RoomViewSet, basename='rooms')
router.register('subjects', SubjectViewSet, basename='subjects')
router.register('faculties', FacultyViewSet, basename='faculties')
router.register('faculties_list', FacultyListViewSet, basename='faculties-list')
router.register('univer_groups', UniverGroupViewSet, basename='univer-groups')
router.register('univer_groups_list', UniverGroupListViewSet, basename='univer-groups-list')


urlpatterns = [
    path(r'', include(router.urls)),
    path('users/', include("apps.user.urls")),
    path('fails/', include("apps.main.fails.urls"))
]
