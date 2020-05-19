from src.modules.Lanes import Lane
from src.modules.Junction import Junction
from src.modules.Vehicle import Vehicle
from src.modules.Edge import Edge
from src.utility.ParseXml import ParseXml
from src.Configuration import *


class SumoInstancedProvider:
    def __init__(self, scenario):
        self.scenario = scenario

    def boot(self):
        self.scenario.net_file_location

    @staticmethod
    def instance_list():
        return {
            'lane': {
                'ctor1': Lane,
                'ctor2': lambda arg: Lane(lane_id=arg['id'], index=arg['index'], speed=arg['speed'],
                                          length=arg['length'])
            },
            'vehicle': {
                'ctor1': Vehicle,
                'ctor2': lambda arg: Vehicle(v_id=arg['id'], v_type=arg['type'], depart=arg['depart'],
                                             departLane=arg['departLane'], arrivalPos=arg['arrivalPos'])
            },
            'junction': {
                'ctor': Junction,
                'ctor2': lambda arg: Junction(junction_id=arg['id'], junction_type=arg['type'],
                                              inc_lanes=arg['incLanes'],
                                              int_lanes=arg['incLanes'], x=None if 'x' not in arg else arg['x'],
                                              y=None if 'y' not in arg else arg['y'],
                                              z=None if 'z' not in arg else arg['z'])
            },
            'edge': {
                'ctor1': Edge,
                'ctor2': lambda arg: Edge(edge_id=arg['id'])
            },
            'tlLogic': {
                'ctor1': Edge,
                'ctor2': lambda arg: print(arg)
            }
        }

    def make_instance(self):
        instance_ctor_list = SumoInstancedProvider.instance_list()

        xml_net_file = ParseXml(self.scenario.net_xml_file, self.scenario.path_to_net_xml_file()).open_file()
        vehicle_xml_file = ParseXml(self.scenario.vehicle_xml_file,
                                    self.scenario.path_to_vehicle_xml_file()).open_file()

        instance_list = {}
        for instance_ctor in instance_ctor_list.keys():
            if instance_ctor is not 'vehicle':
                instance_list[instance_ctor] = {arg['id']: instance_ctor_list[instance_ctor]['ctor2'](arg) for arg in
                                                xml_net_file.get_elements(instance_ctor)}
            else:
                instance_list[instance_ctor] = {arg['id']: instance_ctor_list[instance_ctor]['ctor2'](arg) for arg in
                                                vehicle_xml_file.get_elements(instance_ctor)}

        return instance_list


if __name__ == "__main__":
    scenario = Scenario(name="Monacor Scenario", download_url="",
                        dest_folder="MoSTScenario-0.6", conf_path="scenario", conf_file_name="most.sumocfg",
                        net_xml_path="/scenario/in/",
                        vehicle_xml_path="/scenario/in/route/",
                        net_xml_file="most.net.xml",
                        vehicle_xml_file="most.pedestrian.rou.xml")
    instance_provider = SumoInstancedProvider(scenario)

    import time

    start_time = time.time()
    instance_list = instance_provider.make_instance()
    print("--- %s seconds ---" % (time.time() - start_time))

    instance_ctor_list = SumoInstancedProvider.instance_list()
    for instance_ctor in instance_ctor_list.keys():
        print(instance_ctor, ": ", len(instance_list[instance_ctor]))

    # print(instance_list['vehicle'])
    # instance_list = {
    #     'lane': {
    #         "152810#2_1": Lane(lane_id=arg['id'], index=arg['index'], speed=arg['speed'], length=arg['length']),
    #         "152810#2_1": Lane(lane_id=arg['id'], index=arg['index'], speed=arg['speed'], length=arg['length']),
    #         "152810#2_1": Lane(lane_id=arg['id'], index=arg['index'], speed=arg['speed'], length=arg['length']),
    #         "152810#2_1": Lane(lane_id=arg['id'], index=arg['index'], speed=arg['speed'], length=arg['length']),
    #         "152810#2_1": Lane(lane_id=arg['id'], index=arg['index'], speed=arg['speed'], length=arg['length']),
    #         "152810#2_1": Lane(lane_id=arg['id'], index=arg['index'], speed=arg['speed'], length=arg['length']),
    #         "152810#2_1": Lane(lane_id=arg['id'], index=arg['index'], speed=arg['speed'], length=arg['length']),
    #     }
    # }
