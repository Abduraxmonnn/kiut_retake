# Django
from django.urls import path

# Project
from apps.main.fails.api import FailCreateAPIView, FailUpdateAPIView


urlpatterns = [
    path('create/', FailCreateAPIView.as_view(), name='fails_create'),
    path('update/<int:pk>/', FailUpdateAPIView.as_view(), name='fails_update')
]
