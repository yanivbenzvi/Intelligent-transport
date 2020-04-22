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
