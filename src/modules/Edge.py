import traci.constants as tc
from traci._lane import _readLinks
from traci.domain import Domain
from traci.storage import Storage


class Edge:
    # from \\scenario\\in\\most.net.xml
    def __init__(self, edge_id, edge_from, edge_to, lane_list, priority=None, edge_type=None, shape=None):
        """
        :param edge_id:   unique name - String example - "153459#0"
        :param edge_from: unique from edge - String example - "141010"
        :param edge_to:   unique to edge - String example - "141010"
        :param lane_id:   unique name lane id - String example - "153459#0_0"
        :param priority:  priority - String example - "9", default = None
        :param edge_type: road type - String example - "highway.primary", default = None
        :param shape:     edge shape - String, default = None
        """
        self.edge_id = edge_id
        self.edge_from = edge_from
        self.edge_to = edge_to
        self.priority = priority
        self.relatively_junction_priority = None
        self.edge_type = edge_type
        self.shape = shape
        self.lane_list = lane_list


def getWaitingTime(self, edgeID):
    """getWaitingTime() -> double
    Returns the sum of the waiting time of all vehicles currently on
    that edge (see traci.vehicle.getWaitingTime).
    """
    return self._getUniversal(tc.VAR_WAITING_TIME, edgeID)


def getCO2Emission(self, edgeID):
    """getCO2Emission(string) -> double
    Returns the CO2 emission in mg for the last time step on the given edge.
    """
    return self._getUniversal(tc.VAR_CO2EMISSION, edgeID)


def getCOEmission(self, edgeID):
    """getCOEmission(string) -> double
    Returns the CO emission in mg for the last time step on the given edge.
    """
    return self._getUniversal(tc.VAR_COEMISSION, edgeID)


def getHCEmission(self, edgeID):
    """getHCEmission(string) -> double
    Returns the HC emission in mg for the last time step on the given edge.
    """
    return self._getUniversal(tc.VAR_HCEMISSION, edgeID)


def getPMxEmission(self, edgeID):
    """getPMxEmission(string) -> double
    Returns the particular matter emission in mg for the last time step on the given edge.
    """
    return self._getUniversal(tc.VAR_PMXEMISSION, edgeID)


def getNOxEmission(self, edgeID):
    """getNOxEmission(string) -> double
    Returns the NOx emission in mg for the last time step on the given edge.
    """
    return self._getUniversal(tc.VAR_NOXEMISSION, edgeID)


def getFuelConsumption(self, edgeID):
    """getFuelConsumption(string) -> double
    Returns the fuel consumption in ml for the last time step on the given edge.
    """
    return self._getUniversal(tc.VAR_FUELCONSUMPTION, edgeID)


def getNoiseEmission(self, edgeID):
    """getNoiseEmission(string) -> double
    Returns the noise emission in db for the last time step on the given edge.
    """
    return self._getUniversal(tc.VAR_NOISEEMISSION, edgeID)


def getElectricityConsumption(self, edgeID):
    """getElectricityConsumption(string) -> double
    Returns the electricity consumption in ml for the last time step.
    """
    return self._getUniversal(tc.VAR_ELECTRICITYCONSUMPTION, edgeID)


def getLastStepMeanSpeed(self, edgeID):
    """getLastStepMeanSpeed(string) -> double
    Returns the average speed in m/s for the last time step on the given edge.
    """
    return self._getUniversal(tc.LAST_STEP_MEAN_SPEED, edgeID)


def getLastStepOccupancy(self, edgeID):
    """getLastStepOccupancy(string) -> double
    Returns the net occupancy (excluding inter-vehicle gaps) in % for the last time step on the given edge.
    """
    return self._getUniversal(tc.LAST_STEP_OCCUPANCY, edgeID)


def getLastStepLength(self, edgeID):
    """getLastStepLength(string) -> double
    Returns the mean vehicle length in m for the last time step on the given edge.
    """
    return self._getUniversal(tc.LAST_STEP_LENGTH, edgeID)


def getLaneNumber(self, edgeID):
    """getLaneNumber(string) -> int
    Returns the number of lanes of this edge
    """
    return self._getUniversal(tc.VAR_LANE_INDEX, edgeID)


def getStreetName(self, edgeID):
    """getStreetName(string) -> string
    Returns the street name of this edge
    """
    return self._getUniversal(tc.VAR_NAME, edgeID)


def getTraveltime(self, edgeID):
    """getTraveltime(string) -> double
    Returns the estimated travel time in s for the last time step on the given edge.
    """
    return self._getUniversal(tc.VAR_CURRENT_TRAVELTIME, edgeID)


def getLastStepVehicleNumber(self, edgeID):
    """getLastStepVehicleNumber(string) -> integer
    Returns the total number of vehicles for the last time step on the given edge.
    """
    return self._getUniversal(tc.LAST_STEP_VEHICLE_NUMBER, edgeID)


def getLastStepHaltingNumber(self, edgeID):
    """getLastStepHaltingNumber(string) -> integer
    Returns the total number of halting vehicles for the last time step on the given edge.
    A speed of less than 0.1 m/s is considered a halt.
    """
    return self._getUniversal(tc.LAST_STEP_VEHICLE_HALTING_NUMBER, edgeID)


def getLastStepVehicleIDs(self, edgeID):
    """getLastStepVehicleIDs(string) -> list(string)
    Returns the ids of the vehicles for the last time step on the given edge.
    """
    return self._getUniversal(tc.LAST_STEP_VEHICLE_ID_LIST, edgeID)


def getLastStepPersonIDs(self, edgeID):
    """getLastStepPersonIDs(string) -> list(string)
    Returns the ids of the persons on the given edge during the last time step.
    """
    return self._getUniversal(tc.LAST_STEP_PERSON_ID_LIST, edgeID)
