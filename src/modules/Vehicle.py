class Vehicle:
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

