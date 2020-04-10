from src.utility import Path

production = False
sumoBinary = "sumo" if production else "sumo-gui"
project_folder_name = "smart-transport"
project_path = Path.get_project_home_path()
sumoFolder = "C:\\Users\\Yaniv\\Desktop\\MoSTScenario\\scenario\\most.sumocfg"
sumoCmd = [sumoBinary, "-c", sumoFolder, "-S"]

