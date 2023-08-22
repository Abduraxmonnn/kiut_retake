# Rest-Framework
from rest_framework import serializers

# Project
from apps.user.models import User


class UserSignUpSerializer(serializers.ModelSerializer):
    univer_group = serializers.CharField(
        max_length=255
    )

    class Meta:
        model = User
        fields = [
            'student_id',
            'full_name',
            'passport_number',
            'passport_issue_date',
            'gender',
            'nation',
            'password',
            'univer_group'
        ]

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError
