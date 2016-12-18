import unittest
from unittest import TestCase
from app.amity import Amity
import unittest.mock as mock

class TestAmity(TestCase):


    def test_room_does_not_exist(self):
        Amity.create_room('Oculus', 'O')
        self.assertTrue('OCULUS' in Amity.all_rooms)
        response = Amity.create_room('OCULUS', 'O')
        self.assertEqual(response, "Room already exists")

    def test_create_room(self):
        previous_room_count = len(Amity.all_rooms)
        self.assertFalse('Oculus' in Amity.all_rooms)
        Amity.create_room('Oculus', 'O')
        self.assertTrue('Oculus'.upper() in Amity.all_rooms)
        new_room_count = len(Amity.all_rooms)
        self.assertEqual(previous_room_count + 1, new_room_count)

    def test_add_person_staff(self):
        previous_staff_count = len(Amity.staffs)
        self.assertFalse(2 in Amity.all_people)
        Amity.add_person(2, 'steve', 'kanyi', 'S', 'N')
        self.assertTrue(2 in Amity.all_people)
        current_staff_count = len(Amity.staffs)
        self.assertEqual(previous_staff_count + 1, current_staff_count,  'Person staff has not been added')

    def test_add_person_fellow(self):
        previous_fellow_count = len(Amity.fellows)
        self.assertFalse(1 in Amity.all_people)
        Amity.add_person(1, 'steve', 'kanyi', 'F', 'Y')
        self.assertTrue(1 in Amity.all_people)
        current_fellow_count = len(Amity.fellows)
        self.assertEqual(previous_fellow_count + 1, current_fellow_count, 'Person fellow has not been added')

    def test_generate_random_office_from_office_rooms(self):
        random_office = Amity.generate_random_office()
        self.assertTrue(random_office in Amity.office_rooms)

    def test_generate_random_living_space_from_ls_rooms(self):
        random_ls = Amity.generate_random_living_space()
        self.assertTrue(random_ls in Amity.ls_rooms)

    def test_reallocate_person(self):
        Amity.create_room('PHP', 'l')
        self.assertIn('PHP', Amity.all_rooms)
        Amity.add_person(1, 'steve', 'kanyi', 'F')
        self.assertNotIn('steve kanyi', Amity.ls_rooms['PHP'])
        Amity.reallocate_person_from_ls('steve kanyi', 'PHP')
        self.assertIn('steve kanyi', Amity.ls_rooms['PHP'])

    @mock.patch('app.amity.open')
    def test_load_people_calls_open_function(self, mock_open):
        Amity.load_people('data/people.txt')
        mock_open.assert_called_with('data/people.txt')

    def test_load_people_read_lines(self):
        with mock.patch.object(Amity, 'add_person') as mock_method:
            Amity.load_people('data/people.txt')
        mock_method.assert_called_with(1, 'OLUWAFEMI', 'SULE', 'FELLOW', 'Y')
