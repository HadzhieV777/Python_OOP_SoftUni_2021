from Exam_Prep.Exam_23_08_2021.project import Table


class InsideTable(Table):
    __VALID_TABLE_NUMBER_RANGE = range(1, 51)
    __INVALID_TABLE_ERROR = "Inside table's number must be between 1 and 50 inclusive!"

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if value not in self.__VALID_TABLE_NUMBER_RANGE:
            raise ValueError(self.__INVALID_TABLE_ERROR)

        self.__table_number = value