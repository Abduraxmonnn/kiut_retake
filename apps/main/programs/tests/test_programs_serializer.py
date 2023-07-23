from django.test import TestCase

from apps.main.programs.models import Program
from apps.main.programs.serializers import ProgramSerializer


class ProgramsSerializerTestCase(TestCase):
    def test_serializer_reaction_to_correct(self):
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

    def test_serializer_reaction_to_incorrect(self):
        program_1 = Program.objects.create(name='Test_1')
        program_2 = Program.objects.create(name='Test_2')
        serializer_data = ProgramSerializer([program_1, program_2], many=True).data
        expected_data = [
            {
                'id': 3,
                'name': 'Test 3'
            },
            {
                'id': 4,
                'name': 'Test 4'
            }
        ]
        assert expected_data != serializer_data
        self.assertEqual(serializer_data[0]['name'], 'Test_1')
        self.assertEqual(serializer_data[1]['name'], 'Test_2')


