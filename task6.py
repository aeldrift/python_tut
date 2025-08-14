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

