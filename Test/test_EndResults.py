import unittest

from Code.EndResults import EndResults
from Code.JsonChecker import JsonChecker


class TestEndResults(unittest.TestCase):
    def setUp(self) -> None:
        # test voor logsitc
        self.object = EndResults.logistic(self, bact_name="xx", time=3, pH=9, temperature=10)

        # test log growth
        self.object2 = EndResults.log_growth(self, bact_name="xx", time=3, pH=9, temperature=10)

        # test temp groeifactor
        self.temp_check = JsonChecker(bacteria_name="xx", temperature=10, pH=7, item="temp", inputWaarde=10)
        self.temp_check_terug = self.temp_check.values_check()
        self.object3 = EndResults.temp_growth_factor(self, bact_name="xx", pH=8, end_time=4, temp_check=
        self.temp_check_terug)

        # test logistic curve
        self.object6 = EndResults.logstic_curve(self, bact_name="xx", time=3, pH=6, temperature=37)

        # test voor logsitc via de klasse
        self.object4 = EndResults(bact_naam="s-aureus", temp_input=10, ph_input=7, aw = 0.85, end_time=3, type_graph=1)
        # test logistic curve via de klasse
        self.object5 = EndResults(bact_naam="s-aureus", temp_input=20, ph_input=6, aw = 0.85,end_time=3, type_graph=2)
        # test temp groeifactor via de klasse
        self.object8 = EndResults(bact_naam="s-aureus", temp_input=37, ph_input=6,aw = 0.85, end_time=3, type_graph=4)

        # test met ongeldige inputs (temp, ph)
        self.dingen1 = EndResults(bact_naam="xx", temp_input=120, ph_input=0,aw = 0.85, end_time=3, type_graph=1)
        self.dingen2 = EndResults(bact_naam="xx", temp_input=10, ph_input=11, aw = 0.85,end_time=3, type_graph=2)
        self.dingen3 = EndResults(bact_naam="xx", temp_input=46.5, ph_input=-8,aw = 0.85, end_time=3, type_graph=3)
        self.dingen4 = EndResults(bact_naam="xx", temp_input=0, ph_input=0,aw = 0.85, end_time=3, type_graph=4)

        # test new growth rate
        self.ding = EndResults.new_growth_rate(self, bact_name="xx", pH=8, temperature=30)
        self.ding2 = EndResults.new_growth_rate(self, bact_name="xx", pH=8.9, temperature=40)
        self.ding3 = EndResults.new_growth_rate(self, bact_name="xx", pH=10, temperature=10)

        self.ding4 = EndResults.new_growth_rate(self, bact_name="s-aureus", pH=8, temperature=30)
        self.ding5 = EndResults.new_growth_rate(self, bact_name="s-aureus", pH=4.5, temperature=6)

    def tearDown(self) -> None:
        # zet alles terug naar None na het runnen van de test
        self.object = None
        self.object2 = None
        self.object3 = None
        self.object7 = None
        self.ding = None
        self.ding2 = None
        self.ding3 = None
        self.ding4 = None
        self.ding5 = None

        self.object4 = None
        self.object5 = None
        self.object6 = None
        self.object8 = None

        self.dingen1 = None
        self.dingen2 = None
        self.dingen3 = None
        self.dingen4 = None

    def test_new_growth_rate(self):
        self.assertNotEqual(self.ding, [])
        self.assertNotEqual(self.ding, None)
        self.assertEqual(self.ding, 0.12952267095269068)

        self.assertNotEqual(self.ding2, [])
        self.assertNotEqual(self.ding2, None)
        self.assertEqual(self.ding2, 0.08377588690778318)

        self.assertEqual(self.ding3, -0.0)

        self.assertEqual(self.ding4, 1.2922544811522854)
        self.assertEqual(self.ding5, 0.0)

    def test_log_growth(self):
        self.assertNotEqual(self.object2, [])
        self.assertNotEqual(self.object2, None)

        self.assertEqual(self.dingen3, None)

    def test_logistic(self):
        self.assertNotEqual(self.object, [])
        self.assertNotEqual(self.object, None)

        self.assertNotEqual(self.object4, [])
        self.assertEqual(self.dingen1, None)

    def test_logstic_curve(self):
        self.assertNotEqual(self.object6, [])
        self.assertNotEqual(self.object6, None)

        self.assertNotEqual(self.object5, [])

        self.assertEqual(self.dingen2, None)

    def test_temp_growth_factor(self):
        self.assertNotEqual(self.object3, [])
        self.assertNotEqual(self.object3, None)

        self.assertNotEqual(self.object8, [])

        self.assertEqual(self.dingen4, None)


if __name__ == '__main__':
    unittest.main()
