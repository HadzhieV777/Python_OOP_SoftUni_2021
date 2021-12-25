from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    __ALLOWED_MEMBERS = 2
    __DEFAULT_ROOM_COST = 20
    __APPLIANCES_BY_DEFAULT = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name, salary_one, salary_two):
        super().__init__(family_name, salary_one + salary_two, YoungCouple.__ALLOWED_MEMBERS)
        self.room_cost = self.__DEFAULT_ROOM_COST
        self.appliances = self.__APPLIANCES_BY_DEFAULT * 2
        self.calculate_expenses(self.appliances)



