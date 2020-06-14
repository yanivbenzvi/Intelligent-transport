from src.utility import Path
from src import Configuration
from src.utility.DownloadFile import DownloadFile
from src.utility.Simluationinformationreader import SimulationInformationReader


class Scenario:
    ScenarioLocation = "simulator"

    def __init__(self, name, download_url, dest_folder, conf_path, conf_file_name, net_xml_path, net_xml_file,
                 vehicle_xml_path, vehicle_xml_file):
        self.name = name
        self.download_url = download_url
        self.dest_folder = dest_folder
        self.conf_path = conf_path
        self.conf_file_name = conf_file_name
        self.net_xml_path = net_xml_path
        self.net_xml_file = net_xml_file
        self.vehicle_xml_path = vehicle_xml_path
        self.vehicle_xml_file = vehicle_xml_file
        self.traci = None
        self.start_end_point = None

    def download_scenario(self):
        scenario_folder = Configuration.project_path + "\\" + Scenario.ScenarioLocation + "\\" + self.dest_folder
        print("scenario_folder", scenario_folder)

        if not Path.folder_exist(scenario_folder):
            print("scenario files not exist, starting download...")
            if DownloadFile.get_extension_from_url(self.download_url) in ["zip", ".zip", ".7z", "7z", "gz", ".gz",
                                                                          ".tar"]:
                return DownloadFile.download_zip(self.download_url, "simulator", unpack=True)
            else:
                return DownloadFile.download_file(self.download_url, Scenario.ScenarioLocation)
        else:
            print("scenario files exist there is no need to download.\n")

    def path_to_scenario_folder(self):
        return Configuration.project_path + "\\" + Scenario.ScenarioLocation + "\\" + self.dest_folder + \
               "\\"
    def path_to_scenario_conf(self):
        return self.path_to_scenario_folder() + self.conf_file_name

    def path_to_net_xml_file(self):
        return self.path_to_scenario_folder() + self.net_xml_path

    def path_to_vehicle_xml_file(self):
        return self.path_to_scenario_folder() + self.vehicle_xml_path

    def search_for_xml(self):
        pass

    def scenario_start_end_tuple(self):
        if not self.start_end_point:
            self.start_end_point = SimulationInformationReader.extract_time(self.path_to_scenario_conf())
        return self.start_end_point

    def scenario_start_time(self):
        return self.scenario_start_end_tuple()[0]

    def scenario_end_time(self):
        return self.scenario_start_end_tuple()[1]

    def scenario_duration(self):
        return (float(self.scenario_end_time()) - float(self.scenario_start_time())) / 3600

    @staticmethod
    def get_num_of_cells(duration, interval_length):
        num_of_cells = duration / interval_length
        if isinstance(num_of_cells, int):
            return num_of_cells
        else:
            return int(num_of_cells + 1)

    @staticmethod
    def get_cells_number(num_of_cells, calc_time, interval_length):
        count = 0;
        start = interval_length
        if start >= calc_time:
            return count
        while start <= calc_time:
            start += interval_length
            count += 1
        if num_of_cells < count:
            count = -1
        return count
