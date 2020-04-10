import os
from src import Configuration


def get_project_home_path():
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    script_dir = os.path.split(script_dir)
    while script_dir[1] != Configuration.project_folder_name:
        script_dir = os.path.split(script_dir[0])

    return script_dir[0] + "\\" + Configuration.project_folder_name
