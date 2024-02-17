from project.library import Library
from unittest import TestCase


class TestLibrary(TestCase):
    def test_constructor(self):
        library1 = Library("Devin")
        self.assertEqual(library1.name, "Devin")
        self.assertEqual(library1.books_by_authors, {})
        self.assertEqual(library1.readers, {})
        with self.assertRaises(ValueError) as ve:
            Library("")
        self.assertEqual(str(ve.exception), "Name cannot be empty string!")

    def test_add_book_case1(self):
        library1 = Library("Devin")
        library1.add_book("Kaku", "Universe")
        self.assertEqual(library1.books_by_authors, {"Kaku": ["Universe"]})
        library1.add_book("Kaku", "The world")
        self.assertEqual(library1.books_by_authors, {"Kaku": ["Universe", "The world"]})
        library1.add_book("Vazov", "Pod igoto")
        self.assertEqual(library1.books_by_authors, {"Kaku": ["Universe", "The world"], "Vazov": ["Pod igoto"]})
        library1.add_book("Kaku", "The world")
        self.assertEqual(library1.books_by_authors, {"Kaku": ["Universe", "The world"], "Vazov": ["Pod igoto"]})

    def test_add_reader_case1(self):
        library1 = Library("Devin")
        library1.add_reader("Martin")
        self.assertEqual(library1.readers, {"Martin": []})
        library1.add_reader("Dani")
        self.assertEqual(library1.readers, {"Martin": [], "Dani": []})
        message = library1.add_reader("Martin")
        self.assertEqual(message, "Martin is already registered in the Devin library.")
        self.assertEqual(library1.readers, {"Martin": [], "Dani": []})

    def test_rent_book_case1(self):
        library1 = Library("Devin")
        library1.add_book("Kaku", "Universe")
        library1.add_book("Vazov", "Pod igoto")
        library1.add_book("Kaku", "The world")
        library1.add_reader("Martin")
        library1.add_reader("Dani")
        library1.rent_book("Martin", "Kaku", "Universe")
        self.assertEqual(library1.readers, {"Martin": [{"Kaku": "Universe"}], "Dani": []})
        self.assertEqual(library1.books_by_authors, {"Kaku": ["The world"], "Vazov": ["Pod igoto"]})
        library1.rent_book("Martin", "Kaku", "The world")
        self.assertEqual(library1.readers, {"Martin": [{"Kaku": "Universe"}, {"Kaku": "The world"}], "Dani": []})
        self.assertEqual(library1.books_by_authors, {"Kaku": [], "Vazov": ["Pod igoto"]})
        library1.rent_book("Dani", "Vazov", "Pod igoto")
        self.assertEqual(library1.readers, {"Martin": [{"Kaku": "Universe"}, {"Kaku": "The world"}], "Dani": [{"Vazov": "Pod igoto"}]})
        self.assertEqual(library1.books_by_authors, {"Kaku": [], "Vazov": []})

    def test_rent_book_case2(self):
        library1 = Library("Devin")
        library1.add_book("Kaku", "Universe")
        library1.add_book("Vazov", "Pod igoto")
        library1.add_book("Kaku", "The world")
        library1.add_reader("Martin")
        library1.add_reader("Dani")
        message1 = library1.rent_book("Peter", "Kaku", "Universe")
        message2 = library1.rent_book("Dani", "Botev", "Brata si")
        message3 = library1.rent_book("Martin", "Kaku", "Outside")
        self.assertEqual(message1, "Peter is not registered in the Devin Library.")
        self.assertEqual(message2, "Devin Library does not have any Botev's books.")
        self.assertEqual(message3, """Devin Library does not have Kaku's "Outside".""")

