from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    __ALLOWED_MEMBERS = 2
    __DEFAULT_ROOM_COST = 15
    __APPLIANCES_BY_DEFAULT = [TV(), Fridge(), Stove()]

    def __init__(self, family_name, pension_one, pension_two):
        super().__init__(family_name, pension_one + pension_two, OldCouple.__ALLOWED_MEMBERS)
        self.room_cost = OldCouple.__DEFAULT_ROOM_COST
        self.appliances = OldCouple.__APPLIANCES_BY_DEFAULT * 2
        self.calculate_expenses(self.appliances)

