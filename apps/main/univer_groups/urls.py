# Django
from django.urls import path

# Project
from apps.main.univer_groups.api import UniverGroupToDeanListViewSet


urlpatterns = [
    path('dean/list/', UniverGroupToDeanListViewSet.as_view({'get': 'list'}), name='groups-to-dean-list')
]
