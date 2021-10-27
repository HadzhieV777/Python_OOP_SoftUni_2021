# 04. Cup

class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, quantity):
        free_space = (self.size - self.quantity)
        if quantity <= free_space:
            self.quantity += quantity

    def status(self):
        free_space = (self.size - self.quantity)
        return free_space


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())