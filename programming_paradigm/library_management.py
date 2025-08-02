# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if self._is_checked_out:
            return False  # déjà emprunté
        self._is_checked_out = True
        return True

    def return_book(self):
        if not self._is_checked_out:
            return False  # n'était pas emprunté
        self._is_checked_out = False
        return True

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book instances can be added.")
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                success = book.check_out()
                if not success:
                    print(f"'{title}' is already checked out.")
                return
        print(f"Book titled '{title}' not found in library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                success = book.return_book()
                if not success:
                    print(f"'{title}' was not checked out.")
                return
        print(f"Book titled '{title}' not found in library.")

    def list_available_books(self):
        available = [book for book in self._books if book.is_available()]
        if not available:
            print("No available books.")
            return
        for book in available:
            print(str(book))
