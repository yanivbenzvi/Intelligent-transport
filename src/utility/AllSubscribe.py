from src.modules.Lanes import Lane
import traci

class AllSubscribe:

    def __init__(self, traci_object: traci):
        """
        :param traci_object:traci
        """
        self.traci_sub = traci_object

    def subscribes_all_instance(self):
        self.traci_sub.lane.subscribe("152174#0_1", AllSubscribe.preper_argument("lane"))

    @staticmethod
    def prepare_argument(instance_type):
        if instance_type == "lane":
            return set(map(lambda arg: arg['hex'], Lane.subscribe_argument().values()))


if __name__ == "__main__":
    print(AllSubscribe.prepare_argument("lane"))
