import unittest
from urllib.error import HTTPError

from main import _requester
from src.iss import Iss
from src.api import Api
from src.service import to_float

"""Tests"""


class IssTests(unittest.TestCase):

    def test_requester_empty_args(self):
        with self.assertRaises(SystemExit):
            _requester()

    def test_runner_wrong_args(self):
        with self.assertRaises(SystemExit):
            _requester()

    def test_service_to_float_good(self):
        result = 2.0
        self.assertEqual(to_float(2), result)

    def test_service_to_float_bad(self):
        result = False
        self.assertEqual(to_float('not-a-number'), result)

    def test_can_instantiate_api(self):
        api = Api()

    def test_can_instantiate_iss(self):
        iss = Iss()

    def test_can_get_people(self):
        iss = Iss()
        result = True
        iss.get_people()
        self.assertEqual(iss.status, result)

    def test_can_get_location(self):
        iss = Iss()
        result = True
        iss.get_loc()
        self.assertEqual(iss.status, result)

    def test_can_get_pass_good_coords(self):
        iss = Iss()
        result = True
        args = [23, 19]
        iss.get_pass(args)
        self.assertEqual(iss.status, result)

    def test_can_get_pass_bad_coords(self):
        iss = Iss()
        args = [23, 'longitude']
        with self.assertRaises(HTTPError):
            iss.get_pass(args)


if __name__ == '__main__':
    unittest.main()
