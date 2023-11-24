# Rest-Framework
from rest_framework import serializers


class ApplyRetakeSerializer(serializers.Serializer):
    passport_issue_date = serializers.DateField()
    passport_given_by = serializers.CharField(max_length=255)
    language = serializers.CharField(max_length=2, allow_blank=True, allow_null=True)
    # user = serializers.CharField(max_length=15) instead, use request.user.username
    subject_name = serializers.CharField()
    case_index = serializers.IntegerField()
    phone_number = serializers.IntegerField(allow_null=True)
