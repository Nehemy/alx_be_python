class Book:
    
    def __init__(self, title, author):
        self._is_checked_out = False
        self._title = title
        self._author = author
        
class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self, Book):
        pass
    
    def return_book(self, book):
        pass
        
    def check_out_book(title):
        pass
    
    def list_available_books(self):
        return self._books