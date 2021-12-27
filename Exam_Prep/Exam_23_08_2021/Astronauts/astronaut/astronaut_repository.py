from project.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        if astronaut in self.astronauts:
            self.astronauts.remove(astronaut)

    def find_by_name(self, name):
        for astronaut in self.astronauts:
            if astronaut.name == name:
                return astronaut

    def find_all_suitable_astronauts(self, count, needed_oxygen):
        return sorted([astronaut for astronaut in self.astronauts if astronaut.oxygen > needed_oxygen],
                      key=lambda x: x.oxygen,
                      reverse=True)[0: count]


