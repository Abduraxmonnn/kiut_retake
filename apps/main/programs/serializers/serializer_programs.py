# RestFramework
from rest_framework import serializers

# Project
from apps.main.programs.models import Program


class ProgramSerializer(serializers.ModelSerializer):
    """
    Serializer for the Programs of University.

    The ProgramSerializer is responsible for converting instances of the Dean model
    to and from JSON format. It allows data to be serialized for responses and deserialized
    for request data, enabling easy integration with Django REST framework views.
    """
    class Meta:
        model = Program
        fields = '__all__'
