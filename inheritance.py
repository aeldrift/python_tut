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