# Introspection

'''Ability of a program to examine the type and properties of an object at runtime.

Simply: "Looking inside an object while the program is running."

Useful for debugging, checking attributes/methods, and building flexible programs. '''

# Its Functions are: 

# 1. dir(obj)	List of all attributes & methods '''
# example: 

x = [1, 2, 3]
print(dir(x))   # shows all methods/attributes of list

# 2. __dict__	Instance variables in dict form
# example:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1

p = Person("John", 30)
print(p.__dict__)
# Output: {'name': 'John', 'age': 30, 'version': 1}

#3. help(obj)	Documentation/help info 
# example:

