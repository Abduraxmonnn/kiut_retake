# Rest-Framework
from rest_framework import status
from rest_framework.response import Response

# Project
from apps.retake.models import Retake


def create_retake(language, user, subject, case_index):
    try:
        created_retake = Retake.objects.create(
            language=language,
            user=user,
            subject=subject,
            case=case_index
        )
        created_retake_data = {
            'id': created_retake.id,
            'language': created_retake.language,
            'user': created_retake.user.id,
            'subject': created_retake.subject.id,
            'case': created_retake.case.id,
            'retake_date': None,
            'retake_time': None
        }
    except Exception as ex:
        return Response({
            'status': 'error',
            'message': 'Raise while creating Retake',
            'error': ex
        }, status=status.HTTP_400_BAD_REQUEST)
    else:
        created_retake.save()
        return Response({
            'status': 'successfully',
            'message': created_retake_data
        }, status=status.HTTP_201_CREATED)


def is_check_retake_for_free(user, subject):
    check_is_free = Retake.objects.filter(subject=subject)

    for item in check_is_free:
        return True if item.user == user else False

    # return False if check_is_free.exists() else True
