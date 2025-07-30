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

# PY decorator using logging 

import logging

# Configure logging to display INFO level messages
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f'Calling {func.__name__} with args={args}, kwargs={kwargs}')
        result = func(*args, **kwargs)
        logging.info(f'{func.__name__} returned {result}')
        return result
    return decorated
@log_function_call
def my_function(a, b):
    return a + b
# Test the function
result = my_function(5, 7)
print("Final result:", result)


