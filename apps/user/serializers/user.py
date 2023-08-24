# Rest-Framework
from rest_framework import serializers

# Project
from apps.user.models import User
from apps.main.univer_groups.serializers import UniverGroupSerializer


class UserListSerializer(serializers.ModelSerializer):
    univer_group = UniverGroupSerializer(many=False)

    class Meta:
        model = User
        fields = [
            'id',
            'student_id',
            'full_name',
            'phone_number',
            'passport_number',
            'passport_issue_date',
            'passport_expiry_date',
            'dob',
            'nation',
            'profile_image',
            'about_me',
            'fails',
            'univer_group',
            'email_address',
            'is_active',
            'last_login'
        ]
