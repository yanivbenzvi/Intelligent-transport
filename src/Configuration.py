from src.utility import Path
from src.modules.Scenario import Scenario

production = False
sumoBinary = "sumo" if production else "sumo-gui"
project_folder_name = "smart-transport"
project_path = Path.get_project_home_path()
scenario_object = None
# sumoFolder = "C:\\Users\\Yaniv\\Desktop\\MoSTScenario\\scenario\\most.sumocfg"
sumoFolder = None

scenario_list = [
    Scenario(name="Monacor Scenario ver 06",
             download_url="https://github.com/lcodeca/MoSTScenario/archive/v0.6.zip",
             dest_folder="MoSTScenario-0.6", conf_path="scenario",
             conf_file_name="most.sumocfg", net_xml_path="/scenario/in/",
             vehicle_xml_path="/scenario/in/route/", net_xml_file="most.net.xml",
             vehicle_xml_file="most.pedestrian.rou.xml"),
    Scenario(name="Bologna small ver 0.29",
             download_url="https://liquidtelecom.dl.sourceforge.net/project/sumo/traffic_data/scenarios/Bologna_small/Bologna_small-0.29.0.zip",
             dest_folder="Bologna_small-0.29.0", conf_path="acosta", conf_file_name="run.sumo.cfg",
             net_xml_path="",
             vehicle_xml_path="", net_xml_file="",
             vehicle_xml_file=""),
    Scenario(name="Luxembourg ver 2.0", download_url="https://github.com/lcodeca/LuSTScenario/archive/v2.0.zip",
             dest_folder="LuSTScenario-2.0", conf_path="scenario", conf_file_name="due.actuated.sumocfg",
             net_xml_path="",
             vehicle_xml_path="", net_xml_file="",
             vehicle_xml_file=""),
    Scenario(name="Cologne Germany ver 0.32",
             download_url="https://liquidtelecom.dl.sourceforge.net/project/sumo/traffic_data/scenarios/TAPASCologne/TAPASCologne-0.32.0.7z",
             dest_folder="TAPASCologne-0.32.0", conf_path="", conf_file_name="cologne.sumocfg",
             net_xml_path="",
             vehicle_xml_path="", net_xml_file="",
             vehicle_xml_file="")
]


def tripInfoFile():
    if not scenario_object:
        import sys
        print("Error: cannot generate tripinfo path, there is no selected scenario object.")
        sys.exit(1)
    filename = scenario_object.name.lower().replace(" ", "_")
    from datetime import datetime
    date = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    full_path = "logs\\" + filename + "_date-" + date + "_tripinfo.trips.xml"
    return full_path


def sumoCmd(): return [sumoBinary, "-c", sumoFolder, "-S", "--tripinfo-output", tripInfoFile()]
