# PRACTISE QUESTION

''' Write a library class with no_of_books and books as two instance variables.  
write a program to create a library from this library class and show you can 
print all books, add a bookand get a number of books using different methods. 
Show that your program dosen't presist the books after the program is stopped! '''

        
class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0

    def add_book(self, book_name):
        self.books.append(book_name)
        self.no_of_books += 1

    def print_books(self):
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print(input(f"Book added:{book}"))
        else:
            print("No books in the library.")

    def get_no_of_books(self):
        return self.no_of_books


my_library = Library()

my_library.add_book()
my_library.add_book()

my_library.print_books()

print("Number of books:", my_library.get_no_of_books())
