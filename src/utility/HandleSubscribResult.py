from src.utility import Store
from src.utility.XmlToDict import save2json


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

    @staticmethod
    def handleResults(store: Store):
        lanes = store.get_all_instances_by_name('lane')
        saving_result = dict()
        for lane_id in lanes.keys():
            lane_s = {
                lane_id: lanes[lane_id].occupancy
            }
            saving_result = {**saving_result, **lane_s}
        save2json(saving_result, "lanes_results", path="logs/")
