class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def intern(cls, name):
        return cls(name, 5000)  # default salary for interns

# Regular Constructor 
e1 = Employee("Alice", 40000)

# class method used as constructor 
e2 = Employee.intern("Bob")

print(e1.name, e1.salary)  # Alice 40000
print(e2.name, e2.salary)  # Bob 5000


# Quick check for you:
''' If you wanted a constructor for managers, where the salary is always 80000,
how would you write that class method inside Employee?  '''

class Employee:
    def __init__(self, post, salary):
        self.post = post
        self.salary = salary

    @classmethod
    def Manager(cls, post):          # class method as alternative constructor
        return cls(post, 80000)      # create object with fixed salary

# create object using class method
e1 = Employee.Manager("Manager1,")

print(e1.post, e1.salary)