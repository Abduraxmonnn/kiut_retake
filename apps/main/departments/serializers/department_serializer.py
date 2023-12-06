# Rest-Framework
from rest_framework import serializers

# Project
from apps.main.departments.models import Department
from apps.user.models import User


class HeadOfDepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'student_id',
            'full_name',
            'fails',
            'gender'
        ]


class DepartmentSerializer(serializers.ModelSerializer):
    head_of_department = HeadOfDepartmentSerializer(many=False)

    class Meta:
        model = Department
        fields = [
            'pk',
            'name',
            'description',
            'head_of_department'
        ]
