import unittest
from unittest import TestCase
from app.amity import *

class TestAmity(TestCase):

    def setUp(self):
        self.room1 = Amity()

    def test_load_people(self):
        '''
        Check that every person does not exist in the system before
        loading them.
        '''
        #ask more and read on this
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
