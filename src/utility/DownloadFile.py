import os
import urllib.request
import zipfile
import tarfile
from src.utility.DownloadProgressBar import DownloadProgressBar
from urllib.parse import urlparse
from src import Configuration
from os.path import basename
from pathlib import Path


class DownloadFile:

    @staticmethod
    def url2name(url):
        return basename(urlparse(url)[2])

    @staticmethod
    def download_file(url, folder_path, file_name=None):
        download_path = Configuration.project_path + "\\" + folder_path + "\\"
        if file_name is None:
            download_path += DownloadFile.get_url_file_name(url)
        else:
            if DownloadFile.has_extension(file_name) is False:
                file_name += "." + str(DownloadFile.get_extension_from_url(url))
            download_path += file_name
        result = None
        my_file = Path(download_path)
        print("\n\nstarting to download file: \n" + DownloadFile.get_url_file_name(url))
        if not my_file.is_file():
            with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=url.split('/')[-1]) as t:
                result = urllib.request.urlretrieve(url, download_path, reporthook=t.update_to)
        if result is not None:
            print("\nfinish download: " + str(DownloadFile.get_extension_from_url(url)))
        return {"download_path": download_path, "result": result}

    @staticmethod
    def has_extension(file_name):
        extension = file_name.split(".")
        return extension[-1] is not None and len(extension) is not 1

    @staticmethod
    def get_extension_from_url(url):
        return DownloadFile.get_url_file_name(url).split(".")[-1]

    @staticmethod
    def get_extension_from_file(path_name):
        return Path(path_name).suffix

    @staticmethod
    def get_url_file_name(url):
        req = urllib.request.Request(url)
        remote_file = urllib.request.urlopen(req)
        if 'Content-Disposition' in remote_file.info():
            file_name = remote_file.info()['Content-Disposition'].split('filename=')[1]
            if file_name[0] == '"' or file_name[0] == "'":
                file_name = file_name[1:-1]
        else:
            file_name = DownloadFile.url2name(remote_file.url)

        # print("file_name: ", file_name)
        return file_name

    @staticmethod
    def get_file_name_from_path(path):
        return os.path.basename(path).split(".")[0]

    @staticmethod
    def remove_file(path):
        if os.path.isfile(path):
            os.remove(path)

    @staticmethod
    def download_zip(url, folder_path, file_name=None, unpack=False, delete_after_unpack=True):
        result = DownloadFile.download_file(url, folder_path, file_name)
        ext = DownloadFile.get_extension_from_file(result['download_path'])
        if unpack:
            print("starting unpack file\n")
            project_path = Configuration.project_path + "\\" + folder_path
            if ext == ".zip":
                print("result:", result['download_path'])
                with zipfile.ZipFile(result['download_path'], 'r') as zip_ref:
                    zip_ref.extractall(project_path)
            elif ext == ".gz":
                tar = tarfile.open(result['download_path'])
                file_list = filter(lambda file: len(file.name.split("/")) == 1 and file.isdir(), tar.getmembers())
                folder_name = DownloadFile.get_file_name_from_path(result['download_path']) if len(
                    list(file_list)) is not 1 else ""
                tar.extractall(path=project_path + "\\" + folder_name)
                tar.close()
        if delete_after_unpack:
            DownloadFile.remove_file(result['download_path'])
        return project_path


if __name__ == "__main__":
    # file_url = "https://images.unsplash.com/reserve/Af0sF2OS5S5gatqrKzVP_Silhoutte.jpg?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60"
    # DownloadFile.download_file(file_url, "simulator", "scenario.jpg")
    # DownloadFile.download_file(file_url, "simulator")
    # DownloadFile.download_file(file_url, "simulator", "demo_download")
    #
    # file_url = "http://academic.lucabedogni.it/wp-content/uploads/2019/11/bolognaringway_1.0.tar.gz"
    # DownloadFile.download_zip(file_url, "simulator", unpack=True)
    #
    # file_url = "https://github.com/lcodeca/MoSTScenario/archive/v0.6.tar.gz"
    # DownloadFile.download_zip(file_url, "simulator", unpack=True)

    file_url = "https://github.com/lcodeca/MoSTScenario/archive/v0.6.zip"
    DownloadFile.download_zip(file_url, "simulator", unpack=True)


