from project.train.train import Train
from unittest import TestCase, main


class Test(TestCase):
    TRAIN_NAME = "name"
    TRAIN_CAPACITY = 10
    TRAIN_CAPACITY_IF_IS_FULL = 1
    PASSENGER_NAME = 'Pesho'
    SECOND_PASSENGER_NAME = 'Gosho'

    def setUp(self) -> None:
        self.train = Train(self.TRAIN_NAME, self.TRAIN_CAPACITY)

    def test_the_init_method(self):
        self.assertEqual(self.TRAIN_NAME, self.train.name)
        self.assertEqual(self.TRAIN_CAPACITY, self.train.capacity)
        self.assertListEqual([], self.train.passengers)

    def test_add_method__if_no_free_space__expect_to_raise(self):
        self.train = Train(self.TRAIN_NAME, self.TRAIN_CAPACITY_IF_IS_FULL)
        self.train.add(self.PASSENGER_NAME)

        with self.assertRaises(ValueError) as context:
            self.train.add(self.SECOND_PASSENGER_NAME)
        self.assertEqual("Train is full", str(context.exception))

    def test_add_method__if_passenger_in_passengers__expect_to_raise(self):
        self.train.add(self.PASSENGER_NAME)

        with self.assertRaises(ValueError) as context:
            self.train.add(self.PASSENGER_NAME)
        self.assertEqual(f"Passenger {self.PASSENGER_NAME} Exists", str(context.exception))

    def test_add_method__expect_the_passenger_to_be_added_succesfully(self):
        result = self.train.add(self.PASSENGER_NAME)
        self.assertEqual(f"Added passenger {self.PASSENGER_NAME}", result)
        self.assertListEqual([self.PASSENGER_NAME], self.train.passengers)

    def test_remove_method__if_passenger_name_not_in_passengers__expect_to_raise(self):
        with self.assertRaises(ValueError) as context:
            self.train.remove(self.PASSENGER_NAME)

        self.assertEqual("Passenger Not Found", str(context.exception))

    def test_remove_method__if_passenger_name_is_valid__expect_empty_passengers_list(self):
        self.train.passengers = [self.PASSENGER_NAME]
        result = self.train.remove(self.PASSENGER_NAME)
        self.assertEqual(f"Removed {self.PASSENGER_NAME}", result)
        self.assertListEqual([], self.train.passengers)


if __name__ == '__main__':
    main()
