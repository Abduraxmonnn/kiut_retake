# Django
from django.contrib.auth import authenticate, login

# Rest-Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Project
from apps.user.serializers import UserLogInSerializer
from apps.user.models import User


class UserLogInAPIView(APIView):
    def post(self, request):
        serializer = UserLogInSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        student_id = serializer.validated_data['student_id']
        password = serializer.validated_data['password']

        try:
            user = User.objects.get(student_id=student_id)

            if user is not None:
                if user.check_password(password):
                    if user.is_active:
                        user_data = {
                            'student_id': student_id,
                            'full_name': user.full_name,
                            'univer_group': user.univer_group.name
                        }

                        login(request, user=user)
                        return Response({
                            "data": user_data,
                            "message": "Login successful."
                        }, status=status.HTTP_200_OK)
                    else:
                        return Response({"message": "User is Inactive."}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"message": "Password Incorrect."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"message": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({"message": "User does not exists."}, status=status.HTTP_400_BAD_REQUEST)
