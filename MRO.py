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