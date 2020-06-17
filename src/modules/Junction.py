class Junction:

    # from \\scenario\\in\\most.net.xml
    def __init__(self, junction_id, inc_lanes, int_lanes, request=None, junction_type='traffic_light', x=None, y=None,
                 z=None):
        """
        :param junction_id:   unique name - String example - "131241"
        :param junction_type: type - String example - "priority"
        :param inc_lanes:     all incoming paths list separated space - String example - "152137#4_0 152137#4_1 152137#4_2"
        :param int_lanes:     all internal paths list separated ':' - String example - ":131241_0_0 :131241_1_0 :131241_1_1"
        :param x:             position X in Axis system - String example - "4408.64",  default = None
        :param y:             position Y in Axis system - String example - "1373.60",  default = None
        :param z:             position Z in Axis system - String example - "21.13",  default = None
        """
        self.junction_id = junction_id
        self.junction_type = junction_type
        self.inc_lanes = inc_lanes
        self.int_lanes = int_lanes
        self.x = x
        self.y = y
        self.z = z
        self.request = request
