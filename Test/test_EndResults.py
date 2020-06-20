import unittest

from Code.EndResults import EndResults


class TestEndResults(unittest.TestCase):
    def setUp(self) -> None:
        # test voor logsitc
        self.object = EndResults(bact_naam="xx", temp_input=10, ph_input=10, end_time=3, type_graph=1)
        # test log growth
        self.object2 = EndResults(bact_naam="xx", temp_input=10, ph_input=5, end_time=3, type_graph=3)
        # test temp groeifactor
        self.object3 = EndResults(bact_naam="xx", temp_input=10, ph_input=4, end_time=3, type_graph=4)
        # test logistic curve
        self.object7 = EndResults(bact_naam="xx", temp_input=37, ph_input=6, end_time=3, type_graph=2)

        # test voor logsitc
        self.object4 = EndResults(bact_naam="s-aureus", temp_input=10, ph_input=7, end_time=3, type_graph=1)
        # test logistic curve
        self.object5 = EndResults(bact_naam="s-aureus", temp_input=20, ph_input=6, end_time=3, type_graph=2)
        # test log growth
        self.object6 = EndResults(bact_naam="s-aureus", temp_input=10, ph_input=10, end_time=3, type_graph=3)
        # test temp groeifactor
        self.object8 = EndResults(bact_naam="s-aureus", temp_input=37, ph_input=6, end_time=3, type_graph=4)

    def tearDown(self) -> None:
        # zet alles terug naar None na het runnen van de test
        self.object = None
        self.object2 = None
        self.object3 = None
        self.object7 = None

        self.object4 = None
        self.object5 = None
        self.object6 = None
        self.object8 = None

    def test_logistic(self):
        self.assertIsNot(self.object, False)
        self.assertNotEqual(self.object, None)
        self.assertEqual(self.object, [13.245915420825243, 14.336648569912533, 15.22112925224309, 15.91395460392643,
                                       3.333333333333333e+29,
                                       7.869860421615984e+29, 9.646631559719039e+29, 9.950669512572845e+29,
                                       13.245915420825243, 14.336648569912533,
                                       15.22112925224309, 15.91395460392643, 3.333333333333333e+29,
                                       7.869860421615984e+29, 9.646631559719039e+29,
                                       9.950669512572845e+29])

        self.assertNotEqual(self.object4, [])
        self.assertNotEqual(self.object4, None)

    def test_logstic_curve(self):
        self.assertIsNot(self.object7, False)
        self.assertNotEqual(self.object7, None)

        self.assertIsNot(self.object8, False)
        self.assertNotEqual(self.object8, None)

    def test_log_growth(self):
        self.assertIsNot(self.object2, False)
        self.assertNotEqual(self.object2, None)
        self.assertEqual(self.object2, [14.53335035111459, 14.53335035111459, 14.542993981011344, 14.5526376109081,
                                        14.562281240804854])
        self.assertNotEqual(self.object6, [])

    def test_temp_growth_factor(self):
        self.assertIsNot(self.object3, False)
        self.assertEqual(self.object3, [14.53335035, 14.53335035, 14.84321702, 15.15308368, 15.46295035, 15.77281702,
                                        16.08268368, 16.39255035, 16.70241702, 17.01228368, 17.32215035, 17.63201702,
                                        17.86344154, 17.86344154, 17.86344154, 17.86344154, 17.86344154, 17.,
                                        16., 15.])

        self.assertNotEqual(self.object5, None)
        self.assertEqual(self.object5, [1.45333504e+01, 1.45333504e+01, 1.45429940e+01, 1.45526376e+01,
                                        1.45622812e+01, 1.00000000e+15, 1.00000000e+15, 1.00000000e+15,
                                        1.00000000e+15, 1.00000000e+15, 1.40000000e+01])


if __name__ == '__main__':
    unittest.main()


