from src.utility.Store import Store
from src.utility.XmlToDict import load_json


class CollectDataAlgorithm:
    @staticmethod
    def get_all_junction_id(store: Store):
        junction_id_list = store.get_all_instances_by_name(instance_name='junction')
        return junction_id_list.keys()

    @staticmethod
    def update_weights_of_junction(store: Store):
        for junction_id in CollectDataAlgorithm.get_all_junction_id(store):
            CollectDataAlgorithm.update_weight_of_edge(store, junction_id)

    @staticmethod
    def update_weight_of_edge(store: Store, junction_id):
        edges = store.get_all_instances_by_name('edge')
        related_edge = list(filter(lambda edge: edge.edge_to == junction_id and
                                                len(edge.lane_list) > 0, edges.values()))
        print(related_edge)
        total_priority = list(map(lambda edge: int(edge.priority), related_edge))
        total_priority = sum(total_priority)

        for edge in related_edge:
            edge.relatively_junction_priority = int(edge.priority) / total_priority
            print("edge_id: ", edge.edge_id, "relatively_junction_priority", edge.relatively_junction_priority)

    @staticmethod
    def load_lane_occupancy_data(store: Store):
        occupancy_data = load_json("lanes_results.json")
        lanes_store = store.get_all_instances_by_name('lane')
        lanes_store_keys = store.get_all_instances_by_name('lane').keys()

        for lane_id in occupancy_data.keys():
            if lane_id in lanes_store_keys:
                lanes_store[lane_id].occupancy = occupancy_data[lane_id]



if __name__ == "__main__":
    from src.modules.Scenario import Scenario
    from src.provider.SumoInstanceProvider import SumoInstanceProvider
    from src.utility.Store import Store

    scenario = Scenario(name="Monacor Scenario", download_url="",
                        dest_folder="MoSTScenario-0.6", conf_path="scenario", conf_file_name="most.sumocfg",
                        net_xml_path="scenario\\in\\",
                        vehicle_xml_path="scenario\\in\\route\\",
                        net_xml_file="most.net.xml",
                        vehicle_xml_file="most.pedestrian.rou.xml")
    instance_provider = SumoInstanceProvider(scenario)
    instance_provider.boot()

    CollectDataAlgorithm.update_weights_of_junction(Store(instance_provider.all_instance))
