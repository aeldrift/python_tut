# practice Question : Make a libray Management System for the books being checkout out or not.

class LibraryBook:
    library_name = "Central City Library"

    def __init__(self, title, author, is_checked_out=False):
        self.title = title
        self.author = author
        self.is_checked_out = is_checked_out

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"Book '{self.title}' checked out from {LibraryBook.library_name}")
        else:
            print(f"Book '{self.title}' is already checked out.")
            
    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"Book '{self.title}' returned to {LibraryBook.library_name}")
        else:
            print(f"Book '{self.title}' was not checked out.")

# Create a book instance
book1 = LibraryBook("1984", "Justin")

# Test methods
book1.check_out()     # Should check out the book
book1.check_out()     # Should warn that it's already checked out
book1.return_book()   # Should return the book
book1.return_book()   # Should warn it wasn't checked out

# Expected output:
''' Book '1984' checked out from Central City Library
Book '1984' is already checked out.
Book '1984' returned to Central City Library
Book '1984' was not checked out. '''


