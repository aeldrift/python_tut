# Task
''' Create a Book class that manages a book's title, author, and price. Implement the following:  
A constructor to initialize the title, author, and price of the book.
Getter methods for title, author, and price.
Setter methods for:
title and author (ensure the title and author are non-empty strings).
price (ensure the price is non-negative).
A method discount that applies a discount (a percentage between 0 and 100) to the price.'''

class Book:
    def __init__(self, title, author, price):
        self._title = title
        self._author = author
        self._price = price
        
    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @property
    def price(self):
        return self._price
        
    @title.setter
    def title(self, title_value):
        if not isinstance(title_value, str) or not title_value:
            print("Title is required and must be a string.")
        else:
            self._title = title_value
            
    @author.setter
    def author(self, author_value):
        if not isinstance(author_value, str) or not author_value:
            print("Author is required and must be a string.")
        else:
            self._author = author_value
            
    @price.setter
    def price(self, price_value):
        if price_value < 0:
            print("Invalid price. Price cannot be negative.")
        else:
            self._price = price_value

    def apply_discount(self, discount_percentage):
        if 0 <= discount_percentage <= 100:
            discount = self._price * (discount_percentage / 100)
            self._price -= discount
        else:
            print("Invalid discount percentage. It should be between 0 and 100.")
            
title_input = input("Enter book title: ")   # Create a Book object with user input
author_input = input("Enter book author: ")
while True:
    try:
        price_input = float(input("Enter book price: "))
        if price_input < 0:
            print("Price can't be negative.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid price.")

# Create the book object
book = Book(title_input, author_input, price_input)

print(f"Current book details:\nTitle: {book.title}\nAuthor: {book.author}\nPrice: {book.price}")  # Display the current book details

discount_input = float(input("Enter discount percentage: "))  # Apply discount based on user input
book.apply_discount(discount_input)

print(f"Final book details after applying discount:\nTitle: {book.title}\nAuthor: {book.author}\nPrice: {book.price}")  # Display final details after discount

# EXPECTED OUTPUT:
'''
Enter book title: vg
Enter book author: hbh
Enter book price: h
Invalid input. Please enter a valid price.
Enter book price: i
Invalid input. Please enter a valid price.
Enter book price: k
Invalid input. Please enter a valid price.
Enter book price: 89
Current book details:
Title: vg
Author: hbh
Price: 89.0
Enter discount percentage: 50
Final book details after applying discount:
Title: vg
Author: hbh
Price: 44.5 '''


