from Exam_Prep.Exam_23_08_2021.project import Drink


class Tea(Drink):
    DEFAULT_PRICE = 2.50

    def __init__(self, name, portion, brand):
        super().__init__(name=name, portion=portion, price=Tea.DEFAULT_PRICE, brand=brand)
