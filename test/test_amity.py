import unittest
from unittest import TestCase
from app.amity import Amity

class TestAmity(TestCase):

    def test_create_room(self):
        '''
        Check that the functions creates a room when called
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

    def test_load_people(self):
        '''
        Check that every person does not exist in the system before
        loading them.
        '''
        #ask more and read on this
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

    def test_reallocate_person(self):
        '''
        Check that the id already exist. Confirm the room of reallocation
        is not full
        '''
        pass

    def test_person_has_been_removed(self):
        '''
        Check thats the person has been removed from the room after reallocation
        '''
        pass


if __name__ == '__main__':
    unittest.main()
