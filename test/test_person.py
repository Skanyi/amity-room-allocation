import unittest
from unittest import TestCase
from app.person import Person, Fellow, Staff

class TestPerson(TestCase):

    def test_position_is_fellow(self):
        fellow1 = Fellow(1, 'Steve', 'Kanyi')
        self.assertEqual(fellow1.position.lower(), 'fellow')

    def test_position_is_staff(self):
        fellow1 = Fellow(1, 'Steve', 'Kanyi')
        self.assertEqual(fellow1.position.lower(), 'staff')

    def test_gender_female(self):
        person1 = Person(1, 'Angie', 'Mugo')
        self.assertEqual(person1.gender.upper(),'F')

    def test_gender_male(self):
        person2 = Person(2, 'Steve', 'Kanyi')
        self.assertEqual(person2.gender.upper(), 'M')

if __name__ == '__main__':
    unittest.main()
