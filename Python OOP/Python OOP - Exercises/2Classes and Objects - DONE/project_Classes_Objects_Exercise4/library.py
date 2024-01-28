from project.user import User

class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)
            if user.username not in self.rented_books.keys():
                self.rented_books[user.username] = {}
            self.rented_books[user.username].update({book_name: days_to_return})
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for username, data in self.rented_books.items():
            for b_n, days in data.items():
                if b_n == book_name:
                    return f"The book \"{book_name}\" " \
                           f"is already rented and will be available in " \
                           f"{days} days!"

    def return_book(self, author, book_name, user):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"
        if author not in self.books_available:
            self.books_available[author] = []
        self.books_available[author].append(book_name)
        self.rented_books[user.username].pop(book_name)
        user.books.remove(book_name)

















