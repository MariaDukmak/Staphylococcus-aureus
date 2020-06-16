import unittest
from unittest import TestCase

from Code.JsonChecker import JsonChecker


class TestJsonChecker(TestCase):
    def setUp(self) -> None:
        bact = "xx"
        self.readeersteFile = JsonChecker(bacteriaName="xx", temperature=10, pH=10, item="temp", inputWaarde=10)
        self.readeersteFile2 = self.readeersteFile.read_json()


    def tearDown(self) -> None:

        self.readeersteFile = None
        self.readeersteFile2 = None

    def test_read_json(self):
        self.assertEqual(self.readeersteFile2, [6.0,37.0, 45.0])

    # def test_value_check(self):


if __name__ == '__main__':
    unittest.main()