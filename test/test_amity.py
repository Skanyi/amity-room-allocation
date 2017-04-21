import unittest
from unittest import TestCase
from app.amity import Amity
import unittest.mock as mock
import os
from collections import defaultdict

class TestAmity(TestCase):

    def setUp(self):
        Amity.office_rooms = defaultdict(list)
        Amity.ls_rooms = defaultdict(list)
        Amity.all_rooms  = []
        Amity.staffs = []
        Amity.fellows = []
        Amity.all_people = {}
        Amity.unallocated_person = []

    def test_room_does_not_exist(self):
        Amity.create_room('Oculus', 'O')
        self.assertTrue('OCULUS' in Amity.all_rooms)
        response = Amity.create_room('OCULUS', 'O')
        self.assertEqual(response, "Room already exists")

    def test_create_office(self):
        previous_room_count = len(Amity.all_rooms)
        self.assertFalse('Oculus' in Amity.all_rooms)
        Amity.create_room('Oculus', 'O')
        self.assertTrue('Oculus'.upper() in Amity.all_rooms)
        new_room_count = len(Amity.all_rooms)
        self.assertEqual(previous_room_count + 1, new_room_count)

    def test_create_ls(self):
        previous_room_count = len(Amity.all_rooms)
        self.assertFalse('Go' in Amity.all_rooms)
        Amity.create_room('Go', 'L')
        self.assertTrue('Go'.upper() in Amity.all_rooms)
        new_room_count = len(Amity.all_rooms)
        self.assertEqual(previous_room_count + 1, new_room_count)

    def test_add_person_staff(self):
        previous_staff_count = len(Amity.staffs)
        self.assertFalse('PERCILA NJIRA' in Amity.all_people)
        Amity.add_person('PERCILA', 'NJIRA', 'S')
        self.assertTrue('PERCILA NJIRA' in Amity.all_people)
        current_staff_count = len(Amity.staffs)
        self.assertEqual(previous_staff_count + 1, current_staff_count,  'Person staff has not been added')

    def test_add_person_fellow(self):
        previous_fellow_count = len(Amity.fellows)
        self.assertFalse('STEVE KANYI' in Amity.all_people)
        Amity.add_person('steve', 'kanyi', 'F', 'Y')
        self.assertTrue('STEVE KANYI' in Amity.all_people)
        current_fellow_count = len(Amity.fellows)
        self.assertEqual(previous_fellow_count + 1, current_fellow_count, 'Person fellow has not been added')

    def test_generate_random_office_from_office_rooms(self):
        random_office = Amity.generate_random_office()
        self.assertTrue(random_office in Amity.office_rooms)

    def test_generate_random_living_space_from_ls_rooms(self):
        random_ls = Amity.generate_random_living_space()
        self.assertEqual(random_ls, 'There are no living spaces available')

    def test_reallocate_person(self):
        Amity.create_room('PHP', 'l')
        Amity.add_person('steve', 'kanyi', 'F', 'Y')
        self.assertIn('STEVE KANYI', Amity.ls_rooms['PHP'])
        Amity.create_room('GO', 'l')
        Amity.reallocate_person_to_ls('steve kanyi', 'GO')
        self.assertIn('STEVE KANYI', Amity.ls_rooms['GO'])
        self.assertNotIn('STEVE KANYI', Amity.ls_rooms['PHP'])


    @mock.patch('app.amity.open')
    def test_load_people_calls_open_function(self, mock_open):
        Amity.load_people('data/people.txt')
        mock_open.assert_called_with('data/people.txt')

    def test_load_people_read_lines(self):
        dirname = os.path.dirname(os.path.realpath(__file__))
        with mock.patch.object(Amity, 'add_person') as mock_method:
            Amity.load_people(os.path.join(dirname, 'data/people.txt'))
        mock_method.assert_any_call(firstname='OLUWAFEMI', lastname='SULE', position='F', wants_accomodation='Y')
        mock_method.assert_any_call(firstname='LEIGH', lastname='RILEY', position='S', wants_accomodation='N')
        self.assertEqual(mock_method.call_count, 7)
