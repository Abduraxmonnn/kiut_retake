# Django
from django.urls import path, include

# RestFramework
from rest_framework import routers

# Project
from apps.main.programs.api import ProgramViewSet

router = routers.DefaultRouter()

router.register('programs', ProgramViewSet, basename='programs')

urlpatterns = [
    path(r'', include(router.urls)),
]
