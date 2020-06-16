from unittest import TestCase

from Code.EndResults import EndResults


#TODO: Hier moeten alle testes beter!

class TestEndResults(TestCase):
    def setUp(self) -> None:
        self.object = EndResults("xx", 10, 10, 15, 1)

    def tearDown(self) -> None:
        self.object = None

    def test_log_growth(self):
        self.assertIsNot(self.object,False)

    def test_logistic(self):
        self.assertIsNot(self.object,False)

    def test_temp_logistic(self):
        self.assertIsNot(self.object, False)

