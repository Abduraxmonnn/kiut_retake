# Rest-Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Project
from apps.retake.models import Retake, RetakeCase
from apps.services.retake_services import create_retake
from apps.user.models import User
from apps.main.subjects.models import Subject
from apps.retake.serializers import ApplyRetakeSerializer
from apps.user.custom_permissions import IsStudentOrReadOnly


class ApplyRetakeAPIView(APIView):
    permission_classes = [IsAuthenticated, IsStudentOrReadOnly]

    def post(self, request):
        serializer = ApplyRetakeSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        passport_issue_date = serializer.validated_data.get('passport_issue_date', None)
        passport_given_by = serializer.validated_data.get('passport_given_by', None)
        lang = serializer.validated_data.get('language', Retake.LanguageTypes.UZBEK)
        subject_name = serializer.validated_data['subject_name']
        case_index = serializer.validated_data['case_index']
        phone = serializer.validated_data.get('phone_number', None)

        student_id = request.user.student_id

        get_user = User.objects.get(student_id=student_id)
        get_subject = Subject.objects.filter(name=subject_name).first()
        get_case_index = RetakeCase.objects.get(case_index=case_index)

        if not get_user:
            return Response({
                'status': 'error',
                'message': 'User Not Found'
            }, status=status.HTTP_404_NOT_FOUND)

        if not get_subject or not get_case_index:
            return Response({
                'status': 'error',
                'message': 'Subject or Case Index Not Found'
            }, status=status.HTTP_404_NOT_FOUND)

        get_user.passport_issue_date = passport_issue_date or get_user.passport_issue_date
        get_user.passport_given_by = passport_given_by or get_user.passport_given_by
        get_user.phone_number = phone or get_user.phone_number
        get_user.save()

        created_retake = create_retake(
            language=lang,
            user=get_user,
            subject=get_subject,
            case_index=get_case_index
        )

        return created_retake
