from project.pet_shop import PetShop

from unittest import TestCase, main


class Test(TestCase):
    VALID_NAME = "Name"

    def setUp(self) -> None:
        self.pet_shop = PetShop(self.VALID_NAME)

    def test_the_init_method__expect_success(self):
        self.assertEqual(self.VALID_NAME, self.pet_shop.name)
        self.assertDictEqual({}, self.pet_shop.food)
        self.assertListEqual([], self.pet_shop.pets)

    def test_add_food__with_invalid_quantity__expect_to_raise(self):
        invalid_quantity = 0
        self.assertDictEqual({}, self.pet_shop.food)
        with self.assertRaises(ValueError) as context:
            self.pet_shop.add_food(self.VALID_NAME, invalid_quantity)

        expected = 'Quantity cannot be equal to or less than 0'
        self.assertEqual(expected, str(context.exception))

    def test_add_food__happy_case(self):
        # if name not in food
        valid_quantity = 2
        self.assertDictEqual({}, self.pet_shop.food)
        self.pet_shop.add_food(self.VALID_NAME, valid_quantity)
        expected = {self.VALID_NAME: valid_quantity}
        self.assertEqual(expected, self.pet_shop.food)
        self.assertEqual(valid_quantity, self.pet_shop.food[self.VALID_NAME])

        # if name already in food
        self.pet_shop.add_food(self.VALID_NAME, valid_quantity)
        expected = {self.VALID_NAME: valid_quantity * 2}
        self.assertEqual(expected, self.pet_shop.food)
        self.assertEqual(valid_quantity * 2, self.pet_shop.food[self.VALID_NAME])

        # test the message
        expected = f"Successfully added {valid_quantity:.2f} grams of {self.VALID_NAME}."
        result = self.pet_shop.add_food(self.VALID_NAME, valid_quantity)
        self.assertEqual(expected, result)

    def test_add_pet__when_pet_not_in_petshop__expect_to_add_it_and_correct_message(self):
        result = self.pet_shop.add_pet(self.VALID_NAME)

        self.assertListEqual([self.VALID_NAME], self.pet_shop.pets)
        self.assertEqual(
            f'Successfully added {self.VALID_NAME}.',
            result
        )

    def test_add_pet(self):
        # if pet not in pets
        self.assertListEqual([], self.pet_shop.pets)
        self.pet_shop.add_pet(self.VALID_NAME)
        expected = [self.VALID_NAME]
        self.assertEqual(expected, self.pet_shop.pets)

        # if pet already in pets
        with self.assertRaises(Exception) as context:
            self.pet_shop.add_pet(self.VALID_NAME)
        expected = "Cannot add a pet with the same name"
        self.assertEqual(expected, str(context.exception))

    def test_feed_pet__if_pet_not_in_pets__expect_to_raise(self):
        food_name = 'Food'
        self.assertListEqual([], self.pet_shop.pets)

        with self.assertRaises(Exception) as context:
            self.pet_shop.feed_pet(self.VALID_NAME, food_name)
        expected = "Please insert a valid pet name"
        self.assertEqual(expected, str(context.exception))

    def test_feed_pet__if_food_not_in_food__expect_to_raise(self):
        food_name = 'Food'
        self.pet_shop.add_pet(self.VALID_NAME)
        expected = [self.VALID_NAME]
        self.assertEqual(expected, self.pet_shop.pets)

        self.assertDictEqual({}, self.pet_shop.food)
        result = self.pet_shop.feed_pet(food_name, self.VALID_NAME)
        expected = f'You do not have {food_name}'
        self.assertEqual(expected, result)

    def test_feed_pet__when_food_is_99__expect_to_increase_by_1000_and_correct_message(self):
        food_name = 'Food'
        quantity = 99
        self.pet_shop.add_pet(self.VALID_NAME)
        self.pet_shop.add_food(food_name, quantity)

        result = self.pet_shop.feed_pet(food_name, self.VALID_NAME)

        self.assertEqual(
            quantity + 1000,
            self.pet_shop.food[food_name]
        )

        expected = "Adding food..."
        self.assertEqual(expected, result)

    def test_feed_pet__when_food_is_above_100__expect_to_decrease_by_100_and_correct_message(self):
        food_name = 'Food'
        quantity = 103
        self.pet_shop.add_pet(self.VALID_NAME)
        self.pet_shop.add_food(food_name, quantity)

        result = self.pet_shop.feed_pet(food_name, self.VALID_NAME)
        self.assertEqual(
            quantity - 100,
            self.pet_shop.food[food_name]
        )

        expected = f"{self.VALID_NAME} was successfully fed"
        self.assertEqual(expected, result)

    def test_the_repr_method__expect_success(self):
        another_animal = "Animal"
        # with no animals
        expected = f'''Shop {self.VALID_NAME}:
Pets: '''
        result = repr(self.pet_shop)
        self.assertEqual(expected, result)

        # with one animal
        self.pet_shop.add_pet(self.VALID_NAME)
        expected = f'''Shop {self.VALID_NAME}:
Pets: {self.VALID_NAME}'''
        result = repr(self.pet_shop)
        self.assertEqual(expected, result)

        # with two animals
        self.pet_shop.add_pet(another_animal)
        expected = f'''Shop {self.VALID_NAME}:
Pets: {self.VALID_NAME}, {another_animal}'''
        result = repr(self.pet_shop)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
