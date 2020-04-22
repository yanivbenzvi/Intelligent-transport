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
