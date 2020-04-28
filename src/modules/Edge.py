class Edge:
    # from \\scenario\\in\\most.net.xml
    def __init__(self, edge_id, edge_from=None, edge_to=None, lane_id=None, priority=None, edge_type=None, shape=None):
        """
        :param edge_id:   unique name - String example - "153459#0"
        :param edge_from: unique from edge - String example - "141010"
        :param edge_to:   unique to edge - String example - "141010"
        :param lane_id:   unique name lane id - String example - "153459#0_0"
        :param priority:  priority - String example - "9", default = None
        :param edge_type: road type - String example - "highway.primary", default = None
        :param shape:     edge shape - String, default = None
        """
        self.edge_id = edge_id
        self.edge_from = edge_from
        self.edge_to = edge_to
        self.priority = priority
        self.edge_type = edge_type
        self.shape = shape
        self.lane_id = lane_id
