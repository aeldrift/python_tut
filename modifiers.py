# Access Specifers or Access Modifiers

# Public Modifier:
# Example1:

class MyClass:
    def __init__(self):
        self.name = "Eliana"   # public variable

obj = MyClass()
print(obj.name)  # Eliana

# Example2:

class Student:
    def __init__(self):
        self.college="MMDU"
obj=Student()
print(obj.college. # MM(DU)

# EXAMPLE: public, private, protected:

      class Dog:
    def __init__(self,name):
        self.name=name
        self._mood="happy"
        self.__secret="i love cats"
    
    def bark(self):
        print("Woof!")

    def _sleep(self):
        print("Sleeping...")

    def __dream(self):
        print("Dreaming about bones...")
d = Dog("Bruno")

print(d.name)       #  Public - works fine
print(d._mood)      #  Protected - works, but be careful
# print(d.__secret) #  rivate - will give an error

# 🕵️ But you CAN access it like this (not recommended):
print(d._Dog__secret)  # Works, but looks weird

d.bark()         #  Public method
d._sleep()       # ️ Protected method
# d.__dream()    #  Private method (won't work)
d._Dog__dream()  #  Works by name mangling

# ecpected output:

'''Bruno
happy
i love cats
Woof!
Sleeping...
Dreaming about bones... '''
