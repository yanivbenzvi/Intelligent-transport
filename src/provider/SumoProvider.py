from src.provider.SumoInstanceProvider import SumoInstanceProvider
from src.utility.HandleSubscribResult import HandleSubscribeResult
from src.utility.ScenarioTimeCalculation import ScenarioTimeCalculation
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

        # import all nessacceary object from the simulator
        instance_provider = SumoInstanceProvider(Configuration.scenario_object)

        # create store of all instances
        self.store = Store(instance_provider.boot().all_instance)

        # make traci to be global
        Configuration.scenario_object.traci = self.traci

        # start the sumo simulation program
        self.traci.start(Configuration.sumoCmd())

        self.time_utility = ScenarioTimeCalculation(Configuration.scenario_object)

        # subscribe all relevant instance for future update
        SubscribeInstance(self.traci).subscribes_all_instance(self.store)

        # calculate time
        self.initialization_scenario_time_ara()

        while self.traci.simulation.getMinExpectedNumber() > 0:
            try:
                self.traci.simulationStep()
            except self.traci.exceptions.FatalTraCIError as inst:
                print(inst)
                exit(0)

            # update instance by subscribe result
            # HandleSubscribeResult.get_subscribed_result(self.traci,self.time_utility.)

            time.sleep(self.simulator_delay)
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

    def get_real_time(self, time):
        hours = int(time)
        hours = time / 3600
        minutes = (hours * 60) % 60
        seconds = (minutes * 60) % 60
        tuple_date = (round(hours), round(minutes), round(seconds))
        return tuple_date

    def initialization_scenario_time_ara(self):
        pass

