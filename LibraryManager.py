from collections import defaultdict
import json

class LibraryManager:
    def __init__(self):
        self.library = defaultdict(int)
        self.borrow_book = defaultdict(int)

    def add_book(self, book_name, stock):
        self.library[book_name] += stock
        return f"Add book - {book_name}({stock})"

    def borrow_book(self, book_name, amount):
        if self.library[book_name] < amount:
            return f"{book_name}: Not enough stock for borrow."

        self.library[book_name] -= amount
        self.borrow_book[book_name] += amount

        return f"Borrowed - {amount}: {book_name}"

    def return_book(self, book_name, amount):
        if book_name not in self.borrow_book or self.borrow_book[book_name] < amount:
            return f"Cannot return more than borrowed for {book_name}"

        self.library[book_name] += amount
        self.borrow_book[book_name] -= amount

        if self.borrow_book[book_name] == 0:
            del self.borrow_book[book_name]

        return f"Return {book_name}: {amount}"

    def show_library_report(self):
        return dict(self.library)

    def show_borrow_report(self):
        return dict(self.borrow_book)

    def save_data(self):
        with open("library.json", "w") as file:
            json.dump({
                "library": dict(self.library),
                "borrow_book": dict(self.borrow_book)
            }, file)

    def load_data(self):
        try:
            with open("library.json", "r") as file:
                data = json.load(file)
                self.library = defaultdict(int, data.get("library", {}))
                self.borrow_book = defaultdict(int, data.get("borrow_book", {}))
        except FileNotFoundError:
            self.library = defaultdict(int)
            self.borrow_book = defaultdict(int)