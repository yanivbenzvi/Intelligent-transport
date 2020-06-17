from src.provider.SumoInstanceProvider import SumoInstanceProvider


class Store:
    def __init__(self, store_object):
        self.objects = store_object

    def get_all_instances_by_name(self, instance_name):
        if self.is_instance_name_exit(instance_name):
            return None
        return self.objects[instance_name]

    def get_object_by_id(self, instance_name, instance_id):
        if self.is_instance_name_exit(instance_name) or self.is_instance_id_exit(instance_name, instance_id):
            return None
        return self.objects[instance_name][instance_id]

    def is_instance_name_exit(self, instance_name):
        return instance_name not in self.objects

    def is_instance_id_exit(self, instance_name, instance_id):
        return instance_id not in self.objects[instance_name]


if __name__ == "__main__":
    from src.modules.Scenario import Scenario

    scenario = Scenario(name="Monacor Scenario", download_url="",
                        dest_folder="MoSTScenario-0.6", conf_path="scenario", conf_file_name="most.sumocfg",
                        net_xml_path="scenario\\in\\",
                        vehicle_xml_path="scenario\\in\\route\\",
                        net_xml_file="most.net.xml",
                        vehicle_xml_file="most.pedestrian.rou.xml")
    instance_provider = SumoInstanceProvider(scenario)

    import time
    import datetime

    start_time = datetime.datetime.now()
    instance_provider.boot()
    calc_time = datetime.datetime.now() - start_time
    print("--- %s seconds ---" % calc_time)
    print("--- store action ---")

    start_time = datetime.datetime.now()
    store = Store(instance_provider.all_instance)
    print(store.get_object_by_id(instance_name='junction', instance_id='143517'))
    print(store.get_object_by_id(instance_name='lane', instance_id='152174#0_1'))
    print(len(store.get_all_instances_by_name(instance_name='lane')))

    calc_time = datetime.datetime.now() - start_time
    print("--- %s microseconds ---" % calc_time.microseconds)
