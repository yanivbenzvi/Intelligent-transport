from src.modules.Vehicle import Vehicle
from xml.sax import handler, make_parser
from src.Configuration import project_path
from src.utility.AnalysisFileStat import getBasicStats


class VehInformationReader(handler.ContentHandler):
    def __init__(self, vehList):
        super().__init__()
        self._vehList = vehList
        self._Vehicle = None
        self._routeString = ''

    def startElement(self, name, attrs):
        if name == 'tripinfo' and not attrs['vType'] == "slowbicycle":
            self._Vehicle = Vehicle(attrs['id'])
            self._Vehicle.traveltime = float(attrs['duration'])
            self._Vehicle.v_type = attrs['vType']
            self._Vehicle.travellength = float(attrs['routeLength'])
            self._Vehicle.departdelay = float(attrs['departDelay'])
            self._Vehicle.waittime = float(attrs['departDelay']) + float(attrs['waitingTime'])
            self._vehList.append(self._Vehicle)


if __name__ == "__main__":
    parser = make_parser()
    allvehicles = []
    parser.setContentHandler(VehInformationReader(allvehicles))
    parser.parse(project_path + "/tests/resources/bologna_ringway_1.0_date-24-06-2020_12-51-14_tripinfo.trips.xml")

    getBasicStats(True, None, allvehicles)
