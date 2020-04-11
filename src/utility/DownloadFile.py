import urllib.request
import os
from src import Configuration


class DownloadFile:
    @staticmethod
    def download_file(url, path):
        urllib.request.urlretrieve(url, path)

    def download_zip(url, path,  ):


if __name__ == "__main__":
    DownloadFile.download_file(
        "https://images.unsplash.com/reserve/Af0sF2OS5S5gatqrKzVP_Silhoutte.jpg?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60",
        Configuration.project_path + "\simulator\scinario.jpg")
