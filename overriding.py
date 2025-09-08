# Overriding: 
''' Method overriding in Python occurs when a child (subclass) defines a method with the same name and 
parameters as a method in its parent (superclass). When the method is called on a subclass object, the 
subclass’s version is executed, replacing (overriding) the parent’s implementation.'''

# Example:

class Parent:
    def show(self):
        print("I am a parent class")
class Child(Parent):
    def show(self):
        print("I am a child class")
obj = Child()
obj.show()  # Output: I am a child class (method override)


# If the method is not found in the subclass, Python looks for it in the parent class.
# Example:
class A:
    def display(self):
        print("Class A method")
class B(A):
    pass
obj = B()
obj.display()  # Output: Class A method (inherited from parent class)


# Some imp operations using issubclass() function:

# issubclass(): Returns True if class1 is a subclass of class2
print(issubclass(A, B))  # False, because A is not a subclass of B
print(issubclass(B, A))  # True, because B is a subclass of A
print(issubclass(B, object))  # True, because all classes inherit from object



# At runtime, @override does nothing — but it helps catch mistakes early during static analysis.
# This is only for static type checkers (like mypy, pyright), not for runtime.

# Example:
from typing import override

class Animal:
    def sound(self) -> None:
        print("Animal's sound")

class Dog(Animal):
    @override
    def sound(self) -> None:   # correct override
        super().sound()
        print("Bark")  # The -> None indicates the return type of the function.
                       # None means the function does not return anything (or returns None implicitly).

d = Dog()
d.sound()  # Animal's sound 
           # Bark

# Example:

# Parent class
class Animal:
    def sound(self):
        print("Animals make different sounds")

# Child class (overrides sound())
class Dog(Animal):
    def sound(self):
        print("Dog barks: Woof! Woof!")

# Another child class (overrides sound())
class Cat(Animal):
    def sound(self):
        print("Cat meows: Meow! Meow!")

# Demonstration
a = Animal()
a.sound()   # Output: Animals make different sounds

d = Dog()
d.sound()   # Output: Dog barks: Woof! Woof!
