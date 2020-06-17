class Vehicle:
    # from \\scenario\\in\\most.net.xml
    def __init__(self, v_id):  # , v_type, depart, departLane, arrivalPos, edges=None):
        """
        :param v_id:       Unique name - String example - "pedestrian_3-1_3451_tr"
        :param v_type:     Vehicle type - String example - "passenger"
        :param depart:     Start flow - String example - "triggered"
        :param departLane: Depart type - String example  - "best"
        :param arrivalPos: Coordinates location arrive example - "22.89"
        :param edges:      list where visitor separated ' ' String example -"-153457 153452#1 153452#2 153451#1 153451#2 153451#3"
        """
        self.v_id = v_id
        self.v_type = None
        # self.depart = depart
        # self.departLane = departLane
        # self.arrivalPos = arrivalPos
        # self.edges = edges

        self.label = v_id
        self.method = None
        self.depart = 0.
        self.arrival = 0.
        self.speed = 0.
        self.route = []
        self.traveltime = 0.
        self.travellength = 0.
        self.departdelay = 0.
        self.waittime = 0.
        self.rank = 0.

    @classmethod
    def from_args(cls, **kwargs) -> 'Vehicle':
        print(kwargs)
        return cls(v_id=kwargs['v_id'], v_type=kwargs['v_type'], depart=kwargs['depart'],
                   departLane=kwargs['departLane'], arrivalPos=kwargs['arrivalPos'], edges=None)
