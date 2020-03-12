import os
import sys
import traci
import time
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

        # print(traci.junction.getIDList())
        for step in range(self.number_of_iteration):
            traci.simulationStep()
            time.sleep(self.simulator_delay)
            print(step)

        traci.close()
