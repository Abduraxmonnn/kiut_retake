# Rest-Framework
from rest_framework.serializers import ModelSerializer

# Project
from apps.main.fails.models import Fail


class FailSerializer(ModelSerializer):
    class Meta:
        model = Fail
        fields = '__all__'
