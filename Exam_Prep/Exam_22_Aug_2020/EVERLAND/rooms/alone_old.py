from project.rooms.room import Room


class AloneOld(Room):
    __ALLOWED_MEMBERS = 1
    __DEFAULT_ROOM_COST = 10

    def __init__(self, family_name, pension):
        super().__init__(family_name, pension, AloneOld.__ALLOWED_MEMBERS)
        self.room_cost = self.__DEFAULT_ROOM_COST
