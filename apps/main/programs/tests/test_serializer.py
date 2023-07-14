from django.test import TestCase

from apps.main.programs.models import Program
from apps.main.programs.serializers import ProgramSerializer


class TestCaseSerializer(TestCase):
    def test_serializer(self):
        program_1 = Program.objects.create(name='Test_1')
        program_2 = Program.objects.create(name='Test_2')
        serializer_data = ProgramSerializer([program_1, program_2], many=True).data
        expected_data = [
            {
                'id': program_1.id,
                'name': 'Test_1'
            },
            {
                'id': program_2.id,
                'name': 'Test_2'
            }
        ]
        self.assertEqual(expected_data, serializer_data)
