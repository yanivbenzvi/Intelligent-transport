from xml.etree import ElementTree
from src.Configuration import project_path


class ParseXml:
    def __init__(self, file_name, file_location):
        self.file_name = file_name
        self.file_location = file_location
        self.tree = None

    def is_open(self):
        return self.tree is not None

    def open_file(self):
        # print("parsing file: ", self.file_location + self.file_name)
        with open(self.file_location + self.file_name, 'rt') as f:
            self.tree = ElementTree.parse(f)
        return self

    def get_elements(self, element_name):
        return list(map(lambda neighbor: neighbor.attrib, self.tree.iter(element_name)))


if __name__ == "__main__":
    xml_file = ParseXml("most.net.xml", project_path + "/tests/resources/").open_file()

    print(xml_file.get_elements("edge"))
    print("\n")
    print(xml_file.get_elements("lane"))
    print(xml_file.get_elements("none_exist_element"))

