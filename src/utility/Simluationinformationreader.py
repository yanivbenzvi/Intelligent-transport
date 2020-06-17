from xml.sax import handler, make_parser


class SimulationInformationReader(handler.ContentHandler):
    def __init__(self):
        super().__init__()
        self.begin = None
        self.end = None

    def startElement(self, name, attrs):
        if name == 'begin':
            self.begin = attrs['value']
        elif name == 'end':
            self.end = attrs['value']

    @staticmethod
    def extract_time(xml_path):
        parser = make_parser()
        model = SimulationInformationReader()
        parser.setContentHandler(model)
        parser.parse(xml_path)
        return model.begin, model.end
