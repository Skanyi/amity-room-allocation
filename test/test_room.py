import unittest
from unittest import TestCase
from app.room import Room, Office, LivingSpace
#from app.room import Office, LivingSpace

class TestRoom(TestCase):

    def test_max_office_occupants(self):

        office1 = Office('Carmel')
        self.assertEqual(office1.max_occupants, 6)

    def test_max_livingspace_occupants(self):

        ls1 = LivingSpace('PHP')
        self.assertEqual(ls1.max_occupants, 4)
        self.assertEqual(ls1.room_type, 'livingspace')


if __name__ == '__main__':
    unittest.main()
