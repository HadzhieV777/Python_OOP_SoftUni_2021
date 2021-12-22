class PetShop:
    def __init__(self, name: str):
        # TODO name, food and pets are valid
        self.name = name
        self.food = {}
        self.pets = []

    def add_food(self, name: str, quantity: float):
        # TODO Quantity is -1
        if quantity <= 0:
            raise ValueError('Quantity cannot be equal to or less than 0')

        # TODO name not in food
        # TODO name already in food
        if name not in self.food:
            self.food[name] = 0
        self.food[name] += quantity

        # TODO test the return message
        return f"Successfully added {quantity:.2f} grams of {name}."

    def add_pet(self, name: str):
        # TODO happy case
        if name not in self.pets:
            self.pets.append(name)
            return f"Successfully added {name}."
        # TODO pet in pets
        raise Exception("Cannot add a pet with the same name")

    def feed_pet(self, food_name: str, pet_name: str):
        # TODO pet not in pets
        if pet_name not in self.pets:
            raise Exception(f"Please insert a valid pet name")

        # TODO food not in foods
        if food_name not in self.food:
            return f'You do not have {food_name}'

        # TODO food of type is 99
        if self.food[food_name] < 100:
            self.add_food(food_name, 1000.00)
            return "Adding food..."

        # TODO Happy Case
        self.food[food_name] -= 100
        return f"{pet_name} was successfully fed"

    def __repr__(self):
        # TODO check without pets
        # TODO check with pets
        return f'Shop {self.name}:\n' \
               f'Pets: {", ".join(self.pets)}'
