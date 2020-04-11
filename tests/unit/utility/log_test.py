import unittest
from src.utility.Log import Log

class LogCase(unittest.TestCase):
    def test_something(self):
        Log.boot_log()
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
