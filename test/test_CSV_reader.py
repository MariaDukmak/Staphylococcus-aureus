from unittest import TestCase

from Code.CSV_reader import readit


class Testreadit(TestCase):
    def setUp(self) -> None:
        self.testIt= readit("C:/Users/marya/OneDrive/Bureaublad/xx-waardes.csv")
        self.pathread = self.testIt.readd("C:/Users/marya/OneDrive/Bureaublad/xx-waardes.csv")
        self.growth = self.testIt.bereken_growthrate()
        self.cellen = self.testIt.bereken_maxcellen()

    def tearDown(self) -> None:
        self.testIt = None
        self.pathread = None
        self.growth = None

    def test_readd(self):
        self.assertNotEqual(self.pathread, [])
        self.assertNotEqual(self.pathread, None)

    def test_bereken_growthrate(self):
        self.assertEqual(self.growth, 0.370000000000001)
        self.assertNotEqual(self.growth, None)
        self.assertNotEqual(self.growth, [])

    def test_bereken_maxcellen(self):
        self.assertEqual(self.cellen, [15.0, 2.3199999999999985])
        self.assertNotEqual(self.cellen, None)
        self.assertNotEqual(self.cellen, [])
