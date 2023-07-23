# RestFramework
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

# Project
from apps.main.rooms.models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
