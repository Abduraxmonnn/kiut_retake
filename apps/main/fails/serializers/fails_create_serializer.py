# Rest-Framework
from rest_framework import serializers

# Project
from apps.main.fails.models import Fail


class FailCreateSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(max_length=255)

    class Meta:
        model = Fail
        fields = [
            'subject',
            'user',
        ]
