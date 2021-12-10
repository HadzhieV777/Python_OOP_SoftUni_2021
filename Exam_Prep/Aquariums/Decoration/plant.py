from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    DEFAULT_COMFORT = 5
    DEFAULT_PRICE = 10

    def __init__(self):
        super().__init__(Plant.DEFAULT_COMFORT, Plant.DEFAULT_PRICE)