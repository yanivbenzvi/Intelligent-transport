class Junction:
    # from \\scenario\\in\\most.net.xml
    def __init__(self, junction_id, junction_type, inc_lanes, int_lanes, x=None, y=None, z=None):
        self.junction_id = junction_id
        self.junction_type = junction_type
        self.inc_lanes = inc_lanes
        self.int_lanes = int_lanes
        self.x = x
        self.y = y
        self.z = z
