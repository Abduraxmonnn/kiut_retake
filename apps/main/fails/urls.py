# Django
from django.urls import path

# Project
from apps.main.fails.api import (FailCreateAPIView, FailUpdateAPIView, FailDestroyAPIView, FailListAPIView,
                                 FailRetrieveAPIView, FailOfStudentListViewSet)


urlpatterns = [
    path('retrieve/<int:pk>/', FailRetrieveAPIView.as_view(), name='fails-retrieve'),
    path('create/', FailCreateAPIView.as_view(), name='fails-create'),
    path('update/<int:pk>/', FailUpdateAPIView.as_view(), name='fails-update'),
    path('delete/<int:pk>/', FailDestroyAPIView.as_view(), name='fails-delete'),

    path('fails/list/', FailListAPIView.as_view(), name='fails-list'),
    path('fails/student/list/', FailOfStudentListViewSet.as_view({'get': 'list'}), name='fails-of-student-list')
]
