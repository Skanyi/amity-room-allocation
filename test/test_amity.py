import unittest
from unittest import TestCase
from app.amity import Amity
import unittest.mock as mock

class TestAmity(TestCase):


    def test_room_does_not_exist(self):
        Amity.create_room('Oculus', 'Office')
        self.assertTrue('Oculus' in Amity.all_rooms)
        response = Amity.create_room('Oculus', 'Office')
        self.assertEqual(response, "Room already exists")

    def test_create_office_room(self):
        Amity.office_rooms = []
        self.assertEqual(len(Amity.office_rooms), 0)
        Amity.create_room('Carmel', 'office')
        self.assertNotEqual(len(Amity.office_rooms), 0)

    def test_create_room(self):
        previous_room_count = len(Amity.all_rooms)
        self.assertFalse('Oculus' in Amity.all_rooms)
        Amity.create_room('Oculus', 'Office')
        self.assertTrue('Oculus' in Amity.all_rooms)
        new_room_count = len(Amity.all_rooms)
        self.assertEqual(self.previous_room_count + 1, new_room_count)

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

    def test_allocate_office(self):
        Amity.office_rooms = []
        self.assertEqual(len(Amity.office_rooms), 0)
        Amity.create_room('Carmel', 'office')
        self.assertNotEqual(len(Amity.office_rooms), 0)
        previous_people_count = len(Amity.office_rooms['Carmel'])
        Amity.allocate_office('Carmel')
        current_people_count = len(Amity.office_rooms['Carmel'])
        self.assertEqual(previous_people_count + 1, current_people_count, 'Has not been added to the office')


    def test_allocate_living_space(self):
        Amity.create_room('Go', 'livingspace')
        self.assertTrue('Go' in Amity.ls_rooms)
        previous_people_count = len(Amity.ls_rooms['Go'])
        Amity.allocate_living_space('Go')
        current_people_count = len(Amity.ls_rooms['Go'])
        self.assertEqual(previous_people_count + 1, current_people_count, 'Has not been added to the office')

    def test_reallocate_person(self):
        self.assertIn('PHP', Amity.all_rooms)
        Amity.create_room('PHP', 'livingspace')
        self.assertIn('PHP', Amity.all_rooms)
        Amity.add_person(1, 'steve', 'kanyi', 'F')
        Amity.ls_rooms = {'PHP':[]}
        self.assertNotIn(1, Amity.ls_rooms['PHP'])
        Amity.reallocate_person(1, 'PHP')
        self.assertIn(1, Amity.ls_rooms['PHP'])

    @mock.patch('app.amity.open')
    def test_load_people_calls_open_function(self, mock_open):
        Amity.load_people('data/people.txt')
        mock_open.assert_called_with('data/people.txt')

    def test_load_people_read_lines(self):
        with mock.patch.object(Amity, 'add_person') as mock_method:
            Amity.load_people('data/people.txt')
        mock_method.assert_called_with(1, 'OLUWAFEMI', 'SULE', 'FELLOW', 'Y')
