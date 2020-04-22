from src.modules.Lanes import Lane
from src.modules.Junction import Junction
from src.modules.Vehicle import Vehicle
from src.modules.Edge import Edge
from src.modules.Scenario import Scenario
from src.utility.ParseXml import ParseXml
from src.Configuration import *
from collections import deque


class SumoInstancedProvider:
    def __init__(self, scenario):
        self.scenario = scenario

    def boot(self):
        self.scenario.net_file_location

    @staticmethod
    def instance_list():
        return {
            'Lane': {
                'ctor': Lane,
                # 'param' : Lane.get_param_name
            },
            'Junction': {
                'ctor': Junction
            },
            'vehicle': {
                'ctor': Vehicle
            },
            'edge': {
                'ctor': Edge
            }
        }


if __name__ == "__main__":
    Scenario(name="Monacor Scenario", download_url="",
             dest_folder="MoSTScenario-0.6", conf_path="scenario", conf_file_name="most.sumocfg")
    lane_list = []

    xml_file = ParseXml("most.net.xml", project_path + "/tests/resources/").open_file()
    # xml_file = ParseXml(Scenario.get_xml_file, project_path + "/tests/resources/").open_file()

    lane_list = list(
        map(lambda arg: Lane(lane_id=arg['id'], index=arg['index'], speed=arg['speed'], length=arg['length']),
            xml_file.get_elements("lane")))

    print(len(lane_list))

    vehicle_xml_file = ParseXml("most.pedestrian.rou.xml",
                                project_path + "/simulator/MoSTScenario-0.6/scenario/in/route/").open_file()
    edge_list = deque(map(lambda arg: print(arg), vehicle_xml_file.get_elements("vehicle")))


    # edge_list = list(map(lambda arg: Vehicle( vehicle_type, v_id, lat_alignment, person_capacity=-1, tau=1, speed_dev=-1, lc_cooperative=0.0,
    #              key="", value="false", probability=-1, max_speed=-1, sigma=-1, gui_shape="passenger"),xml_file.get_elements("vehicle")))

    # xml_file = ParseXml("most.net.xml", project_path + "/simulator/MoSTScenario-0.6/scenario/in/").open_file()
    # lane_list = list(map(lambda arg: Lane(lane_id=arg['id'], index=arg['index'], speed=arg['speed'], length=arg['length']),xml_file.get_elements("lane")))
    # print(len(lane_list))
