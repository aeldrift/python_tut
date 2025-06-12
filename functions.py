# Functions: A block of code that performs a specific task whenever it's called.
''' In bigger programs, where we have large amounts of code, it is adviseable to create or use
an existing functions that make the program flow organised and neat.
There are two types of functions:
1. Built-in functions  2. User defined functions'''

# Built-in functions:
''' are defined and pre-coded in python. Some examples of built-in functions are as follows:
# min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print() etc.'''

# User- defined functions: 
'''can create functions to perform specific tasks as per our needs.'''

def sum(x,y):
   result=x+y
   print(result)

sum(10,20)
sum(34,10)

# example : A program to calculate geometric mean

def calgmean(a,b):
    mean= (a*b)/(a+b)
    print(mean)
a=9
b=8
calgmean(a, b)
c=2
d=6
calgmean(c,d)

# can also use & apply some conditional statements with functions.

def calgmean(a,b):
    mean= (a*b)/(a+b)
    print(mean)
a=9
b=8
if a>b:
    print("first no. is greater" )
else:
    print("second no. is greater or equal")
calgmean(a, b)
c=2
d=6
if c>d:
    print("first no. is greater" )
else:
    print("second no. is greater or equal")
calgmean(c,d)

# can also create an another functions in one function.

def calgmean(a,b):
    mean= (a*b)/(a+b)
    print(mean)
a=9
b=8
calgmean(a, b)
c=2
d=6
calgmean(c,d)

# can also use & apply some conditional statements with functions.

def calgmean(a,b):
    mean= (a*b)/(a+b)
    print(mean)
def isgreater(a,b):
    if a>b:
        print("first no. is greater" )
    else:
        print("second no. is greater or equal")
def isless(a,b):
    pass # a function is created and passed (pass) as want to write the body of function later. or else will shows an indentation error. 
a=9
b=8
isgreater(a,b)
calgmean(a, b)
c=2
d=6
isgreater(c,d)
calgmean(c,d)

#  Write a program to greet user using function:

# Define the function
def greet_user(name):
    print("Hello, " + name + "! Welcome to the program.")

# Main part of the program
user_name = input("Enter your name: ")
greet_user(user_name)
