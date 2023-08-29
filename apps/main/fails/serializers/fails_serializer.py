# Rest-Framework
from rest_framework.serializers import ModelSerializer

# Project
from apps.main.fails.models import Fail
from apps.main.subjects.serializers import SubjectSerializer
from apps.user.serializers import UserListSerializer


class FailSerializer(ModelSerializer):
    class Meta:
        model = Fail
        fields = [
            'id',
            'subject',
            'user',
            'is_free'
        ]


class FailListSerializer(ModelSerializer):
    subject = SubjectSerializer(many=False)
    user = UserListSerializer(many=False)

    class Meta:
        model = Fail
        fields = [
            'id',
            'subject',
            'user',
            'is_free'
        ]