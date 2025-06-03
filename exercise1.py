# EXERCISE NO:1 Create a calculator capable of performing addition, subtraction, multiplication and division operators on two numbers. Your program should format the output in a readable manner.


a=2         # number1
b=4         # number2
print("the sum of two numbers is", a+b)
print("the difference of two numbers is", a-b) 
print("the product of two numbers is", a*b)
print("the division of two numbers is", a/b)
print("the division of two numbers is", a//b)
print("the division of two numbers is", a%b)

#typecasting or type conversion
#conversion of one data type into another data type is known as type casting or type conversion in python.

c="4"
d="5"
print(c+d)
print(int(c)+ int(d))  # also is type of explicit type casting
e=6.7  #float
f=9  #integer
print(e+f)  # here, lower data type is converted into higher data type
print(type(e+f)) # is type of implicit type casting or type conversion

# Taking input from the user.   We can directly take input from user. This function gives a return value as  string/character . Hence we have to pqass that into a variable.
x=input("enter your name/number:" )   #concatinates as take string value by default
y=input("enter your name/number:" )
print("My name is", x+y)
 
p=int(input("enter first name:" ))   #type casting is dont to make it an int value separately
q=int(input("enter second name:" ))
print("the sum of two numbers is:", p+q)

m=input("enter number_1:" )           #type casting is dont to make it an int value while adding directly
n=input("enter number_2:" )
print("the sum of two numbers is:", int(m)+int(n))  

x=input("enter your name/number:" )  # In python, we can rewrite a variable
y=input("enter your name/number:" )
print("My name is", x+y)
# x-y, x*y, x/y
# This will not work on string and shows error



