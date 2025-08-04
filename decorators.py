# decorators 
# Creating a simple decorator
def greet():
    print("Hello! I am a Decorator")
def wrapper_function(func):
    func()
wrapper_function(greet)  #output: Hello! I am a Decorator

# decorator by passing arguments:

def bar(**kwargs):
    print("kwargs is:", kwargs)

bar(a=1, b=2)  # kwargs is: {'a': 1, 'b': 2}

def abc(*args):
    print("args is:", args)

abc(1, 2, 3)   # args is: (1, 2, 3)
# example: 
def decorator(func):
    def wrapper():
        print("transaction initiated")
        func()
        print("transaction completed")
    return wrapper

def hello():
    print("the sum is:")

he = decorator(hello)
he()         
#output:
''' transaction initiated
the sum is:
transaction completed'''

# example: 
def decorator(func):
    def wrapper(*args, **kwargs):
        print("transaction initiated")
        func(*args, **kwargs)
        print ("transaction completed")
    return wrapper 
def hello(a=1,b=1):
    print("the sum is:", a+b)
    
hello1= decorator(hello)
hello1()

# example: also can use like this:
def decorator(func):
    def wrapper(*args, **kwargs):
        print("transaction initiated")
        func(*args, **kwargs)
        print ("transaction completed")
    return wrapper 
    
@decorator
def hello(a=1,b=1):
    print("the sum is:", a+b)
    
hello()
# example:1
def greet(func):
    def wrapper(*args, **kwargs):
        print("Hi!")
        return func(*args, **kwargs)
    return wrapper
    
# example:2 where:  
'''  
output: Good Morning
5
Thanks for using this function'''

@greet
def add(a=0, b=0):
    print("sum is:",a + b)

add(10,80)


def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello world")

@greet
def add(a, b):
    print(a + b)
add(2,3)

# using logging: 
import logging
logging.basicConfig(level=logging.INFO)

logging.info("This is an info message")


logging.basicConfig(level=logging.INFO)

# Define the decorator
def log_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling function '{func.__name__}' with args={args} and kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function '{func.__name__}' finished and returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

@log_decorator
def greet(name="World"):
    return f"Hello, {name}!"

# Call them
add(2, 3)
greet(name="Alice")

# Example: a simple logging decorator
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Decorator that logs function calls
def log_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Function '{func.__name__}' called with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper

# Example function using the decorator
@log_decorator
def add(a, b):
    return a + b

# Call the function
add(5, 7)

# practise questions:
# Write a decorator called @my_decorator that prints "Before the function" before a function runs and "After the function" afterward.
def my_decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper
@my_decorator
def hello():
    print("Hello, i am a function")
hello()

# Write a decorator that modifies the return value of a function by converting it to uppercase.

def deco(func):
    def wrapper():
        s = func()
        print("String in uppercase is:", s.upper())
        return s
    return wrapper

@deco
def input():
    return "i am a function."

input() # expected ouptput: String in uppercase is: I AM A FUNCTION.


