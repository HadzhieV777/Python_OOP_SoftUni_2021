from Exam_Prep.Exam_23_08_2021.project import BakedFood


class Cake(BakedFood):
    DEFAULT_PORTION_GRAMS = 245

    def __init__(self, name, price) :
        super().__init__(name, self.DEFAULT_PORTION_GRAMS, price)