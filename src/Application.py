from src import Providers


class Application:
    def __init__(self):
        self.start = False

    def startup(self):
        print("starting application")
        providers = list(map(lambda provider: provider(), Providers.app_providers))
        providers = list(map(lambda provider: provider.boot(), providers))
        self.start = True
