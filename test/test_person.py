import unittest
from unittest import TestCase
from app.person import *
from app.amity import *
import unittest.mock as mock

class TestPerson(TestCase):

    def test_add_person_staff(self):
        Amity.staffs = []
        self.assertEqual(len(Amity.staffs), 0)
        Amity.add_person(1, 'steve', 'kanyi', 'Staff')
        self.assertNotEqual(len(Amity.staffs), 0, 'Person staff has not been added')

    def test_add_person_fellow(self):
        Amity.fellows = []
        self.assertEqual(len(Amity.fellows), 0)
        Amity.add_person(1, 'steve', 'kanyi', 'Fellow')
        self.assertNotEqual(len(Amity.fellows), 0, 'Person fellow has not been added')

    def test_position_is_fellow(self):
        fellow1 = Fellow(2, 'Angie', 'Mugo')
        self.assertEqual(fellow1.position.lower(), 'fellow', 'The position must be a fellow')

    def test_position_is_staff(self):
        staff1 = Staff(3, 'Joshua', 'Mwaniki')
        self.assertEqual(staff1.position.lower(), 'staff', 'The position must be a staff')

    def test_allocate_office(self):
        Amity.create_room('Carmel')
        self.assertTrue('Carmel' in Amity.office_rooms)
        Amity.allocate_office('Carmel')
        self.assertNotEqual(len(Amity.office_rooms['Carmel']), 0, 'person1 has not been added to the office')

    def test_allocate_living_space(self):
        Amity.create_room('PHP')
        self.assertTrue('PHP', in Amity.ls_rooms)
        Amity.allocate_living_space('PHP')
        self.assertNotEqual(len(Amity.ls_rooms['PHP']), 0, 'person1 has not been added to living space')

    def test_reallocate_person(self):
        Amity.reallocate_person(1, 'PHP')
        self.assertIn(1, Amity.all_people.keys(), 'person1 does not exist')
        self.assertIn('PHP', Amity.rooms, 'PHP room does not exist')

    @mock.patch('app.amity.open')
    def test_load_people_calls_open_function(self, mock_open):
        Amity.load_people('data/people.txt')
        mock_open.assert_called_with('data/people.txt')

    def test_load_people_read_lines(self):
        with mock.patch.object(Amity, 'add_person') as mock_method:
            Amity.load_people('data/people.txt')
        mock_method.assert_called_with(1, 'OLUWAFEMI', 'SULE', 'FELLOW', 'Y')
