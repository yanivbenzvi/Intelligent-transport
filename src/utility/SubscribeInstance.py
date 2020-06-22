from src.modules.Lanes import Lane
import traci


class SubscribeInstance:

    def __init__(self, traci_object: traci):
        """
        :param traci_object:traci
        """
        self.traci_object = traci_object

    def subscribes_all_instance(self, store):
        for lane_id in store.get_all_instances_by_name('lane').keys():
            self.traci_object.lane.subscribe(lane_id, SubscribeInstance.prepare_argument("lane"))

    @staticmethod
    def prepare_argument(instance_type):
        if instance_type == "lane":
            return set(map(lambda arg: arg['hex'], Lane.subscribe_argument().values()))


if __name__ == "__main__":
    print(SubscribeInstance.prepare_argument("lane"))
