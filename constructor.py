# A decorator is a function that modifies the behavior of another function without changing its actual code.
# It's like wrapping one function inside another.

# Example:1 To create constructor
class Student:
    def __init__(self, n, age, g):
        print("I am a student")
        self.name = n
        self.age = age
        self.grade = g

    def info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}")



# Creating objects
a = Student("Alice", 20, "A")
b = Student("Meena", 19, "B")


# Calling methods
a.info()
b.info()

# Example:2 
class book:
    def __init__(self, title, author, price):
        
        self.title = title
        self.author = author
        self.price = price

    def get_details(self):
        print(f"tile: {self.title}\nauthir: {self.author}\nprice: {self.price}")
    def is_expensive(self):
        if self.price>500 :
            return "True"
        else:
            return "False"

# Creating objects
a = book("Biology", "ABC", 600)

# Calling methods
a.get_details()
a.is_expensive()

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Creating an object
rectangle1 = Rectangle(50, 20)

# Printing results
print("Area:", rectangle1.area())
print("Perimeter:", rectangle1.perimeter())

# Practice question: Create a constructor to print name using print_name method.

class My_class:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"Name is {self.name}")

a = My_class("Abas")
a.print_name()

# Output: Name is Abas