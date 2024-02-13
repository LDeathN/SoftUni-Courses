from project.bookstore import Bookstore
from unittest import TestCase


class TestBookStore(TestCase):
    def test_constructor(self):
        Store = Bookstore(300)
        self.assertEqual(Store.books_limit, 300)
        self.assertEqual(Store.total_sold_books, 0)
        self.assertEqual(Store.availability_in_store_by_book_titles, {})
        with self.assertRaises(ValueError) as ve:
            Store2 = Bookstore(-150)
        self.assertEqual(str(ve.exception), "Books limit of -150 is not valid")
        with self.assertRaises(ValueError) as ve:
            Store3 = Bookstore(0)
        self.assertEqual(str(ve.exception), "Books limit of 0 is not valid")

    def test_len_method(self):
        Store = Bookstore(400)
        result = Store.__len__()
        self.assertEqual(result, 0)
        Store.receive_book("Harry Potter", 50)
        Store.receive_book("Book", 20)
        result2 = Store.__len__()
        self.assertEqual(result2, 70)


    def test_receive_book_case1(self):
        Store = Bookstore(300)
        message = Store.receive_book("Harry Potter", 100)
        self.assertEqual(len(Store), 100)
        self.assertEqual(message, "100 copies of Harry Potter are available in the bookstore.")
        self.assertEqual(Store.availability_in_store_by_book_titles, {"Harry Potter": 100})
        Store.receive_book("Game of thrones", 100)
        message2 = Store.receive_book("Harry Potter", 100)
        self.assertEqual(message2, "200 copies of Harry Potter are available in the bookstore.")
        self.assertEqual(Store.availability_in_store_by_book_titles, {"Harry Potter": 200, "Game of thrones": 100})

    def test_receive_book_case2(self):
        Store = Bookstore(300)
        Store.receive_book("Harry Potter", 100)
        with self.assertRaises(Exception) as ve:
            Store.receive_book("Manipulation", 250)
        self.assertEqual(str(ve.exception), "Books limit is reached. Cannot receive more books!")

    def test_sell_book_case1(self):
        Store = Bookstore(500)
        Store.receive_book("Harry Potter", 100)
        Store.receive_book("Game of thrones", 100)
        Store.receive_book("Manipulation", 100)
        message = Store.sell_book("Game of thrones", 50)
        self.assertEqual(message, "Sold 50 copies of Game of thrones")
        self.assertEqual(Store.availability_in_store_by_book_titles, {"Harry Potter": 100, "Game of thrones": 50, "Manipulation": 100})
        self.assertEqual(len(Store), 250)
        self.assertEqual(Store.total_sold_books, 50)
        Store.sell_book("Game of thrones", 50)
        Store.sell_book("Harry Potter", 100)
        Store.sell_book("Manipulation", 100)
        self.assertEqual(Store.availability_in_store_by_book_titles, {'Game of thrones': 0, 'Harry Potter': 0, 'Manipulation': 0})
        self.assertEqual(Store.total_sold_books, 300)
        self.assertEqual(len(Store), 0)

    def test_sell_book_case2(self):
        Store = Bookstore(500)
        Store.receive_book("Harry Potter", 100)
        Store.receive_book("Game of thrones", 100)
        Store.receive_book("Manipulation", 100)
        with self.assertRaises(Exception) as e:
            Store.sell_book("Dark Souls", 100)
        self.assertEqual(str(e.exception), "Book Dark Souls doesn't exist!")
        with self.assertRaises(Exception) as e:
            Store.sell_book("Manipulation", 200)
        self.assertEqual(str(e.exception), "Manipulation has not enough copies to sell. Left: 100")

    def test_str_method(self):
        Store = Bookstore(500)
        Store.receive_book("Harry Potter", 100)
        Store.receive_book("Game of thrones", 100)
        Store.receive_book("Manipulation", 100)
        Store.sell_book("Harry Potter", 50)
        Store.sell_book("Game of thrones", 100)
        result = Store.__str__()
        actual = ["Total sold books: 150"]
        actual.append("Current availability: 150")
        actual.append(" - Harry Potter: 50 copies")
        actual.append(" - Game of thrones: 0 copies")
        actual.append(" - Manipulation: 100 copies")
        actual = "\n".join(actual)
        self.assertEqual(result, actual)
        Store2 = Bookstore(500)
        result2 = Store2.__str__()
        actual2 = ["Total sold books: 0"]
        actual2.append("Current availability: 0")
        actual2 = "\n".join(actual2)
        self.assertEqual(result2, actual2)


