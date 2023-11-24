# Django
from django.urls import path

# Project
from apps.retake.api import ApplyRetakeAPIView


urlpatterns = [
    path('apply-retake/', ApplyRetakeAPIView.as_view())
]
