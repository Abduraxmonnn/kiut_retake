# RestFramework
from rest_framework import serializers

# Project
from apps.main.subjects.models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
