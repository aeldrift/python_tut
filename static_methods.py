# Static methods 
# Example: 

class Example:
    def instance_method(self):
        print("I'm an instance method")
    @staticmethod
    def static_method():
        print("I'm a static method")
        
e=Example()
e.instance_method() # Works
e.static_method()   # Also works


Example.static_method() # Also works directly from class
  
# Example2:
class TemperatureConverter:
    @staticmethod 
    def Temp(c):
        return (c*9/5) +32
        
celsius=float(input("Enter Temp in celsius:" ))
print(TemperatureConverter.Temp(celsius))

# Practise Question:
'''Create a class Calculator that has a static method called multiply which takes two numbers as input and returns their product. '''

class Calculator:
    @staticmethod 
    def Multiply(num1,num2):
        return num1 * num2
        
num1=float(input("Enter 1st number:" ))
num2=float(input("Enter 2nd number:" ))

result=Calculator.Multiply(num1,num2)

print(f"The product of {num1} and {num2} is: {result}")
