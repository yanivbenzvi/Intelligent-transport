from src.provider.SumoProvider import SumoProvider

production = False
sumoBinary = "sumo" if production else "sumo-gui"
sumoFolder = "C:\\Users\\Yaniv\\Desktop\\MoSTScenario\\scenario\\most.sumocfg"
sumoCmd = [sumoBinary, "-c", sumoFolder, "-S"]
app_providers = [
    SumoProvider
]
