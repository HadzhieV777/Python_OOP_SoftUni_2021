from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    __ALLOWED_MEMBERS = 1
    __DEFAULT_ROOM_COST = 10
    __APPLIANCES_BY_DEFAULT = [TV()]

    def __init__(self, family_name, salary):
        super().__init__(family_name, salary, AloneYoung.__ALLOWED_MEMBERS)
        self.room_cost = self.__DEFAULT_ROOM_COST
        self.appliances = self.__APPLIANCES_BY_DEFAULT
        self.calculate_expenses(self.appliances)
