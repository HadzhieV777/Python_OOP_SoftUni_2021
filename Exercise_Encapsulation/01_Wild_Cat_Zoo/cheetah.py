from project.animal import Animal


class Cheetah(Animal):
    CHEETAH_MONEY_FOR_CARE = 60

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, Cheetah.CHEETAH_MONEY_FOR_CARE)