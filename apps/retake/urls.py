# Django
from django.urls import path

# Project
from apps.retake.api import ApplyRetakeAPIView, SetTimesRetakeAPIView


urlpatterns = [
    path('apply-retake/', ApplyRetakeAPIView.as_view()),
    path('set-times-retake/', SetTimesRetakeAPIView.as_view())
]
