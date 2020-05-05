import traci.constants as tc
from traci._lane import _readLinks
from traci.domain import Domain
from traci.storage import Storage

class VehicleType:
    # from \\scenario\\in\\add\\basic.vType.xml
    def __init__(self, vehicle_type, v_id, lat_alignment, person_capacity=-1, tau=1, speed_dev=-1, lc_cooperative=0.0,
                 key="", value="false", probability=-1, max_speed=-1, sigma=-1, gui_shape="passenger"):
        """
        :param vehicle_type:    vehicle type String example - "passenger"
        :param v_id:            vehicle id String example - "passenger1"
        :param lat_alignment:   alignment vehicle String example - "center"
        :param person_capacity: number of passengers String example - "4"
        :param tau:             this means vehicles will be in a stationary state at 7.885m/s String example - "0.5"
        :param speed_dev:       the deviation of the speedFactor String example - "0.1"
        :param lc_cooperative:  the willingness for performing cooperative lane changing. String example - "0.0"
        :param key:             param key String example - "has.rerouting.device"
        :param value:           param value String example - "false"
        :param probability:     probability for emitting a vehicle each second - String example - ".33"
        :param max_speed:       the vehicle's maximum velocity (in m/s) - String example - "2.0"
        :param sigma:           the driver imperfection (0 denotes perfect driving - String example- "2.0"
        :param gui_shape:       vehicle shape for drawing. By default a standard passenger car body is drawn String example - "passenger"
        """
        self.vehicle_type = vehicle_type
        self.v_id = v_id
        self.lat_alignment = lat_alignment
        self.person_capacity = person_capacity
        self.tau = tau
        self.speed_dev = speed_dev
        self.lc_cooperative = lc_cooperative
        self.key = key
        self.value = value
        self.probability = probability
        self.max_speed = max_speed
        self.sigma = sigma
        self.gui_shape = gui_shape

def getLength(self, typeID):
    """getLength(string) -> double
    Returns the length in m of the vehicles of this type.
    """
    return self._getUniversal(tc.VAR_LENGTH, typeID)

def getMaxSpeed(self, typeID):
    """getMaxSpeed(string) -> double
    Returns the maximum speed in m/s of vehicles of this type.
    """
    return self._getUniversal(tc.VAR_MAXSPEED, typeID)

def getSpeedFactor(self, typeID):
    """getSpeedFactor(string) -> double
    .
    """
    return self._getUniversal(tc.VAR_SPEED_FACTOR, typeID)

def getSpeedDeviation(self, typeID):
    """getSpeedDeviation(string) -> double
    Returns the maximum speed deviation of vehicles of this type.
    """
    return self._getUniversal(tc.VAR_SPEED_DEVIATION, typeID)

def getAccel(self, typeID):
    """getAccel(string) -> double
    Returns the maximum acceleration in m/s^2 of vehicles of this type.
    """
    return self._getUniversal(tc.VAR_ACCEL, typeID)

def getDecel(self, typeID):
    """getDecel(string) -> double
    Returns the maximal comfortable deceleration in m/s^2 of vehicles of this type.
    """
    return self._getUniversal(tc.VAR_DECEL, typeID)

def getEmergencyDecel(self, typeID):
    """getEmergencyDecel(string) -> double
    Returns the maximal physically possible deceleration in m/s^2 of vehicles of this type.
    """
    return self._getUniversal(tc.VAR_EMERGENCY_DECEL, typeID)

def getApparentDecel(self, typeID):
    """getApparentDecel(string) -> double
    Returns the apparent deceleration in m/s^2 of vehicles of this type.
    """
    return self._getUniversal(tc.VAR_APPARENT_DECEL, typeID)

def getActionStepLength(self, typeID):
    """getActionStepLength(string) -> double
    Returns the action step length for vehicles of this type.
    """
    return self._getUniversal(tc.VAR_ACTIONSTEPLENGTH, typeID)

def getImperfection(self, typeID):
    """getImperfection(string) -> double
    .
    """
    return self._getUniversal(tc.VAR_IMPERFECTION, typeID)

def getTau(self, typeID):
    """getTau(string) -> double
    Returns the driver's reaction time in s for vehicles of this type.
    """
    return self._getUniversal(tc.VAR_TAU, typeID)

def getVehicleClass(self, typeID):
    """getVehicleClass(string) -> string
    Returns the class of vehicles of this type.
    """
    return self._getUniversal(tc.VAR_VEHICLECLASS, typeID)

def getEmissionClass(self, typeID):
    """getEmissionClass(string) -> string
    Returns the emission class of vehicles of this type.
    """
    return self._getUniversal(tc.VAR_EMISSIONCLASS, typeID)

def getShapeClass(self, typeID):
    """getShapeClass(string) -> string
    Returns the shape class of vehicles of this type.
    """
    return self._getUniversal(tc.VAR_SHAPECLASS, typeID)

def getMinGap(self, typeID):
    """getMinGap(string) -> double
    Returns the offset (gap to front vehicle if halting) of vehicles of this type.
    """
    return self._getUniversal(tc.VAR_MINGAP, typeID)

def getWidth(self, typeID):
    """getWidth(string) -> double
    Returns the width in m of vehicles of this type.
    """
    return self._getUniversal(tc.VAR_WIDTH, typeID)

def getHeight(self, typeID):
    """getHeight(string) -> double
    Returns the height in m of vehicles of this type.
    """
    return self._getUniversal(tc.VAR_HEIGHT, typeID)

def getColor(self, typeID):
    """getColor(string) -> (integer, integer, integer, integer)
    Returns the color of this type.
    """
    return self._getUniversal(tc.VAR_COLOR, typeID)

def getMaxSpeedLat(self, vehID):
    """getMaxSpeedLat(string) -> double
    Returns the maximum lateral speed in m/s of this type.
    """
    return self._getUniversal(tc.VAR_MAXSPEED_LAT, vehID)

def getLateralAlignment(self, vehID):
    """getLateralAlignment(string) -> string
    Returns The preferred lateral alignment of the type
    """
    return self._getUniversal(tc.VAR_LATALIGNMENT, vehID)

def getMinGapLat(self, vehID):
    """getMinGapLat(string) -> double
    Returns The desired lateral gap of this type at 50km/h in m
    """
    return self._getUniversal(tc.VAR_MINGAP_LAT, vehID)

def getPersonCapacity(self, typeID):
    """getPersonCapacity(string) -> int
    Returns the person capacity of this type
    """
    return self._getUniversal(tc.VAR_PERSON_CAPACITY, typeID)
