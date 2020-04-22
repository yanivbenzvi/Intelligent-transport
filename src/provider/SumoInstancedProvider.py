from src.modules.Lanes import Lane
from src.modules.Junction import Junction
from src.modules.Vehicle import Vehicle
from src.modules.Edge import Edge


class SumoInstanseProvider:
    def __init__(self, senario):
        self.xmlFile = senario

    def boot(self):

    @staticmethod
    def instance_list():
        return {
            'Lane': {
                'ctor': Lane,
                # 'param' : Lane.get_param_name
            },
            'Junction': {
                'ctor': Junction
            },
            'vehicle': {
                'ctor': Vehicle
            },
            'edge': {
                'ctor' : Edge
            }

        }
