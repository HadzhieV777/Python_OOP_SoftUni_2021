from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    AQUARIUM = "SaltwaterAquarium"
    VALUE_TO_INCREASE_FISH_SIZE_WITH = 2

    def __init__(self, name, species, price):
        super().__init__(name = name, species = species, size = 5, price = price)

    def eat(self):
        self.size += self.VALUE_TO_INCREASE_FISH_SIZE_WITH


