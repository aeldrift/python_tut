# MRO: Method Resolution Order
''' this is the oredr in which python looks for a method or attribute when you call it on an object. especially when multiple inheritance is innvolved.'''
# example:
class A:
    def show(self):
        print("Class A")

class B(A):
    pass

obj = B()
obj.show()  # expected output: Class A 
''' reason: B inherits from A, so it can access A's methods. Python looks first in:
Class B and then in class A'''


# IN CASE IF HYBRID INHERITANCE:

class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):
    pass

obj = D()
obj.greet()  # expected output: Hello from B

''' D → B → C → A → object

Since B comes before C in the class declaration class D(B, C), Python finds the method greet() in B first and stops there. '''
