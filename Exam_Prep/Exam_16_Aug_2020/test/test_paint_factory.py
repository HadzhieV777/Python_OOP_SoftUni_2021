from project.factory.paint_factory import PaintFactory
from unittest import TestCase, main


class Test(TestCase):
    VALID_NAME = 'Valid Name'
    CAPACITY = 5
    VALID_COLOR = "blue"
    INVALID_COLOR = 'invalid color'
    VALID_INGREDIENTS = ["white", "yellow", "blue", "green", "red"]

    def setUp(self) -> None:
        self.paint_factory = PaintFactory(self.VALID_NAME, self.CAPACITY)

    def test_init_method__expect_success(self):
        self.assertEqual(self.VALID_NAME, self.paint_factory.name)
        self.assertEqual(self.CAPACITY, self.paint_factory.capacity)
        self.assertDictEqual({}, self.paint_factory.ingredients)
        self.assertListEqual(self.VALID_INGREDIENTS, self.paint_factory.valid_ingredients)

    def test_if_all_abstract_methods_are_available(self):
        self.assertTrue('__init__' in dir(PaintFactory))
        self.assertTrue('add_ingredient' in dir(PaintFactory))
        self.assertTrue('remove_ingredient' in dir(PaintFactory))
        self.assertTrue('can_add' in dir(PaintFactory))

    def test_the_product_property(self):
        result = self.paint_factory.products
        expected = self.paint_factory.ingredients
        self.assertEqual(expected, result)

    def test_add_ingredient__invalid_product_type__expect_to_raise(self):
        with self.assertRaises(TypeError) as context:
            self.paint_factory.add_ingredient(self.INVALID_COLOR, self.CAPACITY)

        self.assertEqual(f"Ingredient of type {self.INVALID_COLOR} not allowed in PaintFactory", str(context.exception))

    def test_add_ingredient__valid_product_type_no_space__expect_to_raise(self):
        self.paint_factory.add_ingredient(self.VALID_COLOR, self.CAPACITY)
        expected = {self.VALID_COLOR: self.CAPACITY}
        result = self.paint_factory.ingredients
        self.assertDictEqual(expected, result)

        with self.assertRaises(ValueError) as context:
            self.paint_factory.add_ingredient('white', self.CAPACITY)

        self.assertEqual("Not enough space in factory", str(context.exception))

    def test_remove_ingredient__with_negative_quantity__expect_to_raise(self):
        self.paint_factory.add_ingredient(self.VALID_COLOR, self.CAPACITY)
        self.paint_factory.remove_ingredient(self.VALID_COLOR, 2)
        expected = {self.VALID_COLOR: 3}
        result = self.paint_factory.ingredients
        self.assertEqual(expected, result)

        with self.assertRaises(ValueError) as context:
            self.paint_factory.remove_ingredient(self.VALID_COLOR, self.CAPACITY)

        self.assertEqual("Ingredients quantity cannot be less than zero", str(context.exception))

    def test_remove_ingredient__with_invalid_ingredient__expect_to_raise(self):
        self.assertDictEqual({}, self.paint_factory.ingredients)
        with self.assertRaises(KeyError) as context:
            self.paint_factory.remove_ingredient(self.VALID_COLOR, self.CAPACITY)

        self.assertEqual(f"'No such ingredient in the factory'", str(context.exception))

    def test_can_add__expect_success(self):
        self.assertTrue(self.paint_factory.can_add(self.CAPACITY))
        self.paint_factory.add_ingredient(self.VALID_COLOR, self.CAPACITY)
        self.assertFalse(self.paint_factory.can_add(self.CAPACITY))

    def test_repr_method_expect_succcess(self):
        result = repr(self.paint_factory)
        expected = f"Factory name: {self.VALID_NAME} with capacity {self.CAPACITY}.\n"
        self.assertEqual(result, expected)
        self.paint_factory.add_ingredient(self.VALID_COLOR, self.CAPACITY)
        result = repr(self.paint_factory)
        expected = f"Factory name: {self.VALID_NAME} with capacity {self.CAPACITY}.\n"\
            f"{self.VALID_COLOR}: {self.CAPACITY}\n"
        self.assertEqual(result, expected)



if __name__ == '__main__':
    main()
