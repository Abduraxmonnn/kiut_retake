# Rest-Framework
from rest_framework.serializers import ModelSerializer

# Project
from apps.main.faculties.models import Faculty
from apps.main.programs.serializers import ProgramSerializer
from apps.main.deans.serializers import DeanSerializer


class FacultySerializer(ModelSerializer):

    class Meta:
        model = Faculty
        fields = '__all__'
