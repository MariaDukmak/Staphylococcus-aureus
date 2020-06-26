from unittest import TestCase

from Code.CSV_reader import ReadIt


class Testreadit(TestCase):
    def setUp(self) -> None:
        # test met de goede path van een csv file
        self.testIt = ReadIt("C:/Users/marya/OneDrive/Bureaublad/xx-waardes.csv")
        self.pathread = self.testIt.readd("C:/Users/marya/OneDrive/Bureaublad/xx-waardes.csv")
        self.growth = self.testIt.bereken_growth_rate()
        self.cellen = self.testIt.bereken_maxcellen()

        # test met een path van een xlsx file (verkeerde file)
        self.testIt2 = ReadIt("C:/Users/marya/OneDrive/Bureaublad/xxx-waardes.xlsx")
        self.pathread2 = ReadIt.readd(self,"C:/Users/marya/OneDrive/Bureaublad/xxx-waardes.xlsx")
        self.growth2 = self.testIt2.bereken_growth_rate()
        self.cellen2 = self.testIt2.bereken_maxcellen()

    def tearDown(self) -> None:
        self.testIt = None
        self.pathread = None
        self.growth = None

        self.pathread2 =None
        self.growth2 = None
        self.cellen2 = None

    def test_readd(self):
        self.assertNotEqual(self.pathread, [])
        self.assertNotEqual(self.pathread, None)

        self.assertRaises(UnicodeDecodeError, )
        self.assertNotEqual(self.pathread2, [])

    def test_bereken_growthrate(self):
        self.assertEqual(self.growth, 0.15266666666666673)
        self.assertNotEqual(self.growth, None)
        self.assertNotEqual(self.growth, [])

        self.assertEqual(self.growth2, 0)

    def test_bereken_maxcellen(self):
        self.assertEqual(self.cellen, [15.0, 2.3199999999999985])
        self.assertNotEqual(self.cellen, None)
        self.assertNotEqual(self.cellen, [])

        self.assertEqual(self.cellen2, None)
