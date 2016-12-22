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
        Amity.all_rooms  = {}
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
        Amity.create_room('NARNIA', 'O')
        previous_staff_count = len(Amity.staffs)
        self.assertFalse('PERCILA NJIRA' in Amity.all_people)
        Amity.add_person('PERCILA', 'NJIRA', 'S')
        self.assertTrue('PERCILA NJIRA' in Amity.all_people)
        current_staff_count = len(Amity.staffs)
        self.assertEqual(previous_staff_count + 1, current_staff_count,  'Person staff has not been added')

    def test_add_person_fellow(self):
        Amity.create_room('NARNIA', 'O')
        previous_fellow_count = len(Amity.fellows)
        self.assertFalse('STEVE KANYI' in Amity.all_people)
        Amity.add_person('steve', 'kanyi', 'F')
        self.assertTrue('STEVE KANYI' in Amity.all_people)
        current_fellow_count = len(Amity.fellows)
        self.assertEqual(previous_fellow_count + 1, current_fellow_count, 'Person fellow has not been added')

    def test_return_random_office_room(self):
        Amity.create_room('Carmel', 'O')
        Amity.create_room('Narnia', 'O')
        random_office = Amity.generate_random_office()
        self.assertIn(random_office, Amity.office_rooms)


    def test_return_random_ls_room(self):
        Amity.create_room('PHP', 'L')
        Amity.create_room('Go', 'L')
        random_ls = Amity.generate_random_living_space()
        self.assertIn(random_ls, Amity.ls_rooms)

    def test_reallocate_person(self):
        Amity.create_room('PHP', 'l')
        Amity.create_room('NARNIA', 'O')
        Amity.add_person('steve', 'kanyi', 'F', 'Y')
        self.assertIn('STEVE KANYI', Amity.ls_rooms['PHP'])
        Amity.create_room('GO', 'l')
        Amity.reallocate_person_to_ls('steve kanyi', 'GO')
        self.assertIn('STEVE KANYI', Amity.ls_rooms['GO'])
        self.assertNotIn('STEVE KANYI', Amity.ls_rooms['PHP'])

    def test_does_not_reallocate_to_a_full_ls_room(self):
        Amity.create_room('PHP', 'L')
        Amity.create_room('NARNIA', 'O')
        previous_count = len(Amity.ls_rooms['PHP'])
        Amity.add_person('steve', 'kanyi', 'F', 'Y')
        Amity.add_person('Angie', 'Mugo', 'F', 'Y')
        Amity.add_person('Percila', 'Njira', 'F', 'Y')
        Amity.add_person('David', 'Chironde', 'F', 'Y')
        current_count = len(Amity.ls_rooms['PHP'])
        self.assertEqual(previous_count + 4, current_count)
        Amity.create_room('GO', 'L')
        Amity.add_person('Clement', 'Mwendwa', 'F', 'Y')
        response = Amity.reallocate_person_to_ls('Clement Mwendwa', 'PHP')
        self.assertEqual(response, 'PHP is already full')

    def test_does_reallocate_to_same_ls_room(self):
        Amity.create_room('PHP', 'L')
        Amity.create_room('NARNIA', 'O')
        Amity.add_person('Steve', 'Kanyi', 'F', 'Y')
        response = Amity.reallocate_person_to_ls('Steve Kanyi', 'PHP')
        self.assertEqual(response, 'STEVE KANYI is already allocated to PHP')

    def test_does_not_reallocate_to_a_full_office_room(self):
        Amity.create_room('Narnia', 'O')
        previous_count = len(Amity.office_rooms['NARNIA'])
        Amity.add_person('steve', 'kanyi', 'F')
        Amity.add_person('Angie', 'Mugo', 'F')
        Amity.add_person('Percila', 'Njira', 'S')
        Amity.add_person('David', 'Chironde', 'F')
        Amity.add_person('Paul', 'Kahohi', 'S')
        Amity.add_person('Josh', 'Mwaniki', 'S')
        current_count = len(Amity.office_rooms['NARNIA'])
        self.assertEqual(previous_count + 6, current_count)
        Amity.create_room('Carmel', 'O')
        Amity.add_person('Clement', 'Mwendwa', 'F')
        response = Amity.reallocate_person_to_office('Clement Mwendwa', 'NARNIA')
        self.assertEqual(response, 'NARNIA is already full')

    def test_does_reallocate_to_same_office_room(self):
        Amity.create_room('NARNIA', 'O')
        Amity.add_person('Steve', 'Kanyi', 'F')
        response = Amity.reallocate_person_to_office('Steve Kanyi', 'NARNIA')
        self.assertEqual(response, 'STEVE KANYI is already allocated to NARNIA')



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
