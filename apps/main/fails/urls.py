# Django
from django.urls import path

# Project
from apps.main.fails.api import (FailCreateAPIView, FailUpdateAPIView, FailDestroyAPIView, FailListAPIView,
                                 FailRetrieveAPIView)


urlpatterns = [
    path('list/', FailListAPIView.as_view(), name='fails_list'),
    path('retrieve/<int:pk>/', FailRetrieveAPIView.as_view(), name='fails_retrieve'),
    path('create/', FailCreateAPIView.as_view(), name='fails_create'),
    path('update/<int:pk>/', FailUpdateAPIView.as_view(), name='fails_update'),
    path('delete/<int:pk>/', FailDestroyAPIView.as_view(), name='fails_delete'),
]
