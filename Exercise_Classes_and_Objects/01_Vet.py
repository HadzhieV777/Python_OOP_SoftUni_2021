# 01. Vet

class Vet:
    animals = []
    space = 5

    def __init__(self, name: str, ):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name):
        if not len(self.animals) < Vet.space:
            return "Not enough space"
        Vet.animals.append(animal_name)
        self.animals.append(animal_name)
        return f"{animal_name} registered in the clinic"

    def unregister_animal(self, animal_name):
        if animal_name not in self.animals:
            return f"{animal_name} not in the clinic"

        for animal in self.animals:
            if animal == animal_name:
                Vet.animals.remove(animal_name)
                self.animals.remove(animal_name)
                return f"{animal_name} unregistered successfully"