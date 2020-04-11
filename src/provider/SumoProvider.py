import os
import sys
from collections import deque

import traci
import time
import traci.constants as tc
from src import Configuration
from src.modules.Scenario import Scenario


class SumoProvider:
    def __init__(self):
        self.number_of_iteration = 300000
        self.simulator_delay = 0

    def boot(self):
        if 'SUMO_HOME' in os.environ:
            tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
            sys.path.append(tools)
        else:
            sys.exit("please declare environment variable 'SUMO_HOME'")

        SumoProvider.prefer_simulation()
        print(Configuration.sumoCmd())
        traci.start(Configuration.sumoCmd())

        # traci.lane.subscribe("152810#2_1", (tc.VAR_LENGTH, tc.VAR_WIDTH,tc.VAR_WAITING_TIME))
        # traci.lane.subscribe("-152330#1_1", (tc.VAR_LENGTH, tc.VAR_WIDTH,tc.VAR_WAITING_TIME))
        # traci.lane.subscribeLeader(vehID="EXT", dist=0)
        for step in range(self.number_of_iteration):
            traci.simulationStep()
            # print(traci.lane.getAllSubscriptionResults())
            time.sleep(self.simulator_delay)
            # print(step)

        traci.close()

    @staticmethod
    def prefer_simulation():
        scenario_object = SumoProvider.select_simulation()
        scenario_object.download_scenario()
        print(scenario_object.path_to_scenario_conf())
        Configuration.sumoFolder = scenario_object.path_to_scenario_conf()

    @staticmethod
    def select_simulation():
        scenario_list = [
            Scenario(name="Monacor Scenario", download_url="https://github.com/lcodeca/MoSTScenario/archive/v0.6.zip",
                     dest_folder="MoSTScenario-0.6", conf_path="scenario", conf_file_name="most.sumocfg"),
        ]
        if not Configuration.production:
            SumoProvider.print_scenario_menu(scenario_list)
            while True:
                selected_choice_num = int(input("enter your choice: "))
                if selected_choice_num - 1 in range(0, len(scenario_list)):
                    break
            return scenario_list[selected_choice_num - 1]
        return scenario_list[0]

    @staticmethod
    def print_scenario_menu(scenario_list):
        print("please select which scenario you want to run:")
        deque(map(lambda args: print("press ", args[0] + 1, " for scenario: ", args[1].name), enumerate(scenario_list)),
              maxlen=0)
