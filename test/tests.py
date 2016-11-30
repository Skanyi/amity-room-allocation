import unittest
from unittest import TestCase
from amity import Amity
from room import Office

class TestRoom(TestCase):

    def setUp(self):
        self.room1 = Office()

    def test_max_office_occupants(self):
        '''
        Check that the minimum ocupants office is 0 and maximum occupants is 
        6
        '''
        self.assertEqual(self.room1.room_max_occupants, 6)

    def test_max_livingspace_occupants(self):
        '''
        Check that the minimum occupants of a room is 0 and maximum 
        is 4
        '''
        self.assertEqual(self.room1.room_max_occupants, 4)

    def test_create_room(self):
        '''
        Check that the functions creats a room when called
        '''
        pass

    def test_room_type(self):
        '''
        Ensures that only two type of rooms, that is office and living space 
        can be created by the create room function
        '''
        pass

    def test_room_wing(self):
        '''
        Ensures that only two type of living space wings are created,
        that is the male_wing and female_wing
        '''
        pass

    def test_add_person(self):
        '''
        Test that the person being added is not already in the system
        '''
        pass

    def test_gender(self):
        '''
        Ensures that only male and female genders options are available 
        to ease allocation of living space
        '''
        pass

    def test_position(self):
        '''
        Test that there only two type of positions, fellow and staff
        '''
        pass

    def test_allocate_office(self):
        '''
        Ensure that the office allocation is really random,
        Ensure that the office is not full before allocation
        '''
        pass

    def test_allocate_living_space(self):
        '''
        Ensure that the living space allocation is really random,
        Ensure that the living space is not full before allocation
        '''
        pass


    def test_load_people(self):
        '''
        Check that every person does not exist in the system before
        loading them. 
        '''
        #ask more and read on this
        pass






if __name__ == '__main__':
    unittest.main()
