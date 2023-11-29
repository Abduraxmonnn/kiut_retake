# Django
from django.urls import path

# Project
from apps.retake.api import ApplyRetakeAPIView, SetTimesRetakeAPIView, UpdateRetakeAPIView, DeleteRetakeAPIView


urlpatterns = [
    path('apply-retake/', ApplyRetakeAPIView.as_view(), name='apply-retake'),
    path('set-times-retake/', SetTimesRetakeAPIView.as_view(), name='set-times-retake'),
    path('update-times-retake/<int:pk>/', UpdateRetakeAPIView.as_view(), name='update-retake'),
    path('delete-retake/<int:pk>/', DeleteRetakeAPIView.as_view(), name='delete-retake'),
]
