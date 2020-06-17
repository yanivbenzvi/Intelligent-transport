import xmltodict
import pprint
import json
from src.Configuration import project_path


def xml2dict(path):
    with open(path) as fd:
        doc = xmltodict.parse(fd.read())
    return doc


def save2json(doc, file_name):
    pp = pprint.PrettyPrinter(indent=4)
    j = json.dumps(doc, indent=4, sort_keys=True)
    with open("../../tests/resources/" + file_name + ".json", 'w') as file:
        file.write(j)


if __name__ == "__main__":
    import os

    docs = xml2dict(os.path.join(project_path, "simulator/MoSTScenario-0.6/scenario/in/most.net.xml"))
    print(docs['net']['tlLogic'])
