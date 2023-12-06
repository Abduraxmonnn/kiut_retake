# Rest-Framework
from rest_framework import serializers

# Project
from apps.retake.serializers.set_times_retake_serializer import RoomForSetTimesRetakeSerializer


class UpdateRetakeSerializer(serializers.Serializer):
    retake_date = serializers.DateField(required=False)
    retake_time = serializers.TimeField(required=False)
    retake_room = RoomForSetTimesRetakeSerializer(many=False, required=False)
