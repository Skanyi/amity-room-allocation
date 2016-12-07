import unittest
from unittest import TestCase
from app.amity import *
from app.room import *

class TestRoom(TestCase):

    def test_room_does_not_exist(self):
        room1 = Amity.create_room('PHP', 'Office')
        self.assertIn('PHP', Amity.rooms, 'PHP does not exist')

    def test_create_office_room(self):
        Amity.office_rooms = []
        self.assertEqual(len(Amity.office_rooms), 0)
        Amity.create_room('Carmel', 'office')
        self.assertNotEqual(len(Amity.office_rooms), 0)

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

    def test_create_ls_room(self):
        Amity.ls_rooms = []
        self.assertEqual(len(Amity.ls_rooms), 0)
        Amity.create_room('Carmel', 'livingspace')
        self.assertNotEqual(len(Amity.ls_rooms), 0)
