import unittest
from src.utility.ParseXml import ParseXml
from src.Configuration import project_path

stub = None


def before_each():
    global stub
    stub = ParseXml("most.net.xml", project_path + "/tests/resources/").open_file()


class ParseXmlCase(unittest.TestCase):
    def test_get_elements1(self):
        before_each()
        result = stub.get_elements("edge")
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0], {'id': ':131241_0', 'function': 'internal'})

    def test_get_elements2(self):
        before_each()
        result = stub.get_elements("bla")
        self.assertEqual(len(result), 0)

    def test_is_open(self):
        stub = ParseXml("most.net.xml", project_path + "/tests/resources/")
        self.assertFalse(stub.is_open())
        stub.open_file()
        self.assertTrue(stub.is_open())


if __name__ == '__main__':
    unittest.main()
