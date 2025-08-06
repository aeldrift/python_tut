# OVERRIDING: In this, method greet() in the child that has the same name as the parent’s method.
# Example:

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):  # same method name as in Parent
        print("Hello from Child")

c=Child()
c.greet()  # This will call the Child's greet method