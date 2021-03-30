import unittest

from main import _requester


"""Tests"""


class IssTests(unittest.TestCase):

    def test_requester_empty_args(self):
        with self.assertRaises(SystemExit):
            _requester()

    def test_runner_wrong_args(self):
        with self.assertRaises(SystemExit):
            _requester()


if __name__ == '__main__':
    unittest.main()
