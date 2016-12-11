import unittest
from unittest import TestCase
from app.room import *

class TestRoom(TestCase):

    def test_max_office_occupants(self):
        office1 = Office('Carmel')
        self.assertEqual(office1.max_occupants, 6)

    def test_room_is_office(self):
        office1 = Office('Carmel')
        self.assertEqual(office1.room_type.upper(), 'O')

    def test_max_livingspace_occupants(self):
        ls1 = LivingSpace('PHP')
        self.assertEqual(ls1.max_occupants, 4)

    def test_room_is_ls(self):
        ls1 = LivingSpace('PHP')
        self.assertEqual(ls1.room_type.upper(), 'L')
