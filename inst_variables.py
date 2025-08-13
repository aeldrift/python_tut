# Instance Variabkes And class variables 
# Example for Instance vs class:

class Car:
    def __init__(self, brand):
        self.brand = brand  # instance variable

car1 = Car("Toyota")   # Instance 1
car2 = Car("Tesla")    # Instance 2

print(car1.brand)  # Toyota
print(car2.brand)  # Tesla