import xmltodict
import pprint
import json
import os
from src.Configuration import project_path

with open(os.path.join(project_path, "simulator/MoSTScenario-0.6/scenario/in/most.net.xml")) as fd:
    doc = xmltodict.parse(fd.read())

pp = pprint.PrettyPrinter(indent=4)
j = json.dumps(doc, indent=4, sort_keys=True)
with open("data.json", 'w') as file:
    file.write(j)

print(doc['net']['tlLogic'])
