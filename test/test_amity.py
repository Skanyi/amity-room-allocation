import unittest
from unittest import TestCase
from app.amity import *
import unittest.mock as mock

class TestAmity(TestCase):

    @mock.patch('app.room.print', create=True)
    def test_print_room_empty(self, mock_print):
        Room.print_room('room_name')
        mock_print.assert_called_with('room_name')

    @mock.patch('app.room.print', create=True)
    def test_print_room_with_members(self, mock_print):
        room1 = Room()
        room1.create_room('Carmel', 'office')
        person1 = Fellow(1, 'Steve', 'kanyi')
        person2 = Staff(2, 'Kevin', 'Ndungu')
        person1.allocate_office('Carmel')
        person1.allocate_office('Carmel')
        Room.print_room('Carmel')
        mock_print.assert_called_with('Carmel')
        mock_print.assert_called_with('Steve, Kevin')

    def test_load_state(self):
        '''
        test if the data is loaded from the database to the app
        '''
        pass

    def test_save_state(self):
        '''
        test if the data in the app is saved to the database
        '''
        pass
