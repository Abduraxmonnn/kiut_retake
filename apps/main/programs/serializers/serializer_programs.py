# RestFramework
from rest_framework import serializers

# Project
from apps.main.programs.models import Program


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'
