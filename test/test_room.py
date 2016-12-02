import unittest
from unittest import TestCase
from app.room import *
#from app.room import Office, LivingSpace

class TestRoom(TestCase):

    def test_room_does_not_exist(self):
        self.room1 = Room()
        self.room1.create_room('PHP', 'Office')
        self.assertIn('PHP', Room.rooms)

    def test_add_office_room(self):
        Room.office_rooms = []
        office1 = Room.create_room('Carmel', 'office')
        self.assertNotEqual(len(Room.office_rooms), 0)

    def test_max_office_occupants(self):
        office1 = Office('Carmel')
        self.assertEqual(office1.max_occupants, 6)

    def test_room_is_office(self):
        office1 = Office('Carmel')
        self.assertEqual(office1.room_type.upper(), 'OFFICE')

    def test_max_livingspace_occupants(self):
        ls1 = LivingSpace('PHP')
        self.assertEqual(ls1.max_occupants, 4)

    def test_room_is_ls(self):
        ls1 = LivingSpace('PHP')
        self.assertEqual(ls1.room_type.upper(), 'LIVINGSPACE')

    def test_add_ls_room(self):
        Room.ls_rooms = []
        ls1 = Room.create_room('Carmel', 'livingspace')
        self.assertNotEqual(len(Room.office_rooms), 0)

if __name__ == '__main__':
    unittest.main()
