# issubclass(): Returns True if class1 is a subclass of class2

# Example:
class Animal:
    pass

class Dog(Animal):
    pass

print(issubclass(Dog, Animal)) 
# print(issubclass(Animal, Dog)) # False, because Animal is not a subclass of Dog    

print(issubclass(Dog, object))     # (All classes inherit from object)



