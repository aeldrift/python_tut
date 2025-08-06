# Creating a simple inherited program. 

class Vehicle:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
        
    def drive(self):
        print("Driving at", self.speed, "kmph!")

class Car(Vehicle):  # Car inherits from Vehicle
    def honk(self):
        print("Beep Beep!!")
        
my_car = Car("Red", 100)
my_car.drive()
my_car.honk()

# Using super()

class Animal:
    def make_sound(self):
        print("Some animal sound")

class Dog(Animal):
    def make_sound(self):
        super().make_sound()  # call parent method
        print("Woof!!")

d = Dog()
d.make_sound()

# Practice Question:

''' Create a program with two classes:

1. Class: Person

Method: introduce()
→ Prints: "Hello, I am a person."



2. Class: Student (inherits from Person)

Method: introduce()
→ Use super() to call the parent class method first.
→ Then print: "I am also a student." '''

class Person():
    def introduce(self):
        print("Hello, I am a person")

class Student(Person):
    def introduce(self):
        super().introduce()
        print("I am also a student")

result = Student()
result.introduce()

# Practice Question:

''' Write two classes:
1️⃣ A base class Animal with:

An __init__() method that takes name as a parameter and stores it as an attribute.

A make_sound() method that prints "<name> makes a sound.".


2️⃣ A derived class Dog that inherits from Animal with:

An __init__() method that calls the parent’s __init__() (using super()) and also stores an extra attribute breed.

A make_sound() method that overrides the parent’s method and prints "<name> barks.", but also calls the parent’s make_sound() first.


Finally, create a Dog object with name "Buddy" and breed "Golden Retriever", and call make_sound() on it.'''

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} makes sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)       # call Animal's constructor with name
        self.breed = breed           # initialize Dog-specific attribute

    def make_sound(self):
        print(f"{self.name} barks")

cout = Dog("Buddy", "Golden Retriever")
cout.make_sound() 
 # expected output: Buddy barks

# SINGLE INHERITANCE

# example:
class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor called")

    def greet(self):
        print(f"Hello, I am {self.name}")

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)  # This runs Person's __init__
        self.student_id = student_id
        print("Student constructor called")

    def show_id(self):
        print(f"My ID is {self.student_id}")
