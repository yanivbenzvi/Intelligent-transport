import traci.constants as tc
from traci.domain import Domain


class Vehicle:
    # from \\scenario\\in\\most.net.xml
    def __init__(self, v_id, v_type, depart, departLane, arrivalPos, edges):
        """
        :param v_id:       Unique name - String example - "pedestrian_3-1_3451_tr"
        :param v_type:     Vehicle type - String example - "passenger"
        :param depart:     Start flow - String example - "triggered"
        :param departLane: Depart type - String example  - "best"
        :param arrivalPos: Coordinates location arrive example - "22.89"
        :param edges:      list where visitor separated ' ' String example -"-153457 153452#1 153452#2 153451#1 153451#2 153451#3"
        """
        self.v_id = v_id
        self.v_type = v_type
        self.depart = depart
        self.departLane = departLane
        self.arrivalPos = arrivalPos
        self.edges = edges


def getSpeed(self, vehID):
    """getSpeed(string) -> double
    Returns the (longitudinal) speed in m/s of the named vehicle within the last step.
    """
    return self._getUniversal(tc.VAR_SPEED, vehID)


def getLateralSpeed(self, vehID):
    """getLateralSpeed(string) -> double
    Returns the lateral speed in m/s of the named vehicle within the last step.
    """
    return self._getUniversal(tc.VAR_SPEED_LAT, vehID)


def getAcceleration(self, vehID):
    """getAcceleration(string) -> double
    Returns the acceleration in m/s^2 of the named vehicle within the last step.
    """
    return self._getUniversal(tc.VAR_ACCELERATION, vehID)


def getSpeedWithoutTraCI(self, vehID):
    """getSpeedWithoutTraCI(string) -> double
    Returns the speed that the vehicle would drive if not speed-influencing
    command such as setSpeed or slowDown was given.
    """
    return self._getUniversal(tc.VAR_SPEED_WITHOUT_TRACI, vehID)


def getPosition(self, vehID):
    """getPosition(string) -> (double, double)
    Returns the position of the named vehicle within the last step [m,m].
    """
    return self._getUniversal(tc.VAR_POSITION, vehID)

def getAngle(self, vehID):
    """getAngle(string) -> double
    Returns the angle in degrees of the named vehicle within the last step.
    """
    return self._getUniversal(tc.VAR_ANGLE, vehID)

def getRoadID(self, vehID):
    """getRoadID(string) -> string
    Returns the id of the edge the named vehicle was at within the last step.
    """
    return self._getUniversal(tc.VAR_ROAD_ID, vehID)

def getLaneID(self, vehID):
    """getLaneID(string) -> string
    Returns the id of the lane the named vehicle was at within the last step.
    """
    return self._getUniversal(tc.VAR_LANE_ID, vehID)

def getLaneIndex(self, vehID):
    """getLaneIndex(string) -> integer
    Returns the index of the lane the named vehicle was at within the last step.
    """
    return self._getUniversal(tc.VAR_LANE_INDEX, vehID)

def getTypeID(self, vehID):
    """getTypeID(string) -> string
    Returns the id of the type of the named vehicle.
    """
    return self._getUniversal(tc.VAR_TYPE, vehID)

def getRouteID(self, vehID):
    """getRouteID(string) -> string
    Returns the id of the route of the named vehicle.
    """
    return self._getUniversal(tc.VAR_ROUTE_ID, vehID)

def getRouteIndex(self, vehID):
    """getRouteIndex(string) -> int
    Returns the index of the current edge within the vehicles route or -1 if the
    vehicle has not yet departed
    """
    return self._getUniversal(tc.VAR_ROUTE_INDEX, vehID)

def getRoute(self, vehID):
    """getRoute(string) -> list(string)
    Returns the ids of the edges the vehicle's route is made of.
    """
    return self._getUniversal(tc.VAR_EDGES, vehID)

def getLanePosition(self, vehID):
    """getLanePosition(string) -> double
    The position of the vehicle along the lane measured in m.
    """
    return self._getUniversal(tc.VAR_LANEPOSITION, vehID)

def getNoiseEmission(self, vehID):
    """getNoiseEmission(string) -> double
    Returns the noise emission in db for the last time step.
    """
    return self._getUniversal(tc.VAR_NOISEEMISSION, vehID)

def getPersonCapacity(self, vehID):
    """getPersonCapacity(string) -> int
    Returns the person capacity of the vehicle
    """
    return self._getUniversal(tc.VAR_PERSON_CAPACITY, vehID)

def getPersonNumber(self, vehID):
    """getPersonNumber(string) -> integer
    Returns the total number of persons which includes those defined
    using attribute 'personNumber' as well as <person>-objects which are riding in
    this vehicle.
    """
    return self._getUniversal(tc.VAR_PERSON_NUMBER, vehID)

def getPersonIDList(self, vehID):
    """getPersonIDList(string) -> integer
    Returns the list of persons which includes those defined using attribute 'personNumber'
    as well as <person>-objects which are riding in this vehicle.
    """
    return self._getUniversal(tc.LAST_STEP_PERSON_ID_LIST, vehID)

def getAdaptedTraveltime(self, vehID, time, edgeID):
    """getAdaptedTraveltime(string, double, string) -> double
    .
    """
    self._connection._beginMessage(tc.CMD_GET_VEHICLE_VARIABLE,
                                   tc.VAR_EDGE_TRAVELTIME, vehID, 1 + 4 + 1 + 8 + 1 + 4 + len(edgeID))
    self._connection._string += struct.pack(
        "!BiBd", tc.TYPE_COMPOUND, 2, tc.TYPE_DOUBLE, time)
    self._connection._packString(edgeID)
    return self._connection._checkResult(tc.CMD_GET_VEHICLE_VARIABLE, tc.VAR_EDGE_TRAVELTIME, vehID).readDouble()

def getEffort(self, vehID, time, edgeID):
    """getEffort(string, double, string) -> double
    .
    """
    self._connection._beginMessage(tc.CMD_GET_VEHICLE_VARIABLE,
                                   tc.VAR_EDGE_EFFORT, vehID, 1 + 4 + 1 + 8 + 1 + 4 + len(edgeID))
    self._connection._string += struct.pack(
        "!BiBd", tc.TYPE_COMPOUND, 2, tc.TYPE_DOUBLE, time)
    self._connection._packString(edgeID)
    return self._connection._checkResult(tc.CMD_GET_VEHICLE_VARIABLE, tc.VAR_EDGE_EFFORT, vehID).readDouble()


def getSignals(self, vehID):
    """getSignals(string) -> integer
    Returns an integer encoding the state of a vehicle's signals.
    """
    return self._getUniversal(tc.VAR_SIGNALS, vehID)

def getLength(self, vehID):
    """getLength(string) -> double
    Returns the length in m of the given vehicle.
    """
    return self._getUniversal(tc.VAR_LENGTH, vehID)

def getMaxSpeed(self, vehID):
    """getMaxSpeed(string) -> double
    Returns the maximum speed in m/s of this vehicle.
    """
    return self._getUniversal(tc.VAR_MAXSPEED, vehID)

def getLateralLanePosition(self, vehID):
    """getLateralLanePosition(string) -> double
    Returns The lateral position of the vehicle on its current lane measured in m.
    """
    return self._getUniversal(tc.VAR_LANEPOSITION_LAT, vehID)

def getMaxSpeedLat(self, vehID):
    """getMaxSpeedLat(string) -> double
    Returns the maximum lateral speed in m/s of this vehicle.
    """
    return self._getUniversal(tc.VAR_MAXSPEED_LAT, vehID)

def getLateralAlignment(self, vehID):
    """getLateralAlignment(string) -> string
    Returns The preferred lateral alignment of the vehicle
    """
    return self._getUniversal(tc.VAR_LATALIGNMENT, vehID)

def getAllowedSpeed(self, vehID):
    """getAllowedSpeed(string) -> double
    Returns the maximum allowed speed on the current lane regarding speed factor in m/s for this vehicle.
    """
    return self._getUniversal(tc.VAR_ALLOWED_SPEED, vehID)

def getVehicleClass(self, vehID):
    """getVehicleClass(string) -> string
    Returns the vehicle class of this vehicle.
    """
    return self._getUniversal(tc.VAR_VEHICLECLASS, vehID)

def getSpeedFactor(self, vehID):
    """getSpeedFactor(string) -> double
    Returns the chosen speed factor for this vehicle.
    """
    return self._getUniversal(tc.VAR_SPEED_FACTOR, vehID)

def getSpeedDeviation(self, vehID):
    """getSpeedDeviation(string) -> double
    Returns the standard deviation for the speed factor of the vehicle type.
    """
    return self._getUniversal(tc.VAR_SPEED_DEVIATION, vehID)

def getEmissionClass(self, vehID):
    """getEmissionClass(string) -> string
    Returns the emission class of this vehicle.
    """
    return self._getUniversal(tc.VAR_EMISSIONCLASS, vehID)

def getWaitingTime(self, vehID):
    """getWaitingTime() -> double
    The waiting time of a vehicle is defined as the time (in seconds) spent with a
    speed below 0.1m/s since the last time it was faster than 0.1m/s.
    (basically, the waiting time of a vehicle is reset to 0 every time it moves).
    A vehicle that is stopping intentionally with a <stop> does not accumulate waiting time.
    """
    return self._getUniversal(tc.VAR_WAITING_TIME, vehID)

def getAccumulatedWaitingTime(self, vehID):
    """getAccumulatedWaitingTime() -> double
    The accumulated waiting time of a vehicle collects the vehicle's waiting time
    over a certain time interval (interval length is set per option '--waiting-time-memory')
    """
    return self._getUniversal(tc.VAR_ACCUMULATED_WAITING_TIME, vehID)

def getLaneChangeMode(self, vehID):
    """getLaneChangeMode(string) -> integer
    Gets the vehicle's lane change mode as a bitset.
    """
    return self._getUniversal(tc.VAR_LANECHANGE_MODE, vehID)

def getSpeedMode(self, vehID):
    """getSpeedMode -> int
    The speed mode of a vehicle
    """
    return self._getUniversal(tc.VAR_SPEEDSETMODE, vehID)

def getSlope(self, vehID):
    """getSlope -> double
    The slope at the current position of the vehicle in degrees
    """
    return self._getUniversal(tc.VAR_SLOPE, vehID)

def getWidth(self, vehID):
    """getWidth(string) -> double
    Returns the width in m of this vehicle.
    """
    return self._getUniversal(tc.VAR_WIDTH, vehID)

def getHeight(self, vehID):
    """getHeight(string) -> double
    Returns the height in m of this vehicle.
    """
    return self._getUniversal(tc.VAR_HEIGHT, vehID)

def getLine(self, vehID):
    """getLine(string) -> string
    Returns the line information of this vehicle.
    """
    return self._getUniversal(tc.VAR_LINE, vehID)

def getVia(self, vehID):
    """getVia(string) -> list(string)
    Returns the ids of via edges for this vehicle
    """
    return self._getUniversal(tc.VAR_VIA, vehID)

def getMinGap(self, vehID):
    """getMinGap(string) -> double
    Returns the offset (gap to front vehicle if halting) of this vehicle.
    """
    return self._getUniversal(tc.VAR_MINGAP, vehID)

def getShapeClass(self, vehID):
    """getShapeClass(string) -> string
    Returns the shape class of this vehicle.
    """
    return self._getUniversal(tc.VAR_SHAPECLASS, vehID)

def getAccel(self, vehID):
    """getAccel(string) -> double
    Returns the maximum acceleration possibility in m/s^2 of this vehicle.
    """
    return self._getUniversal(tc.VAR_ACCEL, vehID)

def getDecel(self, vehID):
    """getDecel(string) -> double
    Returns the preferred maximal deceleration possibility in m/s^2 of this vehicle.
    """
    return self._getUniversal(tc.VAR_DECEL, vehID)

def getEmergencyDecel(self, vehID):
    """getEmergencyDecel(string) -> double
    Returns the maximal physically possible deceleration in m/s^2 of this vehicle.
    """
    return self._getUniversal(tc.VAR_EMERGENCY_DECEL, vehID)

def getApparentDecel(self, vehID):
    """getApparentDecel(string) -> double
    Returns the apparent deceleration in m/s^2 of this vehicle.
    """
    return self._getUniversal(tc.VAR_APPARENT_DECEL, vehID)

def getActionStepLength(self, vehID):
    """getActionStepLength(string) -> double
    Returns the action step length for this vehicle.
    """
    return self._getUniversal(tc.VAR_ACTIONSTEPLENGTH, vehID)

def getLastActionTime(self, vehID):
    """getLastActionTime(string) -> double
    Returns the time of last action point for this vehicle.
    """
    return self._getUniversal(tc.VAR_LASTACTIONTIME, vehID)

def getImperfection(self, vehID):
    """getImperfection(string) -> double
    .
    """
    return self._getUniversal(tc.VAR_IMPERFECTION, vehID)

def getTau(self, vehID):
    """getTau(string) -> double
    Returns the driver's reaction time in s for this vehicle.
    """
    return self._getUniversal(tc.VAR_TAU, vehID)

def getBestLanes(self, vehID):
    """getBestLanes(string) ->
    Information about the wish to use subsequent edges' lanes.
    """
    return self._getUniversal(tc.VAR_BEST_LANES, vehID)


def getNextTLS(self, vehID):
    """getNextTLS(string) ->
    Return list of upcoming traffic lights [(tlsID, tlsIndex, distance, state), ...]
    """
    return self._getUniversal(tc.VAR_NEXT_TLS, vehID)



    @staticmethod
    def subscribe_args_list():
        return tc.VAR_WAITING_TIME, tc.VAR_SPEED
