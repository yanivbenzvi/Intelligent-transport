from src.utility.DownloadFile import DownloadFile
from src.utility import Path
from src import Configuration


class Scenario:
    ScenarioLocation = "simulator"

    def __init__(self, name, download_url, dest_folder, conf_path, conf_file_name):
        self.name = name
        self.download_url = download_url
        self.dest_folder = dest_folder
        self.conf_path = conf_path
        self.conf_file_name = conf_file_name

    def download_scenario(self):
        scenario_folder = Configuration.project_path + "\\" + Scenario.ScenarioLocation + "\\" + self.dest_folder
        print("scenario_folder", scenario_folder)

        if not Path.folder_exist(scenario_folder):
            print("scenario files not exist, starting download...")

            if DownloadFile.get_extension_from_url(self.download_url) in ["zip", ".zip", "gz", ".gz", ".tar"]:
                return DownloadFile.download_zip(self.download_url, "simulator", unpack=True)
            else:
                return DownloadFile.download_file(self.download_url, Scenario.ScenarioLocation)
        else:
            print("scenario files exist there is no need to download.\n")

    def path_to_scenario_conf(self):
        return Configuration.project_path + "\\" + Scenario.ScenarioLocation + "\\" + self.dest_folder + \
               "\\" + self.conf_path + "\\" + self.conf_file_name
