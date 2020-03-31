from src.utility.DownloadFile import DownloadFile


class Scenario:
    ScenarioLocation = ".\\simulator"

    def __init__(self, download_url):
        self.download_url = download_url

    def download_scenario(self):
        DownloadFile.download_file(self.download_url, Scenario.ScenarioLocation)
