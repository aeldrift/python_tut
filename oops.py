# OOPS CONCEPTS
# To create classes and objects

class person():
    name="Harry"
    occupation ="Software Developer"
    network=10
    def info(self): # using self parameter
        print(f"{self.name} is a {self.occupation}")

a= person()
b= person()
a.name ="Shubham"
a.occupation="Accountant"

b.name ="Nitika"
b.occupation="HR"
a.info()  # Shubham is a Accountant
b.info()  # Nitika is a HR


    

