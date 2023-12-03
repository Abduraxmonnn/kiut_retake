# Rest-Framework
from rest_framework.views import APIView

# Project
from apps.main.faculty_directions.models import FacultyDirections
from apps.main.faculty_directions.serializers import FacultyDirectionToDeanListSerializer


class FacultyDirectionToDeanListAPIView(APIView):
    def list(self, request):
        queryset = FacultyDirections.objects.all()
        serializer = FacultyDirectionToDeanListSerializer(queryset, many=True)
        return {serializer.data}
