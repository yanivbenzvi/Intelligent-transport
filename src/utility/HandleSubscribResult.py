from src.modules.Lanes import Lane
from src.utility import Store


class HandleSubscribeResult:

    @staticmethod
    def lanes_result_handler(subscribed_result: dict, store: Store, interval_size, ):
        for lane_id in subscribed_result.keys():
            lane = store.get_object_by_id('lane', lane_id)
            # lane.update_attribute(subscribed_result[lane_id], , )

    @staticmethod
    def get_subscribed_result(traci):
        HandleSubscribeResult.lanes_result_handler(traci.lane.getAllSubscriptionResults())
        # print(traci.simulation.getCurrentTime(), traci.lane.getAllSubscriptionResults())
        # print(traci.vehicle.getAllSubscriptionResults())
        # print("Time: ", self.get_real_time(traci.simulation.getTime()), "Lane Id: ", traci.lane.getAllSubscriptionResults())
