class Book:
    def __init__(self, title, author):
        """Initialize base book attributes"""
        self.title = title
        self.author = author
    
    def __str__(self):
        """Common string representation for all books"""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize eBook with additional file_size"""
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        """String representation for eBook"""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize print book with additional page_count"""
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """String representation for print book"""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        """Initialize library with empty book list"""
        self.books = []
    
    def add_book(self, book):
        """Add a book to the library"""
        self.books.append(book)
    
    def list_books(self):
        """Print details of all books in library"""
        for book in self.books:
            print(book)
