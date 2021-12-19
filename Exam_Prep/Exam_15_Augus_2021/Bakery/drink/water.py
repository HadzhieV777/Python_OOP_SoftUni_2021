from Exam_Prep.Exam_23_08_2021.project import Drink


class Water(Drink):
    DEFAULT_PRICE = 1.50

    def __init__(self, name, portion, brand):
        super().__init__(name, portion, self.DEFAULT_PRICE, brand)