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


