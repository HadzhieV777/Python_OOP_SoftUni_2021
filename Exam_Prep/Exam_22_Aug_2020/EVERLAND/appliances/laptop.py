from project.appliances.appliance import Appliance


class Laptop(Appliance):
    __COST_BY_DEFAULT = 1

    def __init__(self):
        super().__init__(self.__COST_BY_DEFAULT)
