from django.test import TestCase

from apps.main.rooms.models import Room
from apps.main.rooms.serializers import RoomSerializer


class RoomsTestCaseSerializer(TestCase):
    def test_serializer_reaction_to_correct(self):
        room_1 = Room.objects.create(
            build=f'{Room.BuildTypes.A_BUILD}',
            number=610,
            type_room=f'{Room.RoomTypes.LECTURE}'
        )
        room_2 = Room.objects.create(
            build=f'{Room.BuildTypes.B_BUILD}',
            number=803,
            type_room=f'{Room.RoomTypes.PRACTICE}'
        )
        serializer_data = RoomSerializer([room_1, room_2], many=True).data
        expected_data = [
            {
                'id': room_1.id,
                'build': f'{Room.BuildTypes.A_BUILD}',
                'number': 610,
                'type_room': f'{Room.RoomTypes.LECTURE}'
            },
            {
                'id': room_2.id,
                'build': f'{Room.BuildTypes.B_BUILD}',
                'number': 803,
                'type_room': f'{Room.RoomTypes.PRACTICE}'
            }
        ]
        self.assertEqual(expected_data, serializer_data)

    def test_serializer_rection_to_incorrect(self):
        room_1 = Room.objects.create(
            build=f'{Room.BuildTypes.A_BUILD}',
            number=310,
            type_room=f'{Room.RoomTypes.LECTURE}'
        )
        room_2 = Room.objects.create(
            build=f'{Room.BuildTypes.B_BUILD}',
            number=203,
            type_room=f'{Room.RoomTypes.PRACTICE}'
        )
        serializer_data = RoomSerializer([room_1, room_2], many=True).data
        expected_data = [
            {
                'id': 12,
                'build': f'{Room.BuildTypes.C_BUILD}',
                'number': 810,
                'type_room': f'{Room.RoomTypes.PRACTICE}'
            },
            {
                'id': 32,
                'build': f'{Room.BuildTypes.A_BUILD}',
                'number': 203,
                'type_room': f'{Room.RoomTypes.PRACTICE}'
            }
        ]
        assert expected_data != serializer_data
        self.assertEqual(serializer_data[0]['build'], f'{Room.BuildTypes.A_BUILD}')
        self.assertEqual(serializer_data[0]['number'], 310)
        self.assertEqual(serializer_data[1]['build'], f'{Room.BuildTypes.B_BUILD}')
        self.assertEqual(serializer_data[1]['number'], 203)
