from src.modules.Lanes import Lane
from src.utility import Store


class HandleSubscribeResult:

    @staticmethod
    def lanes_result_handler(subscribed_result: dict, store: Store, num_of_interval, current_interval):
        for lane_id in subscribed_result.keys():
            lane = store.get_object_by_id('lane', lane_id)
            # print(subscribed_result[lane_id])
            lane.update_attribute(subscribed_result[lane_id], num_of_interval, current_interval)

    @staticmethod
    def get_subscribed_result(traci, store, num_of_interval, current_interval):
        HandleSubscribeResult.lanes_result_handler(traci.lane.getAllSubscriptionResults(), store, num_of_interval,
                                                   current_interval)
        # print(traci.simulation.getCurrentTime(), traci.lane.getAllSubscriptionResults())
        # print(traci.vehicle.getAllSubscriptionResults())
        # print("Time: ", self.get_real_time(traci.simulation.getTime()), "Lane Id: ", traci.lane.getAllSubscriptionResults())
