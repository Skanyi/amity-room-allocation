import unittest
from unittest import TestCase
from app.person import *

class TestPerson(TestCase):

    def test_add_person_staff(self):
        staff1 = Person.add_person(1, 'steve', 'kanyi', 'M', 'Staff')
        self.assertNotEqual(len(Person.staffs), 0)

    def test_add_person_male_fellow(self):
        m_fellow1 = Person.add_person(1, 'steve', 'kanyi', 'M', 'Staff')
        self.assertNotEqual(len(Person.staffs), 0)

    def test_add_person_female_fellow(self):
        f_fellow1 = Person.add_person(1, 'steve', 'kanyi', 'M', 'Staff')
        self.assertNotEqual(len(Person.staffs), 0)


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
