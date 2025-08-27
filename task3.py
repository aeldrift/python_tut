# Practice Question 
'''Try this challenge:  1.  Add a method in Animal called eat()  2. Add a method in Dog called run()  3. Create a new class BabyPuppy that inherits from Puppy  4. Create an object of BabyPuppy and call all methods.'''

class animal:
    def eat(self):
        print("i am an animal")
        
class dog(animal):
    def run(self):
        print("the dog is running")
        
class puppy(dog):
    def sleep(self):
        print("the dog is sleeping")
        
class BabyPuppy(puppy):
    def hobbie(self):
        print("The baby puppy loves playing")
        
a = BabyPuppy()
a.hobbie()
a.run()
a.eat()

# Expected output:
''' The baby puppy loves playing
the dog is running
i am an animal'''
