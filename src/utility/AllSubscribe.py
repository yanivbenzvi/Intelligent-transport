from src.modules.Lanes import Lane
import traci


class AllSubscribe:

    def __init__(self, traci_object: traci):
        """
        :param traci_object:traci
        """
        self.traci_object = traci_object

    def subscribes_all_instance(self, store):
        for lane in store.get_all_instances_by_name('lane'):
            print(lane)
        exit(0)
        self.traci_object.lane.subscribe("152174#0_1", AllSubscribe.prepare_argument("lane"))

    @staticmethod
    def prepare_argument(instance_type):
        if instance_type == "lane":
            return set(map(lambda arg: arg['hex'], Lane.subscribe_argument().values()))


if __name__ == "__main__":
    print(AllSubscribe.prepare_argument("lane"))
