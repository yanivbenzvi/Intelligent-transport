from src.utility.ScenarioTimeCalculation import ScenarioTimeCalculation
from src.utility.Store import Store
from src.utility.AlgorithmCalculation import AlgorithmCalculation
import traci as t


class HandleSimulationInterval:
    @staticmethod
    def checkIntervalPhase(traci: t, store: Store, utility_time: ScenarioTimeCalculation, current_time):
        if utility_time.is_the_next_interval_near(current_time, delta=0.5):
            print("<<updating tls to next interval>>")
            for junction_id in store.get_all_instances_by_name('junction').keys():
                HandleSimulationInterval.change_junction_tls_phase(traci, junction_id, store,
                                                                   utility_time.get_current_interval(current_time))

    @staticmethod
    def change_junction_tls_phase(traci: t, junction_id, store: Store, current_interval):
        edges = store.get_all_instances_by_name('edge')
        tls = traci.trafficlight.getCompleteRedYellowGreenDefinition(junction_id)[0]
        phases = tls.phases
        # print(traci.trafficlight.getCompleteRedYellowGreenDefinition("143517")[0].phases[0])

        related_edge = list(filter(lambda edge: edge.edge_to == junction_id and
                                                len(edge.lane_list) > 0, edges.values()))

        weight_list =[]
        lane_historical_array=[]
        for edge in related_edge:
            for lane in edge.lane_list:
                if not lane.occupancy:
                    continue
                lane_historical_array.append(lane.occupancy[current_interval])
                break
            weight_list.append(edge.relatively_junction_priority)

        for edge in related_edge:
            for lane in edge.lane_list:
                phase_index = HandleSimulationInterval.get_relative_phases_index(phases, lane.index)
                print(phase_index)
                phases = HandleSimulationInterval.update_tls_by_algorithm(phases, phase_index, weight_list, lane_historical_array)
        tls.phases = phases
        traci.trafficlight.setProgramLogic(junction_id, tls)

    @staticmethod
    def get_relative_phases_index(phases, lane_index):
        index_list = []
        for index in range(len(phases)):
            if phases[index].state[int(lane_index)] in ['g', 'G']:
                index_list.append(index)

        return index_list

    @staticmethod
    def update_tls_by_algorithm(phases, phase_index, lanes_weights, lane_historical_array):
        for index in phase_index:
            historical_data_value = AlgorithmCalculation.historical_data(lanes_weights, lane_historical_array)
            new_green_light_duration = AlgorithmCalculation.green_light_duration(historical_data_value)
            phases[index].duration = new_green_light_duration

        return phases
