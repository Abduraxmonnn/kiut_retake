# Django
from django.urls import path

# Project
from apps.retake.api import (ApplyRetakeAPIView, SetTimesRetakeAPIView, UpdateRetakeAPIView, DeleteRetakeAPIView,
                             RetakeListViewSet, RetakeListForDeanViewSet, RetakeListOfSenderViewSet)


urlpatterns = [
    path('apply-retake/', ApplyRetakeAPIView.as_view(), name='apply-retake'),
    path('set-times-retake/', SetTimesRetakeAPIView.as_view(), name='set-times-retake'),
    path('update-times-retake/<int:pk>/', UpdateRetakeAPIView.as_view(), name='update-retake'),
    path('delete-retake/<int:pk>/', DeleteRetakeAPIView.as_view(), name='delete-retake'),
    path('list-retake/', RetakeListViewSet.as_view({'get': 'list'}), name='list-retake'),
    path('list-retake-for-set-times/', RetakeListForDeanViewSet.as_view({'get': 'list'}),
         name='list-retake-for-set-times'),
    path('list-retake-of-exact-user/', RetakeListOfSenderViewSet.as_view({'get': 'list'}),
         name='list-retake-of-exact-user'),
]
