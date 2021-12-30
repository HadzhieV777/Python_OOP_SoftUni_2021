from project.library import Library

from unittest import TestCase, main

class Test(TestCase):
    LIBRARY_NAME = 'Valid Name'
    INVALID_NAME = ''
    BOOK_TITLE = "Book"
    AUTHOR_NAME = "Author"
    READER_NAME = "Reader"

    def setUp(self) -> None:
        self.library = Library(self.LIBRARY_NAME)

    def test_init__expect_success(self):
        self.assertEqual(self.LIBRARY_NAME, self.library.name)
        self.assertDictEqual({}, self.library.books_by_authors)
        self.assertDictEqual({}, self.library.readers)

    def test_name_setter__with_invalid_value__expect_to_raise(self):
        with self.assertRaises(ValueError) as context:
            self.library = Library(self.INVALID_NAME)

        expected = "Name cannot be empty string!"
        self.assertEqual(expected, str(context.exception))

    def test_add_book__expect_success(self):
        self.assertDictEqual({}, self.library.books_by_authors)
        self.library.add_book(self.AUTHOR_NAME, self.BOOK_TITLE)

        expected = {self.AUTHOR_NAME: [self.BOOK_TITLE]}
        self.assertEqual(expected, self.library.books_by_authors)

        self.library.add_book(self.AUTHOR_NAME, 'Another title')
        expected = {self.AUTHOR_NAME: [self.BOOK_TITLE, 'Another title']}
        self.assertEqual(expected, self.library.books_by_authors)

    def test_add_reader__expect_success(self):
        self.assertDictEqual({}, self.library.readers)
        self.library.add_reader(self.READER_NAME)
        expected = {self.READER_NAME: []}
        self.assertEqual(expected, self.library.readers)

        result = self.library.add_reader(self.READER_NAME)
        expected = f"{self.READER_NAME} is already registered in the {self.LIBRARY_NAME} library."
        self.assertEqual(result, expected)

    def test_rent_book__with_invalid_inputs__expect_error(self):
        # if reader_name not in readers
        expected = f"{self.READER_NAME} is not registered in the {self.LIBRARY_NAME} Library."
        result = self.library.rent_book(self.READER_NAME, self.AUTHOR_NAME, self.BOOK_TITLE)
        self.assertEqual(expected, result)

        # if book_author not in books_by_authors
        self.library.add_reader(self.READER_NAME)
        expected = f"{self.LIBRARY_NAME} Library does not have any {self.AUTHOR_NAME}'s books."
        result = self.library.rent_book(self.READER_NAME, self.AUTHOR_NAME, self.BOOK_TITLE)
        self.assertEqual(expected, result)

        self.library.add_book(self.AUTHOR_NAME, 'Another title')
        expected = f"""{self.LIBRARY_NAME} Library does not have {self.AUTHOR_NAME}'s "{self.BOOK_TITLE}"."""
        result = self.library.rent_book(self.READER_NAME, self.AUTHOR_NAME, self.BOOK_TITLE)
        self.assertEqual(expected, result)

    def test_rent_book_should_properly_rent_book(self):
        self.assertDictEqual({}, self.library.readers)
        self.assertDictEqual({}, self.library.books_by_authors)
        self.library.add_reader(self.READER_NAME)
        self.library.add_book(self.AUTHOR_NAME, self.BOOK_TITLE)
        self.library.add_book(self.AUTHOR_NAME, 'Another title')

        self.library.rent_book(self.READER_NAME, self.AUTHOR_NAME, self.BOOK_TITLE)

        self.assertEqual([{self.AUTHOR_NAME: self.BOOK_TITLE}], self.library.readers[self.READER_NAME])
        self.assertEqual(1, len(self.library.books_by_authors[self.AUTHOR_NAME]))
        self.assertTrue(self.BOOK_TITLE not in self.library.books_by_authors[self.AUTHOR_NAME])
        self.assertTrue('Another title' in self.library.books_by_authors[self.AUTHOR_NAME])




if __name__ == '__main__':
    main()