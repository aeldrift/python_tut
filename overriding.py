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