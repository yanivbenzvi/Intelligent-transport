import urllib.request
import os


class DownloadFile:
    @staticmethod
    def download_file(url, path):
        print('Beginning file download with urllib2...\n')
        project_path = os.path.dirname(os.path.abspath(__file__))
        downloaded_path = project_path + path
        print(downloaded_path)
        urllib.request.urlretrieve(url, downloaded_path)


if __name__ == "__main__":
    DownloadFile.download_file("http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg", "\scinario")
