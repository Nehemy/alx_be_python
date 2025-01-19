class Book:
    
    def __init__(self, title, author):
        self._is_checked_out = False
        self.title = title
        self.author = author
        
class Library:
    def __init__(self):
        self._books = []
        
    
    def add_book(self, book):
        self._books.append(book)
        for book in self._books:
            if book._is_checked_out == False:
                print(f"Available books after setup:\n{book.title} by {book.author}")
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out = True
                print(f"Available books after checking out '{book.title}':\n{book.title} by {book.author}")
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out = False
                print(f"Available books after returning '{book.title}':\n{book.title} by {book.author}")


    def list_available_books(self):
        for book in self._books:
            if book._is_checked_out == False:
                print(f"Available books after checking out {book.title}:\n{book.title} by {book.author}")