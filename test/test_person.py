import unittest
from unittest import TestCase
from app.person import Person

class TestPerson(TestCase):

    def test_add_person(self):
        '''
        Test that the person being added is not already in the system
        '''
        pass

    def test_position(self):
        '''
        Test that there only two type of positions, fellow and staff
        '''
        pass

    def test_gender(self):
        '''
        Ensures that only male and female genders options are available
        to ease allocation of living space
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
