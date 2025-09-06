# Function Arguments and return statements
''' There are four types of function arguments:
1. Default arguments: provide a default value for an argument if no value is passed during the function call.'''
# example: 1
def average(a=2,b=2):
    print("The average is:", (a+b)/2 )  
average()
average(4)
average(b=6)
#example: 2 
def name(f_name, m_name, l_name= "singh"):
    print("The full name is:", f_name, m_name, l_name)
name("john", "kumar")

'''2. Keyword arguments: allow you to pass arguments to a function by explicitly specifying the parameter name 
and can pass arguments in any order'''
# example: 1
def average(a=2,b=2):
    print("The average is:", (a+b)/2 )  
average(b=4, a=6)  # passing arguments in different order using keyword arguments

'''3. Required arguments: If don't pass arguments as Key-value syntax, then it's necessary to pass arguments in coreect positional order and no. of arguments pass should match wit actual function definition'''
# example: 1 When no of arguments passes do not match to the actual funcn definition.

def name(f_name, m_name, l_name= "sir"):
    print("Hello", f_name, m_name, l_name)
name("john", "kumar") 

'''4. Variable-length arguments: is used when have to pass more arguments than those defined in actual function definition.'''
# example: 1
def average(*numbers):
    print(type(numbers))  # checking the type of variable-length arguments
    sum=0
    for i in numbers:
        sum=sum+i
    print("average is:", sum/len(numbers))
average(2, 4, 6, 8, 10)  # passing variable-length arguments

''' Return statement: is used to return a value of the expression back to the calling function. If no return statement is present, the function returns None by default.'''
# example: 1
def average(*numbers):
    sum=0
    for i in numbers:
     sum=sum +i
    return sum/len(numbers)  # returning the average value
result=average(2,4,6,8,10)
print(result)  # prints the returned value

