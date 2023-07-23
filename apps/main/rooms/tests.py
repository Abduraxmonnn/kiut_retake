# Rest Framework
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status

# Project
from apps.main.rooms.models import Room

import logging

logger = logging.getLogger(__name__)


class RoomsTestCase(APITestCase):
    def test_add_room(self):
        """
        Adds a test person into the database
        """
        logger.debug('Adding a new person into database')
        create_room = Room(build=Room.BuildTypes.A_BUILD, number=320, type_room=Room.RoomTypes.LECTURE)
        create_room.save()
        logger.debug('Successfully added test person into the database')

    def test_list_rooms(self):
        """
        Test to list all the persons in the list
        """
        logger.debug('Starting test list rooms')

        self.test_add_room()

        url = 'https://localhost:8000%s' % reverse('rooms-list')
        logger.debug('Sending TEST data to url: %s' % url)
        response = self.client.get(url, format='json')
        json = response.json()

        logger.debug('Testing status code response: %s, code: %d' % (json, response.status_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        logger.debug('Testing result count')
        self.assertEqual(len(json), 1)

    def test_create_room(self):
        """
        Tests creating a new person object
        """
        logger.debug('Starting test create room')
        url = 'https://localhost:8000%s' % reverse('rooms-list')
        data = {
            "build": f"{Room.BuildTypes.A_BUILD}",
            "number": 311,
            "type_room": f"{Room.RoomTypes.LECTURE}"
        }

        logger.debug('Sending TEST data to url: %s, data: %s' % (url, data))
        print(data)
        response = self.client.post('/main/api/v1/rooms/', data=data, format='json')

        logger.debug('Testing status code response: %s, code: %d' % (response.json(), response.status_code))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        logger.debug('Testing room count to make sure object was successfully added')
        self.assertEqual(Room.objects.count(), 1)

        logger.debug('Testing new room object details')
        created_room = Room.objects.get()
        self.assertEqual(created_room.build, 'A_BUILD')
        self.assertEqual(created_room.number, 310)
        self.assertEqual(created_room.type_room, 'LECTURE')

        logger.debug('Test room create completed successfully')

    def test_put_persons(self):
        """
        Test to see if put works
        """
        logger.debug('Starting test put room')

        self.test_add_room()

        url = 'https://localhost:8000%s1/' % reverse('rooms-list')
        logger.debug('Sending TEST data to url: %s' % url)
        data = {
            'build': Room.BuildTypes.A_BUILD,
            'number': 311,
            'type_room': Room.RoomTypes.LECTURE
        }

        response = self.client.put(url, data, format='json')

        logger.debug('Testing to see if status code is correct')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        logger.debug('Testing modified room object details')
        update_room = Room.objects.get()
        self.assertEqual(update_room.build, Room.BuildTypes.A_BUILD)
        self.assertEqual(update_room.number, 311)
        self.assertEqual(update_room.type_room, Room.RoomTypes.LECTURE)

        logger.debug('Test room put completed successfully')

    def test_delete_rooms(self):
        """
        Test to list all the persons in the list
        """
        logger.debug('Starting test list persons')

        data = {
            'build': Room.BuildTypes.A_BUILD,
            'number': 311,
            'type_room': Room.RoomTypes.LECTURE
        }

        logger.debug('Removing room from database')
        response_create = self.client.post("/main/api/v1/rooms/", data=data, format="json")
        room_id = response_create.data["id"]
        logger.info(f"Created task with id: {room_id}")
        logger.info(f"Response: {response_create.data}")
        assert response_create.status_code == 201
        assert response_create.data["number"] == data["number"]
        logger.debug('Successfully added test person into the database')

        # Delete the task
        response = self.client.delete(f"/main/api/v1/rooms/{room_id}", format="json")
        assert response.status_responsecode == 204
        json = response.json()

        logger.debug('Testing status code response: %s, code: %d' % (json, response.status_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        logger.debug('Testing result count')
        self.assertEqual(len(json), 1)
