# Django
from django.urls import path, include

# Rest-Framework
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# Project
from apps.user.api import (UserLogInAPIView, StudentSignUpAPIView, StudentListViewSet, AdminsListViewSet,
                           StudentDeleteAPIView)

urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('login/', UserLogInAPIView.as_view(), name='user_login'),
    path('student/signup/', StudentSignUpAPIView.as_view(), name='student_signup'),
    path('students/list/', StudentListViewSet.as_view({'get': 'list'}), name='students_list'),
    path('admins/list/', AdminsListViewSet.as_view({'get': 'list'}), name='admins_list'),
    path('student/delete/<int:pk>/', StudentDeleteAPIView.as_view(), name='student_list'),
]
