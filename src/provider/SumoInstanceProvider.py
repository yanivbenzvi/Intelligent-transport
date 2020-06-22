from src.modules.Lanes import Lane
from src.modules.Junction import Junction
from src.modules.Vehicle import Vehicle
from src.modules.Edge import Edge
from src.utility.ParseXml import ParseXml
from src.Configuration import *
from src.utility.XmlToDict import xml2dict, save2json


class SumoInstanceProvider:
    def __init__(self, scenario):
        self.scenario = scenario
        self.all_instance = None

    def boot(self):
        print("starting building simulator instance store")
        if not isinstance(self.scenario,Scenario):
            print("SumoInstancedProvider: There is no scenario obeject")
            exit(1)
        self.create_and_filter_all_instance()

    @staticmethod
    def instance_list():
        return {
            'tlLogic': {

            },
            'connection': {

            },
            'vehicle': {
                'ctor1': Vehicle,
                'ctor2': lambda arg: Vehicle(v_id=arg['id']),  # , v_type=arg['type'], depart=arg['depart'],
                # departLane=arg['departLane'], arrivalPos=arg['arrivalPos'])
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
                'ctor2': lambda arg: Edge(edge_id=arg['id']),
                'lane': {
                    'ctor1': Lane,
                    'ctor2': lambda arg: Lane(lane_id=arg['id'], index=arg['index'], speed=arg['speed'],
                                              length=arg['length'])
                },
            },
            'tlLogic': {
                'ctor1': Edge,
                'ctor2': lambda arg: print(arg)
            }
        }

    def create_instance_from_xml(self):
        instance_ctor_list = SumoInstanceProvider.instance_list()

        dict_net_file = xml2dict(self.scenario.path_to_net_xml_file())
        dict_vehicle_file = xml2dict(self.scenario.path_to_vehicle_xml_file())

        instance_list = {}
        for instance_ctor in instance_ctor_list.keys():
            if instance_ctor is not 'vehicle':
                instance_list[instance_ctor] = dict_net_file['net'][instance_ctor]
            else:
                instance_list[instance_ctor] = dict_vehicle_file['routes'][instance_ctor]
        return instance_list

    @staticmethod
    def junction_filter_non_traffic_light(instance):
        filtered_list = list(filter(lambda junction: junction['@type'] == 'traffic_light', instance['junction']))
        junction_filtered = {junction['@id']: SumoInstanceProvider.create_junction_object(junction) for junction in
                             filtered_list}

        return junction_filtered

    @staticmethod
    def create_junction_object(junction_dict):
        incLanes = list(filter(lambda lane: 'w' in lane or 'c' in lane, junction_dict['@incLanes'].split(' ')))
        intLanes = list(filter(lambda lane: 'w' in lane or 'c' in lane, junction_dict['@intLanes'].split(' ')))

        junction_object = Junction(junction_dict['@id'], incLanes, intLanes, request=junction_dict['request'])
        return junction_object

    @staticmethod
    def connection_filter(instance):
        filtered_list = list(filter(lambda connection: '@tl' in connection, instance['connection']))
        return filtered_list

    @staticmethod
    def get_all_inc_lanes(junctions):
        all_inc_lanes = list(map(lambda junction: junction.inc_lanes, junctions.values()))
        flatten = lambda l: [item for sublist in l for item in sublist]
        return flatten(all_inc_lanes)

    @staticmethod
    def edges_filter_non_traffic_light(edges, junctions_id_list):
        edges_filtered = list(filter(lambda edge: ('@to' in edge and edge['@to'] in junctions_id_list), edges))
        edges_filtered = {edges['@id']: SumoInstanceProvider.create_edge_object(edges) for edges in
                          edges_filtered}
        return edges_filtered

    @staticmethod
    def create_edge_object(edge_dict):
        def filter_lane_lam(lane):
            if ('@allow' in lane) and ('pedestrian' in lane['@allow'].split(' ')):
                return False
            return True

        if isinstance(edge_dict['lane'], dict):
            lanes_filtered = [edge_dict['lane']] if filter_lane_lam(edge_dict['lane']) else []
        else:
            lanes_filtered = list(filter(lambda lane: filter_lane_lam(lane), edge_dict['lane']))
        lane_object = list(map(lambda lane: Lane(lane['@id'], index=lane['@index'], length=lane['@length']
                                                 , speed=lane['@speed'],
                                                 allow=None if '@allow' not in lane else lane['@allow']), lanes_filtered))

        edge_object = Edge(edge_dict['@id'], edge_from=edge_dict['@from'], edge_to=edge_dict['@to'],
                           priority=None if '@priority' not in edge_dict else edge_dict['@priority'],
                           edge_type=edge_dict['@type'], lane_list=lane_object)
        return edge_object

    def collect_lane_from_edge(self):
        lane_collection = dict()
        for edge in self.all_instance['edge'].values():
            lane_collection = {**{lane.lane_id: lane for lane in edge.lane_list}, **lane_collection}
        return lane_collection

    def create_and_filter_all_instance(self):
        self.all_instance = self.create_instance_from_xml()

        # print("before filtering")
        # for ins in self.all_instance.keys():
        #     print(ins, " length: ", len(self.all_instance[ins]))

        self.all_instance['junction'] = SumoInstanceProvider.junction_filter_non_traffic_light(self.all_instance)
        all_inc_lanes = SumoInstanceProvider.get_all_inc_lanes(self.all_instance['junction'])

        self.all_instance['edge'] = SumoInstanceProvider. \
            edges_filter_non_traffic_light(self.all_instance['edge'], self.all_instance['junction'].keys())

        self.all_instance['lane'] = self.collect_lane_from_edge()

        self.all_instance['connection'] = SumoInstanceProvider.connection_filter(self.all_instance)

        # print("after filtering")
        for ins in self.all_instance.keys():
            print(ins, "size: ", len(self.all_instance[ins]))


if __name__ == "__main__":
    scenario = Scenario(name="Monacor Scenario", download_url="",
                        dest_folder="MoSTScenario-0.6", conf_path="scenario", conf_file_name="most.sumocfg",
                        net_xml_path="scenario\\in\\",
                        vehicle_xml_path="scenario\\in\\route\\",
                        net_xml_file="most.net.xml",
                        vehicle_xml_file="most.pedestrian.rou.xml")
    instance_provider = SumoInstanceProvider(scenario)

    import time

    start_time = time.time()

    instance_provider.boot()

    print("--- %s seconds ---" % (time.time() - start_time))
