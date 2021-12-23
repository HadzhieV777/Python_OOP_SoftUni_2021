from project.appliances.appliance import Appliance


class Fridge(Appliance):
    __COST_BY_DEFAULT = 1.2

    def __init__(self):
        super().__init__(self.__COST_BY_DEFAULT)
