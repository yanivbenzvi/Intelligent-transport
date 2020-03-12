from src import Configuration


class Application:
    def __init__(self):
        self.start = False

    def startup(self):
        print("starting application")
        providers = list(map(lambda provider: provider(), Configuration.app_providers))
        providers = list(map(lambda provider: provider.boot(), providers))
        self.start = True
