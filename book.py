class Book:
    def __init__(self, book_id, title, author):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._is_available = True

    def borrow(self):
        self._is_available = False
    @property
    def is_available(self):
        return self._is_available

    def return_book(self):
        self._is_available = True
    

    @property
    def book_id(self):
        return self._book_id

    def display_info(self):
        print(f"{self._book_id} | {self._title} | {self._author} | Available: {self._is_available}")