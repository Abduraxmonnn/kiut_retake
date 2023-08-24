# Rest-Framework
from rest_framework import serializers, mixins, viewsets

# Project
from apps.main.faculties.models import Faculty
from apps.main.programs.serializers import ProgramSerializer
from apps.main.deans.serializers import DeanSerializer


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class FacultyListSerializer(serializers.ModelSerializer):
    program = ProgramSerializer(many=False)
    dean = DeanSerializer(many=False)

    class Meta:
        model = Faculty
        fields = [
            'id',
            'name',
            'program',
            'dean',
        ]
