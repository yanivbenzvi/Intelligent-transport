class Edge:
    # from \\scenario\\in\\most.net.xml
    def __init__(self, edge_id, edge_from, edge_to, lane_id, priority=None, edge_type=None, shape=None):
        self.edge_id = edge_id
        self.edge_from = edge_from
        self.edge_to = edge_to
        self.priority = priority
        self.edge_type = edge_type
        self.shape = shape
        self.lane_id = lane_id
