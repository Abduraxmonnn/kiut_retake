# Rest-Framework
from rest_framework.serializers import ModelSerializer

# Project
from apps.main.univer_groups.models import UniverGroup
from apps.main.faculties.serializers import FacultyListSerializer


class UniverGroupSerializer(ModelSerializer):
    class Meta:
        model = UniverGroup
        fields = '__all__'


class UniverGroupListSerializer(ModelSerializer):
    faculty = FacultyListSerializer(many=False)

    class Meta:
        model = UniverGroup
        fields = [
            'id',
            'name',
            'level',
            'type_education',
            'language',
            'faculty',
        ]
