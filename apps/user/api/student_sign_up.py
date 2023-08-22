# Rest-Framework
from rest_framework.views import APIView, Response
from rest_framework import status

# Project
from apps.user.models import User
from apps.main.univer_groups.models import UniverGroup
from apps.user.serializers import UserSignUpSerializer


class StudentSignUpAPIView(APIView):
    model = User
    queryset = User.objects.order_by('-id').all()
    serializer_class = UserSignUpSerializer

    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        student_id = serializer.validated_data['student_id']
        full_name = serializer.validated_data['full_name']
        passport_number = serializer.validated_data['passport_number']
        passport_issue_date = serializer.validated_data['passport_issue_date']
        gender = serializer.validated_data['gender']
        password = serializer.validated_data['password']
        univer_group = serializer.validated_data['univer_group']
        check_user = User.objects.filter(student_id=student_id)
        if check_user.exists():
            return Response({'error': 'User exists'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            get_univer_group = UniverGroup.objects.get(name=univer_group)
        except UniverGroup.DoesNotExist:
            return Response({"message": "Univer Group with this name does not exists"},
                            status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_student(student_id=student_id, password=password)
        user.student_id = student_id
        user.full_name = full_name
        user.passport_number = passport_number
        user.passport_issue_date = passport_issue_date
        user.passport_expiry_date = user.calculate_passport_expiry_date
        user.gender = gender
        user.univer_group = get_univer_group
        user.is_active = True

        user.save()
        return Response({
            'message': 'Registration successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
