from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.completed_missions = 0
        self.failed_missions = 0

    def add_astronaut(self, astronaut_type, name):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        astronaut = self.__create_astronaut(astronaut_type, name)
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name, items):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet = Planet(name)
        planet.items = items.split(', ')
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        astronaut = self.astronaut_repository.find_by_name(name)

        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name):
        planet = self.planet_repository.find_by_name(planet_name)

        if planet is None:
            raise Exception("Invalid planet name!")

        astronauts_for_mission = self.astronaut_repository.find_all_suitable_astronauts(5, 30)

        if len(astronauts_for_mission) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")

        participated_in_mission = 0

        for astronaut in astronauts_for_mission:
            if len(planet.items) == 0:
                break
            while len(planet.items) > 0 and astronaut.oxygen > 0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
            participated_in_mission += 1

        if len(planet.items) == 0:
            self.completed_missions += 1
            return f"Planet: {planet_name} was explored. {participated_in_mission} astronauts participated in collecting items."
        else:
            self.failed_missions += 1
            return "Mission is not completed."


    def report(self):
        result = f'{self.completed_missions} successful missions!' + '\n'
        result += f'{self.failed_missions} missions were not completed!' + '\n'
        result += "Astronauts' info:" + '\n'

        for astronaut in self.astronaut_repository.astronauts:
            result += str(astronaut) + '\n'

        return result.strip()

    def __create_astronaut(self, astronaut_type, name):
        if astronaut_type == "Biologist":
            return Biologist(name)
        if astronaut_type == "Geodesist":
            return Geodesist(name)
        if astronaut_type == "Meteorologist":
            return Meteorologist(name)
        raise Exception("Astronaut type is not valid!")

