import unittest
from unittest import TestCase
from amity import Amity
from room import Office

class TestRoom(TestCase):

    def setUp(self):
        self.room1 = Office()

    def test_office_occupants(self):
        self.assertEqual(self.room1.room_max_occupants, 6)

    def test_room_type(self):
        pass

if __name__ == '__main__':
    unittest.main()
