from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type, model, speed_limit):
        for auto in self.cars:
            if auto.model == model:
                raise Exception(f"Car {model} is already created!")

        car = self.__create_car(car_type, model, speed_limit)
        self.cars.append(car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name, car_type):
        for driver in self.drivers:
            if driver.name == driver_name:
                car = self.__check_for_available_car(car_type, self.cars)
                old_car = driver.car
                if car == driver.car:
                    driver.car = car
                    car.is_taken = True
                    return f"Driver {driver_name} changed his car from {old_car} to {car.model}."
                driver.car = car
                car.is_taken = True
                return f"Driver {driver_name} chose the car {car.model}."

        raise Exception(f"Driver {driver_name} could not be found!")

    def add_driver_to_race(self, race_name, driver_name):
        for race in self.races:
            if race.name == race_name:
                driver = self.__check_for_available_driver(driver_name, self.drivers)
                self.__check_if_the_driver_is_already_added(driver, race)
                self.__check_if_driver_has_a_car(driver)

                race.drivers.append(driver)
                return f"Driver {driver_name} added in {race_name} race."

        raise Exception(f"Race {race_name} could not be found!")

    def start_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                self.__check_if_there_is_enough_racers(race)
                self.__fint_the_top_three_racers(race)

        raise Exception(f"Race {race_name} could not be found!")

    def __create_car(self, car_type, model, speed_limit):
        if car_type == MuscleCar.__name__:
            return MuscleCar(model, speed_limit)
        if car_type == SportsCar.__name__:
            return SportsCar(model, speed_limit)

    def __check_for_available_car(self, car_type, car_list):
        possible_cars = []
        for car in car_list:
            if car_type == "MuscleCar" or car_type == "SportsCar":
                possible_cars.append(car)
        cars_for_race = [car for car in possible_cars if not car.is_taken]

        if len(cars_for_race) > 0:
            return cars_for_race.pop()
        else:
            raise Exception(f"Car {car_type} could not be found!")

    def __check_for_available_driver(self, driver_name, drivers_list):
        for driver in drivers_list:
            if driver.name == driver_name:
                return driver
        raise Exception(f"Driver {driver_name} could not be found!")

    def __check_if_driver_has_a_car(self, driver):
        if driver.car == None:
            raise Exception(f"Driver {driver.name} could not participate in the race!")

    def __check_if_the_driver_is_already_added(self, driver, race):
        for current_driver in race.drivers:
            if current_driver.name == driver.name:
                return f"Driver {current_driver.name} is already added in {race.name} race."

    def __check_if_there_is_enough_racers(self, race):
        if len(race.drivers) < 3:
            raise Exception(f"Race {race.name} cannot start with less than 3 participants!")

    def __fint_the_top_three_racers(self, race):
        winners =  sorted([x for x in race.drivers], key=lambda x:x.car.speed_limit, reverse=True)[0:3]

        result = []
        for winner in winners:
            winner.number_of_wins += 1
            result.append(f"Driver {winner.name} wins the {race.name} race with a speed of {winner.car.speed_limit}.")

        for winner in winners:
            result.append(f"{winner.name} {winner.number_of_wins}")


        return '\n'.join(result)


