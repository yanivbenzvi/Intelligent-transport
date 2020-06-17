class Lane:
    # from \\scenario\\in\\most.net.xml
    def __init__(self, lane_id, index, speed, allow=None, disallow=None, length=None, width=None, shape=None):
        """
        :param lane_id: unique name - String example - "131316_w0"
        :param index:   number of road lanes start at 0 - String example "0"
        :param allow:   allow or not passageway - String example - "pedestrian"
        :param speed:   lane speed m/s String example - "1.00"
        :param length:  lane length meters String example - "5.10", default = None
        :param width:   lane width meters String example - "2.00", default = None
        :param shape:   lane shape - String, default = None
        """
        self.lane_id = lane_id
        self.index = index
        self.allow = allow
        self.disallow = disallow
        self.speed = speed
        self.length = length
        self.width = width
        self.shape = shape

    @staticmethod
    def subscribe_argument():
        return {
            "last_step_occupancy": {
                "hex": 0x13
            },

        }


def getLength(self, laneID):
    """getLength(string) -> double
    Returns the length in m.
    """
    return self._getUniversal(tc.VAR_LENGTH, laneID)


def getMaxSpeed(self, laneID):
    """getMaxSpeed(string) -> double
    Returns the maximum allowed speed on the lane in m/s.
    """
    return self._getUniversal(tc.VAR_MAXSPEED, laneID)


def getWidth(self, laneID):
    """getWidth(string) -> double
    Returns the width of the lane in m.
    """
    return self._getUniversal(tc.VAR_WIDTH, laneID)


def getAllowed(self, laneID):
    """getAllowed(string) -> list(string)
    Returns a list of allowed vehicle classes. An empty list means all vehicles are allowed.
    """
    return self._getUniversal(tc.LANE_ALLOWED, laneID)


def getDisallowed(self, laneID):
    """getDisallowed(string) -> list(string)
    Returns a list of disallowed vehicle classes.
    """
    return self._getUniversal(tc.LANE_DISALLOWED, laneID)


def getLinkNumber(self, laneID):
    """getLinkNumber(string) -> integer
    Returns the number of connections to successive lanes.
    """
    return self._getUniversal(tc.LANE_LINK_NUMBER, laneID)


def getLinks(self, laneID, extended=True):
    """getLinks(string) -> list((string, bool, bool, bool))
    A list containing id of successor lane together with priority, open and foe
    for each link.
    if extended=True, each result tuple contains
    (string approachedLane, bool hasPrio, bool isOpen, bool hasFoe,
    string approachedInternal, string state, string direction, float length)
    """
    complete_data = self._getUniversal(tc.LANE_LINKS, laneID)
    if extended:
        return complete_data
    else:
        # for downward compatibility
        return [tuple(d[:4]) for d in complete_data]


def getShape(self, laneID):
    """getShape(string) -> list((double, double))
    List of 2D positions (cartesian) describing the geometry.
    """
    return self._getUniversal(tc.VAR_SHAPE, laneID)


def getEdgeID(self, laneID):
    """getEdgeID(string) -> string
    Returns the id of the edge the lane belongs to.
    """
    return self._getUniversal(tc.LANE_EDGE_ID, laneID)


def getCO2Emission(self, laneID):
    """getCO2Emission(string) -> double
    Returns the CO2 emission in mg for the last time step on the given lane.
    """
    return self._getUniversal(tc.VAR_CO2EMISSION, laneID)


def getCOEmission(self, laneID):
    """getCOEmission(string) -> double
    Returns the CO emission in mg for the last time step on the given lane.
    """
    return self._getUniversal(tc.VAR_COEMISSION, laneID)


def getHCEmission(self, laneID):
    """getHCEmission(string) -> double
    Returns the HC emission in mg for the last time step on the given lane.
    """
    return self._getUniversal(tc.VAR_HCEMISSION, laneID)


def getPMxEmission(self, laneID):
    """getPMxEmission(string) -> double
    Returns the particular matter emission in mg for the last time step on the given lane.
    """
    return self._getUniversal(tc.VAR_PMXEMISSION, laneID)


def getNOxEmission(self, laneID):
    """getNOxEmission(string) -> double
    Returns the NOx emission in mg for the last time step on the given lane.
    """
    return self._getUniversal(tc.VAR_NOXEMISSION, laneID)


def getFuelConsumption(self, laneID):
    """getFuelConsumption(string) -> double
    Returns the fuel consumption in ml for the last time step on the given lane.
    """
    return self._getUniversal(tc.VAR_FUELCONSUMPTION, laneID)


def getNoiseEmission(self, laneID):
    """getNoiseEmission(string) -> double
    Returns the noise emission in db for the last time step on the given lane.
    """
    return self._getUniversal(tc.VAR_NOISEEMISSION, laneID)


def getElectricityConsumption(self, laneID):
    """getElectricityConsumption(string) -> double
    Returns the electricity consumption in ml for the last time step.
    """
    return self._getUniversal(tc.VAR_ELECTRICITYCONSUMPTION, laneID)


def getLastStepMeanSpeed(self, laneID):
    """getLastStepMeanSpeed(string) -> double
    Returns the average speed in m/s for the last time step on the given lane.
    """
    return self._getUniversal(tc.LAST_STEP_MEAN_SPEED, laneID)


def getLastStepOccupancy(self, laneID):
    """getLastStepOccupancy(string) -> double
    Returns the occupancy in % for the last time step on the given lane.
    """
    return self._getUniversal(tc.LAST_STEP_OCCUPANCY, laneID)


def getLastStepLength(self, laneID):
    """getLastStepLength(string) -> double
    Returns the mean vehicle length in m for the last time step on the given lane.
    """
    return self._getUniversal(tc.LAST_STEP_LENGTH, laneID)


def getWaitingTime(self, laneID):
    """getWaitingTime() -> double
    .
    """
    return self._getUniversal(tc.VAR_WAITING_TIME, laneID)


def getTraveltime(self, laneID):
    """getTraveltime(string) -> double
    Returns the estimated travel time in s for the last time step on the given lane.
    """
    return self._getUniversal(tc.VAR_CURRENT_TRAVELTIME, laneID)


def getLastStepVehicleNumber(self, laneID):
    """getLastStepVehicleNumber(string) -> integer
    Returns the total number of vehicles for the last time step on the given lane.
    """
    return self._getUniversal(tc.LAST_STEP_VEHICLE_NUMBER, laneID)


def getLastStepHaltingNumber(self, laneID):
    """getLastStepHaltingNumber(string) -> integer
    Returns the total number of halting vehicles for the last time step on the given lane.
    A speed of less than 0.1 m/s is considered a halt.
    """
    return self._getUniversal(tc.LAST_STEP_VEHICLE_HALTING_NUMBER, laneID)


def getLastStepVehicleIDs(self, laneID):
    """getLastStepVehicleIDs(string) -> list(string)
    Returns the ids of the vehicles for the last time step on the given lane.
    """
    return self._getUniversal(tc.LAST_STEP_VEHICLE_ID_LIST, laneID)


@staticmethod
def subscribe_args_list(self, lanId):
    return tc.LAST_STEP_VEHICLE_HALTING_NUMBER, lanId
