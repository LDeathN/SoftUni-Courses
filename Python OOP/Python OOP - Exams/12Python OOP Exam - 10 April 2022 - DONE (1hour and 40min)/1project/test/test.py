from project.movie import Movie
from unittest import TestCase


class TestMovie(TestCase):
    def test_constructor(self):
        Movie1 = Movie("The Matrix", 1999, 8.7)
        self.assertEqual(Movie1.name, "The Matrix")
        self.assertEqual(Movie1.year, 1999)
        self.assertEqual(Movie1.rating, 8.7)
        Movie2 = Movie("Made up", 1887, 8.0)
        self.assertEqual(Movie2.name, "Made up")
        self.assertEqual(Movie2.year, 1887)
        self.assertEqual(Movie2.rating, 8.0)
        with self.assertRaises(ValueError) as ve:
            Movie("Error", 1500, 9)
        self.assertEqual(str(ve.exception), "Year is not valid!")
        with self.assertRaises(ValueError) as ve2:
            Movie("", 1900, 7)
        self.assertEqual(str(ve2.exception), "Name cannot be an empty string!")

    def test_add_actor_case1(self):
        Movie1 = Movie("The Matrix", 1999, 8.7)
        Movie1.add_actor("Me")
        self.assertEqual(Movie1.actors, ["Me"])
        Movie1.add_actor("You")
        Movie1.add_actor("")
        self.assertEqual(Movie1.actors, ["Me", "You", ""])
        message = Movie1.add_actor("You")
        self.assertEqual(message, "You is already added in the list of actors!")

    def test_gt_method(self):
        Movie1 = Movie("The Matrix", 1999, 8.7)
        Movie2 = Movie("Made up", 1887, 8.0)
        message = Movie1.__gt__(Movie2)
        self.assertEqual(message, '"The Matrix" is better than "Made up"')
        message2 = Movie2.__gt__(Movie1)
        self.assertEqual(message2, '"The Matrix" is better than "Made up"')

    def test_repr_method_case1(self):
        Movie1 = Movie("The Matrix", 1999, 8.7)
        Movie2 = Movie("Made up", 1887, 8.0)
        self.assertEqual(Movie1.__repr__(), "Name: The Matrix\nYear of Release: 1999\nRating: 8.70\nCast: ")
        self.assertEqual(Movie2.__repr__(), "Name: Made up\nYear of Release: 1887\nRating: 8.00\nCast: ")
        Movie1.add_actor("Me")
        Movie1.add_actor("You")
        Movie1.add_actor("")
        self.assertEqual(Movie1.__repr__(), "Name: The Matrix\nYear of Release: 1999\nRating: 8.70\nCast: Me, You, ")

        