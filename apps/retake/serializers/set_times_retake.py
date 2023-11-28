# Rest-Framework
from rest_framework import serializers

# Project
from apps.main.rooms.models import Room


class RoomForSetTimesRetakeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = [
            'build',
            'number',
            'type_room'
        ]


class SetTimesRetakeSerializer(serializers.Serializer):
    student_id = serializers.ListField(child=serializers.CharField(), required=True)
    retake_date = serializers.DateField()
    retake_time = serializers.TimeField()
    retake_room = RoomForSetTimesRetakeSerializer(many=False)
