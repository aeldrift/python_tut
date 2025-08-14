# PRACTISE QUESTION

''' Write a library class with no_of_books and books as two instance variables.  
write a program to create a library from this library class and show you can 
print all books, add a bookand get a number of books using different methods. 
Show that your program dosen't presist the books after the program is stopped! '''

class Library:
    def __init__(self):
        self.books = []  # List to store book names
        self.no_of_books = 0  # Count of books

    def add_book(self, book_name):
        self.books.append(book_name)
        self.no_of_books += 1

    def print_books(self):
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("No books in the library.")

    def get_no_of_books(self):
        return self.no_of_books
# library instance
my_library = Library()

# Add books to the library
my_library.add_book("1984")
my_library.add_book("The Alchemist")
my_library.add_book("Python Basics")

# Print all books
my_library.print_books()

# Print number of books
print("Number of books:", my_library.get_no_of_books())

# Expected output: 
''' Books in the library:
- 1984
- The Alchemist
- Python Basics
Number of books: 3 '''
