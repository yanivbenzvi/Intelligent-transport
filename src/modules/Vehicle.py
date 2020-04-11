class Vehicle:
    # from \\scenario\\in\\add\\basic.vType.xml
    def __init__(self, vehicle_type, v_id, lat_alignment, person_capacity=-1, tau=-1, speed_dev=-1, lc_cooperative=0.0,
                 key="", value="false", probability=-1, max_speed=-1, sigma=-1, gui_shape="passenger"):
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

