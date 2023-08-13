# Rest-Framework
from rest_framework.serializers import ModelSerializer

# Project
from apps.main.univer_groups.models import UniverGroup


class UniverGroupSerializer(ModelSerializer):
    class Meta:
        model = UniverGroup
        fields = '__all__'
