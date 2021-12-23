from project.appliances.appliance import Appliance


class Stove(Appliance):
    __COST_BY_DEFAULT = 0.7

    def __init__(self):
        super().__init__(self.__COST_BY_DEFAULT)