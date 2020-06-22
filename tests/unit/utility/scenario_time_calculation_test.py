import unittest
from src.utility.ScenarioTimeCalculation import ScenarioTimeCalculation
from src.Configuration import scenario_list


class MyTestCase(unittest.TestCase):

    def test_get_current_interval(self):
        stub = ScenarioTimeCalculation(scenario=scenario_list[0], interval_length=2)
        result1 = stub.get_current_interval(14000)  # 4 -> expect 0
        result2 = stub.get_current_interval(21560) # 5 -> expect 0
        result3 = stub.get_current_interval(21600) # 6 o'clock -> expect 1
        result4 = stub.get_current_interval(21601) # 6 o'clock -> expect 1
        result5 = stub.get_current_interval(27000) # 7:30 o'clock -> expect 1
        result6 = stub.get_current_interval(29000) # 8:00 o'clock -> expect 2
        result7 = stub.get_current_interval(33000) # 9:10 o'clock -> expect 2
        result8 = stub.get_current_interval(45000) # 12:30 o'clock -> expect 4

        self.assertEqual(result1, 0)
        self.assertEqual(result2, 0)
        self.assertEqual(result3, 1)
        self.assertEqual(result4, 1)
        self.assertEqual(result5, 1)
        self.assertEqual(result6, 2)
        self.assertEqual(result7, 2)
        self.assertEqual(result8, 4)


if __name__ == '__main__':
    unittest.main()
