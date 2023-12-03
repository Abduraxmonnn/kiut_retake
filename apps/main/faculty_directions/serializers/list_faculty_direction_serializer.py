# Rest-Framework
from rest_framework import serializers

# Project
from apps.main.faculty_directions.models import FacultyDirections
from apps.main.faculties.serializers import FacultyListSerializer


class FacultyDirectionToDeanListSerializer(serializers.ModelSerializer):
    faculty = FacultyListSerializer(many=False)

    class Meta:
        model = FacultyDirections
        fields = [
            'id',
            'name',
            'faculty'
        ]
