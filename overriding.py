# OVERRIDING: In this, method greet() in the child that has the same name as the parent’s method.
# Example1:

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):  # same method name as in Parent
        print("Hello from Child")

c=Child()
c.greet()  # This will call the Child's greet method
           # expected output: Hello from Child

# example2:
class Parent:
    def show(self):
        print("Parent class method")

class Child1(Parent):
    def show(self):   # overridden
        print("Child1 class overrides Parent")

class Child2(Parent):
    pass  #it tells p that do nothing here, just continue

c1 = Child1()
c2 = Child2()

c1.show()   # Uses Child1's override
c2.show()   # Uses Parent's method (no override is there)

# expected output:
'''Child1 class overrides Parent
Parent class method '''