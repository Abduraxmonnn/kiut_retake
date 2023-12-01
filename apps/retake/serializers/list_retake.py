# Rest-Framework
from rest_framework import serializers

# Project
from apps.retake.models import RetakeCase, Retake
from apps.main.univer_groups.serializers import UniverGroupSerializer
from apps.user.models import User
from apps.main.subjects.serializers import SubjectSerializer


class UserForRetakeListSerializer(serializers.ModelSerializer):
    univer_group = UniverGroupSerializer(many=False)

    class Meta:
        model = User
        fields = [
            'id',
            'student_id',
            'full_name',
            'fails',
            'univer_group',
        ]


class RetakeCaseForRetakeList(serializers.ModelSerializer):
    class Meta:
        model = RetakeCase
        fields = '__all__'


class RetakeListSerializer(serializers.ModelSerializer):
    user = UserForRetakeListSerializer(many=False)
    case = RetakeCaseForRetakeList(many=False)
    subject = SubjectSerializer(many=False)

    class Meta:
        model = Retake
        fields = '__all__'


class RetakeListForDeanSerializer(serializers.ModelSerializer):
    user = UserForRetakeListSerializer(many=False)
    case = RetakeCaseForRetakeList(many=False)
    subject = SubjectSerializer(many=False)

    class Meta:
        model = Retake
        fields = '__all__'
