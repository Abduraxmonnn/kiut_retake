# Django
import json

from django.test import TestCase, Client

# Rest Framework
from rest_framework.test import APITestCase
from rest_framework import status

# Project
from apps.main.rooms.models import Room


class RoomsAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.url = '/main/api/v1/rooms/'
        cls.create_room = Room.objects.create(build=f'{Room.BuildTypes.A_BUILD}',
                                              number=311,
                                              type_room=f'{Room.RoomTypes.LECTURE}')

    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('http://localhost:8000/main/api/v1/rooms/')
        self.assertEqual(response.status_code, 200)

    def test_list_rooms(self):
        """
        Test to list all the persons in the list
        """
        # self.test_add_room()

        response = self.client.get(self.url, format='json')
        json = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(json), 1)

    def test_room_exists(self):
        def test_create_room(self):
            """
            Tests creating a new person object
            """
            response = self.client.post(self.url, {
                'build': f'{Room.BuildTypes.C_BUILD}',
                'number': 711,
                'type_room': f'{Room.RoomTypes.PRACTICE}'
            })

            self.assertEquals(response.status_code, 409)
            self.assertEquals(response.data['message'], 'This Room Exists, Please check or create another Room')

    def test_put_rooms(self):
        """
        Test to see if put works
        """
        # self.test_add_room()

        data = {
            'build': f'{Room.BuildTypes.B_BUILD}',
            'number': 321,
            'type_room': f'{Room.RoomTypes.PRACTICE}'
        }

        response = self.client.put(f'/main/api/v1/rooms/{self.create_room.id}/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        update_room = Room.objects.get()
        self.assertEqual(update_room.build, Room.BuildTypes.B_BUILD)
        self.assertEqual(update_room.number, 321)
        self.assertEqual(update_room.type_room, Room.RoomTypes.PRACTICE)

    def test_delete_rooms(self):
        """
        Test to list all the persons in the list
        """

        # response = self.client.delete(f'/main/api/v1/rooms/{self.create_room.id}/')
        # self.assertEquals(response.status_code, 204)

        response = self.client.post(self.url, {
            'build': 'A_BUILD',
            'number': 510,
            'type_room': 'LECTURE'
        })

        self.assertEquals(response.status_code, 201)

        # Delete the task
        room_id = response.data['data']['id']
        response = self.client.delete(f"/main/api/v1/rooms/{room_id}/", format="json")
        self.assertEquals(response.status_code, 204)
        # response_to_json = response.json()
        #
        # self.assertEqual(len(response_to_json), 1)


class RoomTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.url = '/main/api/v1/rooms/'
        cls.create_obj = Room.objects.create(build=f'{Room.BuildTypes.A_BUILD}',
                                             number=311,
                                             type_room=f'{Room.RoomTypes.LECTURE}')

    def test_room_create_method(self):
        response = self.client.post(self.url, {
            'build': 'A_BUILD',
            'number': 420,
            'type_room': 'LECTURE'
        })

        room_17 = Room.objects.get(pk=self.create_obj.id)
        self.assertEquals(room_17.build, f'{Room.BuildTypes.A_BUILD}')
        self.assertEquals(room_17.number, 311)

    def test_room_delete_method(self):
        response = self.client.delete(f'/main/api/v1/rooms/{self.create_obj.id}/', json.dumps({
            'id': self.create_obj.id
        }))

        self.assertEquals(response.status_code, 204)
