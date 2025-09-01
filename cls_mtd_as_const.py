class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def intern(cls, name):
        return cls(name, 5000)  # default salary for interns

# Regular Constructor 
e1 = Employee("Alice", 40000)


e2 = Employee.intern("Bob")

print(e1.name, e1.salary)
print(e2.name, e2.salary)