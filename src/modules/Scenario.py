from src.utility.DownloadFile import DownloadFile
from src.utility import Path
from src import Configuration
import time


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

    def path_to_scenario_conf(self):
        return Configuration.project_path + "\\" + Scenario.ScenarioLocation + "\\" + self.dest_folder + \
               "\\" + self.conf_path + "\\" + self.conf_file_name

    def path_to_net_xml_file(self):
        return Configuration.project_path + "\\" + Scenario.ScenarioLocation + "\\" + self.dest_folder + \
               "\\" + self.net_xml_path

    def path_to_vehicle_xml_file(self):
        return Configuration.project_path + "\\" + Scenario.ScenarioLocation + "\\" + self.dest_folder + \
               "\\" + self.vehicle_xml_path

    def search_for_xml(self):
        pass

    def get_simulation_time(self, star, end):
        num_of_intervals = end - star
        if isinstance(num_of_intervals, int):
            return num_of_intervals
        else:
            return int(num_of_intervals + 1)

    def get_num_of_cells(self, num_of_intervals, hourse):
        num_of_cells = num_of_intervals / hourse
        if isinstance(num_of_cells, int):
            return num_of_cells
        else:
            return int(num_of_cells + 1)

    def get_cells_number(self, num_of_cells, time, cell_hourse):
        count = 0;
        start = cell_hourse
        if start >= time:
            return count
        while start <= time:
            start += cell_hourse
            count += 1
        if num_of_cells < count:
            count = -1
        return count
