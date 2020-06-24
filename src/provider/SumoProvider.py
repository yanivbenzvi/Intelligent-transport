from src.provider.SumoInstanceProvider import SumoInstanceProvider
from src.utility.HandleSimulationInterval import HandleSimulationInterval
from src.utility.HandleSubscribResult import HandleSubscribeResult
from src.utility.ScenarioTimeCalculation import ScenarioTimeCalculation
from src.utility.CollectDataAlgorithm import CollectDataAlgorithm
from src.utility.Store import Store
from src.utility.SubscribeInstance import SubscribeInstance
from src import Configuration
from collections import deque
import os
import sys
import traci
import time


class SumoProvider:
    def __init__(self):
        self.number_of_iteration = 300000
        self.simulator_delay = 0
        self.store = None
        self.traci = traci
        self.time_utility = None

    def boot(self):
        if 'SUMO_HOME' in os.environ:
            tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
            sys.path.append(tools)
        else:
            sys.exit("please declare environment variable 'SUMO_HOME'")

        # set simulator choice from the list of the scenario
        SumoProvider.prefer_simulation()

        # import all necessary object from the simulator
        instance_provider = SumoInstanceProvider(Configuration.scenario_object)

        # create store of all instances
        self.store = Store(instance_provider.boot().all_instance)

        # make traci to be global
        Configuration.scenario_object.traci = self.traci

        # start the sumo simulation program
        self.traci.start(Configuration.sumoCmd())

        self.time_utility = ScenarioTimeCalculation(Configuration.scenario_object, interval_length=2)
        print("duration of selected simulation: ", self.time_utility.scenario_duration())
        # subscribe all relevant instance for future update
        if not Configuration.algorithm_mode:
            SubscribeInstance(self.traci).subscribes_all_instance(self.store)
        # load relevant data for algorithm future running
        else:
            CollectDataAlgorithm.load_lane_occupancy_data(self.store)
            CollectDataAlgorithm.update_weights_of_junction(self.store)

        # for step in range(self.number_of_iteration):
        flag_change = False
        while self.traci.simulation.getMinExpectedNumber() > 0:
            try:
                self.traci.simulationStep()
            except self.traci.exceptions.FatalTraCIError as inst:
                print(inst)
                break

            # update instance by subscribe result
            current_time = self.traci.simulation.getTime()
            if not Configuration.algorithm_mode:
                HandleSubscribeResult.get_subscribed_result(self.traci, self.store,
                                                            self.time_utility.get_num_of_interval(),
                                                            self.time_utility.get_current_interval(current_time))
            else:
                HandleSimulationInterval.checkIntervalPhase(self.traci, self.store, self.time_utility, current_time)

            if self.simulator_delay > 0:
                time.sleep(self.simulator_delay)

        if not Configuration.algorithm_mode:
            HandleSubscribeResult.handleResults(self.store)
        self.traci.close()

    @staticmethod
    def prefer_simulation():
        Configuration.scenario_object = SumoProvider.select_simulation()
        Configuration.scenario_object.download_scenario()
        print(Configuration.scenario_object.path_to_scenario_conf())
        Configuration.sumoFolder = Configuration.scenario_object.path_to_scenario_conf()

    @staticmethod
    def select_simulation():
        if not Configuration.production:
            SumoProvider.print_scenario_menu(Configuration.scenario_list)
            while True:
                selected_choice_num = int(input("enter your choice: "))
                if selected_choice_num - 1 in range(0, len(Configuration.scenario_list)):
                    break
            return Configuration.scenario_list[selected_choice_num - 1]
        return Configuration.scenario_list[0]

    @staticmethod
    def print_scenario_menu(scenario_list):
        print("please select which scenario you want to run:")
        deque(map(lambda args: print("press ", args[0] + 1, " for scenario: ", args[1].name), enumerate(scenario_list)),
              maxlen=0)
