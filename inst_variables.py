# Instance Variabkes And class variables 
# Example for Instance vs class:

class Car:
    def __init__(self, brand):
        self.brand = brand  # instance variable

car1 = Car("Toyota")   # Instance 1
car2 = Car("Tesla")    # Instance 2

print(car1.brand)  # Toyota
print(car2.brand)  # Tesla

# Instance variable:

class Person:
    def __init__(self, name, age):
        self.name = name    # instance variable
        self.age = age      # instance variable

p1 = Person("Alice", 25)
print(p1.name)  # Alice
print(p1.age)   # 25
print(p1) # <__main__.Person object at 0x15247e376cf0>
# 0x152....0>  is memory address where instance is stored.

# Example:  Class variables vs Instance variable:

class Employee:
    company = "TechCorp"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

e1 = Employee("Alice")
e2 = Employee("Bob")

print(e1.company)  # TechCorp
print(e2.company)  # TechCorp

Employee.company = "NewCorp"  #( changed for all instances)
print(e1.company)  # NewCorp 
print(e2.company)  # NewCorp

# To change INSTANCE ATTRIBUTE:

e2.company = "BMW"  #(to change instance attribute)
print(e2.company) # BMW

# Example for Magic method/ Dunder Method/ Double underscore Method:

# EXAMPLE WITH __str__ :

class Book:
    def __init__(self, title):
        self.title = title
    
    def __str__(self):
        return f"Book: {self.title}"

b1 = Book("Python")
print(b1)  # Book: Python

# EXAMPLE WITH __len__ :

class Book:
    def __init__(self, pages):
        self.pages = pages
    
    def len(self):
        return self.pages

b1 = Book(350)
print(len(b1))  # TypeError: object of type 'Book' has no len()

# But with __len__ :

class Book:
    def __init__(self, pages):
        self.pages = pages
    
    def __len__(self):
        return self.pages

b1 = Book(350)
print(len(b1))  # 350 

# INSTANCE IS DESTROYED: 
''' Before destruction, if you have a __del__ method (destructor), Python will call it. '''
class Person:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print(f"{self.name} is being destroyed")

p1 = Person("Alice")
del p1  # Calls __del__ before removing object from memory



