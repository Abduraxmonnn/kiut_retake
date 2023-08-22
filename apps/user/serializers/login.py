# Rest-Framework
from rest_framework import serializers

# Project
from apps.user.models import User


class UserLogInSerializer(serializers.ModelSerializer):
    student_id = serializers.CharField(max_length=15)

    class Meta:
        model = User
        fields = [
            'student_id',
            'password',
        ]
