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


    def test_person_has_been_removed(self):
        '''
        Check thats the person has been removed from the room after reallocation
        '''
        pass

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
