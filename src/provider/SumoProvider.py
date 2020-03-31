import os
import sys
import traci
import time
import traci.constants as tc
from src import Configuration


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

        traci.start(Configuration.sumoCmd)

        for step in range(self.number_of_iteration):
            print(traci.lane.subscribe("152810#2_1",(tc.va), begin=0.0, end=9999999999.9))
            traci.simulationStep()
            time.sleep(self.simulator_delay)
            # print(step)

        traci.close()
