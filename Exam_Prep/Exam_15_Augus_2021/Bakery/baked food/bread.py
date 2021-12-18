from Exam_Prep.Exam_23_08_2021.project import BakedFood


class Bread(BakedFood):
    DEFAULT_PORTION_GRAMS = 200

    def __init__(self, name: str, price: float) -> None:
        super().__init__(name, self.DEFAULT_PORTION_GRAMS, price)