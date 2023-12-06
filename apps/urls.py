# Django
from django.urls import path, include

# RestFramework
from rest_framework import routers

# Project
from apps.main.rooms.api import RoomViewSet
from apps.main.subjects.api import SubjectViewSet
from apps.main.faculties.api import FacultyViewSet, FacultyListViewSet
from apps.main.univer_groups.api import UniverGroupViewSet, UniverGroupListViewSet
from apps.main.departments.api import DepartmentViewSet

router = routers.DefaultRouter()

router.register('rooms', RoomViewSet, basename='rooms')
router.register('subjects', SubjectViewSet, basename='subjects')
router.register('faculties', FacultyViewSet, basename='faculties')
router.register('faculties-list', FacultyListViewSet, basename='faculties-list')
router.register('univer-groups_list', UniverGroupListViewSet, basename='univer-groups-list')
router.register('departments', DepartmentViewSet, basename='departments')


urlpatterns = [
    path(r'', include(router.urls)),
    path('users/', include("apps.user.urls")),
    path('fails/', include("apps.main.fails.urls")),
    path('retakes/', include("apps.retake.urls")),
    path('univer-groups/', include("apps.main.univer_groups.urls"))

]
