# Rest-Framework
from rest_framework import serializers

# Project
from apps.main.fails.models import Fail
from apps.main.subjects.models import Subject
from apps.main.univer_groups.serializers import UniverGroupSerializer
from apps.user.models import User
from apps.main.subjects.serializers import SubjectSerializer


class UserForFailListSerializer(serializers.ModelSerializer):
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


class FailOfStudentListSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(many=False)
    user = UserForFailListSerializer(many=False)
    status_color = serializers.SerializerMethodField()

    def get_status_color(self, obj):
        score = obj.score
        if score <= 20:
            return 'red'
        elif 20 < score <= 40:
            return 'orange'
        elif 40 < score <= 60:
            return 'green'

    class Meta:
        model = Fail
        fields = [
            'id',
            'subject',
            'user',
            'subject_credit',
            'semester',
            'score',
            'status_color',
            'is_free'
        ]
