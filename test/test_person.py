import unittest
from unittest import TestCase
from app.person import *
import unittest.mock as mock

class TestPerson(TestCase):

    def test_position_is_fellow(self):
        fellow1 = Fellow(2, 'Angie', 'Mugo')
        self.assertEqual(fellow1.position.upper(), 'FELLOW', 'The position must be a fellow')

    def test_position_is_staff(self):
        staff1 = Staff(3, 'Joshua', 'Mwaniki')
        self.assertEqual(staff1.position.upper(), 'STAFF', 'The position must be a staff')
