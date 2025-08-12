# Static methods 
# Example: 

class Example:
    def instance_methods(self):
        print("I'm an instance method")
    @staticmethod
    def static_method():
        print("I'm a static method")
        
e=Example()
e.instance_method() # Works
e.static_method()   # Also works


Example.static_method() # Also works directly from class
  
