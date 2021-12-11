from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    AQUARIUM = "FreshwaterAquarium"
    VALUE_TO_INCREASE_FISH_SIZE_WITH = 3

    def __init__(self, name, species, price):
        super().__init__(name = name, species = species, size = 3, price = price)

    def eat(self):
        self.size += self.VALUE_TO_INCREASE_FISH_SIZE_WITH

