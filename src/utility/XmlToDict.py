import xmltodict
import pprint
import json
import os
from src.Configuration import project_path


def xml2dict(path):
    with open(os.path.join(project_path, path)) as fd:
        doc = xmltodict.parse(fd.read())
    return doc
    # pp = pprint.PrettyPrinter(indent=4)
    # j = json.dumps(doc, indent=4, sort_keys=True)
    # with open("../../tests/resources/data.json", 'w') as file:
    #     file.write(j


if __name__ == "__main__":
    docs = xml2dict("simulator/MoSTScenario-0.6/scenario/in/most.net.xml")
    print(docs['net']['tlLogic'])
