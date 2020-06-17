import unittest
from unittest import TestCase

from Code.JsonChecker import JsonChecker


class TestJsonChecker(TestCase):
    def setUp(self) -> None:
        #tempratuur testen
        self.readeersteFile_temp = JsonChecker(bacteriaName="xx", temperature=10, pH=10, item="temp", inputWaarde=10)
        self.readeersteFile_temp_O2 = JsonChecker(bacteriaName="xx", temperature=4, pH=10, item="temp", inputWaarde=4)
        self.readeersteFile_temp_O3 = JsonChecker(bacteriaName="xx", temperature=37, pH=10, item="temp", inputWaarde=37)
        self.readeersteFile_temp_O4 = JsonChecker(bacteriaName="xx", temperature=45, pH=10, item="temp", inputWaarde=45)
        self.readeersteFile_temp_O5= JsonChecker(bacteriaName="xx", temperature=50, pH=10, item="temp", inputWaarde=50)

        self.readeersteFile_temp1 = self.readeersteFile_temp.read_json()
        self.readeersteFile_temp_2 = self.readeersteFile_temp.values_check()
        self.readeersteFile_temp_O2_1 = self.readeersteFile_temp_O2.values_check()
        self.readeersteFile_temp_O3_1 = self.readeersteFile_temp_O3.values_check()
        self.readeersteFile_temp_O4_1 = self.readeersteFile_temp_O4.values_check()
        self.readeersteFile_temp_O5_1 = self.readeersteFile_temp_O5.values_check()

        #ph testen
        self.readeersteFile_pH= JsonChecker(bacteriaName="xx", temperature=10, pH=10, item="ph", inputWaarde=10)
        self.readeersteFile_pH_O2= JsonChecker(bacteriaName="xx", temperature=10, pH=3.5, item="ph", inputWaarde=3.5)
        self.readeersteFile_pH_O3= JsonChecker(bacteriaName="xx", temperature=10, pH=5, item="ph", inputWaarde=5)
        self.readeersteFile_pH_O4= JsonChecker(bacteriaName="xx", temperature=10, pH=4.5, item="ph", inputWaarde=4.5)
        self.readeersteFile_pH_O5= JsonChecker(bacteriaName="xx", temperature=10, pH=20, item="ph", inputWaarde=20)


        self.readeersteFile_pH1= self.readeersteFile_pH.read_json()
        self.readeersteFile_pH2= self.readeersteFile_pH.values_check()
        self.readeersteFile_pH_O2_1= self.readeersteFile_pH_O2.values_check()
        self.readeersteFile_pH_O3_1 = self.readeersteFile_pH_O3.values_check()
        self.readeersteFile_pH_O4_1 = self.readeersteFile_pH_O4.values_check()
        self.readeersteFile_pH_O5_1 = self.readeersteFile_pH_O5.values_check()

        #aw_testen
        self.readeersteFile_aw= JsonChecker(bacteriaName="xx", temperature=10, pH=10, item="aw", inputWaarde=10)
        self.readeersteFile_aw_1 = self.readeersteFile_aw.read_json()

    def tearDown(self) -> None:
        self.readeersteFile_temp1 = None
        self.readeersteFile_temp_2 = None
        self.readeersteFile_temp_O2_1 = None

        self.readeersteFile_pH1 = None
        self.readeersteFile_pH2 = None
        self.readeersteFile_pH_O2_1 = None

    def test_read_json(self):
        # temp lezen
        self.assertEqual(self.readeersteFile_temp1, [6.0, 37.0, 45.0])
        # ph lezen
        self.assertEqual(self.readeersteFile_pH1, [4.0, 5.0, 10.0])
        #aw lezen
        self.assertEqual(self.readeersteFile_aw_1, ["bestaat ffetje niet"])

    def test_value_check(self):
        #temp check
        # temp is grooter dan de min en kleiner dan de optimum
        self.assertEqual(self.readeersteFile_temp_2, [10.0, 37, 45.0])
        # temp is kleiner dan de min
        self.assertRaises(Exception, self.readeersteFile_temp_O2_1)
        # temp is gelijk aan de optimum
        self.assertEqual(self.readeersteFile_temp_O3_1, [37.0, 45.0])
        # tep is gelijk aan de max
        self.assertEqual(self.readeersteFile_temp_O4_1, [45.0])
        # temp is grooter dan de max
        self.assertRaises(Exception,self.readeersteFile_temp_O5_1)

        # ph check
        # ph is gelijk aan de max
        self.assertEqual(self.readeersteFile_pH2, [10.0])
        # ph is kleiner dan de min
        self.assertRaises(Exception, self.readeersteFile_pH_O2_1)
        # ph is gelijk aan de optimum
        self.assertEqual(self.readeersteFile_pH_O3_1,[5.0, 10.0])
        # ph is kleiner dan de optimum en groter dan de min
        self.assertEqual(self.readeersteFile_pH_O4_1,[4.5,5.0, 10.0])
        # ph is grooter dan de max
        self.assertEqual(self.readeersteFile_pH_O5_1, [0.0])


if __name__ == '__main__':
    unittest.main()