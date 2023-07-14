from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.main.programs.models import Program
from apps.main.programs.serializers import ProgramSerializer


class ProgramAPITestCase(APITestCase):
    def test_create_program(self):
        url = reverse('programs-list')
        data = {
            'name': 'Test Program 1'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Program.objects.last().name, data['name'])

    def test_list_program(self):
        program_1 = Program.objects.create(name='Test_1')
        program_2 = Program.objects.create(name='Test_2')
        url = reverse('programs-list')
        response = self.client.get(url)
        serializer_data = ProgramSerializer([program_1, program_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data[::-1])


class BookUpdateTest(TestCase):
    def test_update_book(self):
        program_1 = Program.objects.create(name='Test_1')

        response = self.client.post(
            reverse('programs-update', kwargs={'pk': program_1.id}),
            {'name': 'Test_1 Updated'})

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        program_1.refresh_from_db()
        self.assertEqual(program_1.name, 'Test_1 Updated')
