# Rest-Framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Project
from apps.main.fails.models import Fail
from apps.main.subjects.models import Subject
from apps.services.retake_services import check_for_free
from apps.user.models import User
from apps.main.fails.serializers import FailCreateSerializer


class FailCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = {
            'subject': request.data.get('subject', None),
            'user': request.user.id
        }
        serializer = FailCreateSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        subject = serializer.validated_data['subject'].upper()
        user = serializer.validated_data['user']

        get_subject = Subject.objects.filter(name=subject).first()
        is_free = check_for_free(user=user, subject=subject)

        if not get_subject:
            return Response({"message": "Subject does not Exists"}, 400)

        if not User.objects.get(student_id=user.student_id).is_active:
            return Response({"message": "User are not Active."}, 400)

        Fail.objects.create(
            subject=get_subject,
            user=user,
            is_free=is_free).save()

        return Response({
            'student_id': request.user.student_id,
            'message': 'Fail created Successfully'
        }, 200)
