import unittest
from src.modules.Scenario import Scenario


class ScenarioCase(unittest.TestCase):
    def test_get_num_of_cells(self):
        # Assume
        start_time = 4.1
        end_time = 14.6
        duration = end_time - start_time
        interval_time = 2
        result = Scenario.get_num_of_cells(duration, interval_time)
        self.assertEqual(result, 11)


if __name__ == '__main__':
    unittest.main()
