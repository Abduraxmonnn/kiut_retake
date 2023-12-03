# Django
from django.db.models import Sum

# Rest-Framework
from rest_framework import serializers

from apps.main.fails.models import Fail
# Project
from apps.main.univer_groups.models import UniverGroup
from apps.main.faculty_directions.serializers import FacultyDirectionToDeanListSerializer
from apps.user.models import User


class GroupStatsMixin:
    def calculate_group_stats(self, instance):
        users = User.objects.filter(univer_group__name=instance.name)
        total_fails = Fail.objects.filter(user__univer_group__name=instance.name).count()
        total_score = 0
        for user in users:
            fail = Fail.objects.filter(user=user)
            if fail:
                fail_score = fail.aggregate(Sum('score'))['score__sum']
                if fail_score:
                    total_score += fail_score
        return {
            'total_students': len(users),
            'total_fails': total_fails,
            'average_score': total_score / len(users) if users else 0,
        }


class UniverGroupToDeanListSerializer(GroupStatsMixin, serializers.ModelSerializer):
    faculty_dirs = FacultyDirectionToDeanListSerializer(many=False)

    class Meta:
        model = UniverGroup
        fields = [
            'id',
            'name',
            'level',
            'type_education',
            'language',
            'faculty_dirs',
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        stats = self.calculate_group_stats(instance)
        data.update(stats)
        return data


class StudentToDeanListSerializer(GroupStatsMixin, serializers.ModelSerializer):
    faculty_dirs = FacultyDirectionToDeanListSerializer(many=False)

    class Meta:
        model = UniverGroup
        fields = [
            'id',
            'name',
            'level',
            'type_education',
            'language',
            'faculty_dirs',
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        stats = self.calculate_group_stats(instance)
        data.update(stats)
        return data
