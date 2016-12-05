import unittest
from unittest import TestCase
from app.person import *
from app.room import *
import unittest.mock as mock

class TestPerson(TestCase):

    def test_add_person_staff(self):
        staff1 = Person.add_person(1, 'steve', 'kanyi', 'Staff')
        self.assertNotEqual(len(Person.staffs), 0, 'Person staff has not been added')

    def test_add_person_fellow(self):
        fellow1 = Person.add_person(1, 'steve', 'kanyi', 'Staff')
        self.assertNotEqual(len(Person.fellows), 0, 'Person fellow has not been added')

    def test_position_is_fellow(self):
        fellow1 = Fellow(1, 'Steve', 'Kanyi')
        self.assertEqual(fellow1.position.lower(), 'fellow', 'The position must be a fellow')

    def test_position_is_staff(self):
        fellow1 = Fellow(1, 'Steve', 'Kanyi')
        self.assertEqual(fellow1.position.lower(), 'staff', 'The position must be a staff')

    def test_allocate_office(self):
        person1 = Person.allocate_office('Carmel')
        self.assertNotEqual(len(Room.office_rooms['Carmel']), 0, 'person1 has not been added to the office')

    def test_allocate_living_space(self):
        person1 = Person.allocate_living_space('PHP')
        self.assertNotEqual(len(Room.ls_rooms['PHP']), 0, 'person1 has not been added to living space')

    def test_reallocate_person(self):
        person1 = Person(1, 'Steve', 'Kanyi')
        person1.reallocate_person(1, 'PHP')
        self.assertIn(1, Person.all_people.keys(), 'person1 does not exist')
        self.assertIn('PHP', Room.rooms, 'PHP room does not exist')

    @mock.patch('app.person.open')
    def test_load_people_calls_open_function(self, mock_open):
        Person.load_people('data/people.txt')
        mock_open.assert_called_with('data/people.txt')

    def test_load_people_read_lines(self):
        with mock.patch.object(Person, 'add_person') as mock_method:
            Person.load_people('data/people.txt')
        mock_method.assert_called_with(1, 'OLUWAFEMI', 'SULE', 'FELLOW', 'Y')
