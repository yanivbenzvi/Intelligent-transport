class Lane:
    # from \\scenario\\in\\most.net.xml
    def __init__(self, lane_id, index, allow, speed, length=None, width=None, shape=None):
        self.lane_id = lane_id
        self.index = index
        self.allow = allow
        self.speed = speed
        self.length = length
        self.width = width
        self.shape = shape
