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
# memory address where instance is stored.