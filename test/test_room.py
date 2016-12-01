import unittest
from unittest import TestCase
from app.room import Room, Office, LivingSpace
#from app.room import Office, LivingSpace

class TestRoom(TestCase):

    def test_max_office_occupants(self):
        '''
        Check that the minimum ocupants office is 0 and maximum occupants is
        6
        '''
        office1 = Office('Carmel')
        self.assertEqual(office1.max_occupants, 6)
        self.assertEqual(office1.room_type, 'office')

    def test_max_livingspace_occupants(self):
        '''
        Check that the minimum occupants of a room is 0 and maximum
        is 4; ls = LivingSpace1
        '''
        ls1 = LivingSpace('PHP')
        self.assertEqual(ls1.max_occupants, 4)
        self.assertEqual(ls1.room_type, 'livingspace')


if __name__ == '__main__':
    unittest.main()
