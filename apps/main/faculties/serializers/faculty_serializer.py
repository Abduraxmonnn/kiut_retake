# Rest-Framework
from rest_framework import serializers

# Project
from apps.main.faculties.models import Faculty
from apps.main.deans.serializers import DeanSerializer


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class FacultyListSerializer(serializers.ModelSerializer):
    dean = DeanSerializer(many=False)

    class Meta:
        model = Faculty
        fields = [
            'id',
            'name',
            'dean',
        ]
