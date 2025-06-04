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
 
p=int(input("enter first name:" ))   #type casting is don't to make it an int value separately
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

name="harry"
frnd_name="raghav"
print("hey!, my name is " +name + " and my friend's name is " +frnd_name +".")
# can use a colon(,) or addition symbol(+) as well.
# it can't combines a string and an integer together.

line= """hey! myself an enthusiastic tech learner.
currently, i'm learning python.
what about you?"""   # To print multiple line statement, can you ("""") or ('''). By this you can avoid error of EOL while scanning string literal.
print(line)
# string is like an array of characters(not exact) as indexing is done.
name="harry"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5])  will gives an error: string index out of range.
print("Let's print using a foor loop\n")
for character in name:
     print(character) # Helps to printeach character of complex strings without indexing separately.

import lorem
st=lorem.paragraph()   # here, lorem is used to create some random text. 
print(st)                          # for which firstly, lorem library is imported.
for char in st:
     print(char)

#indexing & slicing 

print(name[0:4])  # while indexing, index starts from zero(0), includes starting index & excludes the ending index.
name1="Harry, Shubham"
print(name1[0:9])  # spaces are also counted. as shows output: Harry, Sh
name2="Harry,Shubham"   
print(name2[0:9])# output is Harry,Shu 

# to find length of a string
print(len(name1)) # output: 14 
print(len(name2)) # output: 13       # counts space
fruit="Mango"
print("fruit is of ", len(fruit), "word length") # or can create a separate variable also to print.
'''length=len(fruit)                                 # it will gives an error.
print("the length of fruit is" {length} + "yes" )''' 
# Here '+'  will not workout as it adds or combine only strings together.
#  Hence can use a formatted string literals (i.e f-string) for instance:
new_name="Rahul" 
age=20
print(f" My name is {new_name} and I am {age} years old. ")
fruit1 = "apple"
length = 5   # int value
print(f"The length of {fruit1} is {length}") # converted int value in a str value.
# QUICK TIP : 
'''Use f"..." if you're using {} to insert variables.  
 Don't mix + with {}  
AS LIKE: 
                f"Hello, {name}" → f-string
                "Hello, {name}" → just a regular string, no formatting '''
# Now, how (if 5 be a number) can be taken as a string?
a = 5
b = 3          # a and b are numbers (int).
print(f"{a} + {b} = {a + b}")   # But you’re using them inside a string.

# Same thing in old way
a = 5
print("Value is " + str(a))  #  Manual conversion  # can use str(a) also.
# negative indexing
fruit="Mango"
print(fruit[0:4])    #output: Mang
print(fruit[:4]) # will take zero(0) by default    # output: Mang
print(fruit[0:-2])  # output: Man  # here, it is taken as [0: len(fruit)-3] as:
print(fruit[0:len(fruit)-2])   # output: Man
print(fruit[-1:-2]) # here it wont show anything. neither output nor an error as it works but doesn't makes any sense.
print(fruit[0:2])

# QUICK QUESTION:
# If name is Harry, then find result after slicing from [-4 to -2] 
name="Harry"
print(name[-4:-2])  # output : ar as: length=5 so, we have; [5-4:5-2] =[1:3]= 1 included and 3 is excluded.

# strings:
# Strings are immutable
# A set of build-in methods are provided used to alter and modify.
# These methods won't change string but apply operations and make a new string( as like copy of the string).
string= "Teesha"
print(len(string))
print(string.upper())

# or can call a function in different ways:
# 1. You did call the method on this line and then print the value.
text="Hello"
method_ref = text.upper()  # <- the () here calls the method 
print(method_ref)  # This just prints the string "HELLO"

# 2.  If you want to store the method itself (not the result):
text = "hello"

# Store the method itself (not called yet)
method_ref = text.upper  # no ()

# Now call the stored method
print(method_ref())  # Output: HELLO
# lower
string1="HARRY"
print(string1.lower())

#rstrip(): removes any trailing characters (i.e. characters at end)
string2="Hello!!!"
print(string2.rstrip("!"))   # output: Hello
string3="!Hello!7abc!8!"
print(string3.rstrip("!"))   # output: !Hello!7abc!8

# replace(): it replaces all occurances of a string with another string.
string4=" He is john . John is my good friend. John is a good boy."
print(string4.replace("John", "harry")) # replaces all occuarnces but he is joh is not replaced, as python is case sensitive.

string4=" He is John. John is my good friend. John is a good boy."
print(string4.replace("John", "Harry"))

# split():  splits the given string at a specified instance and returns the separatee strings as list items .
string5="apple banana  mango 23 wow! 56.3 true" 
print(string5.split())   # can hold int, char, symbols and all datav types

# capitalize() : turns first character of string to upper case and all the rest in lower case.
string6="introducioon to pytHon"  
capit=string6.capitalize()    # if there's no change then won't show any error.
print(capit)     # i turns to I and rest in lower case (H turns to h) 
 
# center(): aligns the string to the center as per parameters given b y the user.
string7="Welcome"
print(string7.center(51))  
print(string7.center(90))  
print(len(string7.center(50))) 
# logic:
''' string7.center(50)
You're centering "Welcome" in a space of 50 characters.

So:

Total space = 50

Text = 7

Spaces = 50 - 7 = 43

Half on left, half on right → about 21 on left, 22 on right ( Python adds extra space to the right if it's odd.)

Output: " Welcome "

Length: 50'''

print(len(string7.center(10)))

''' len(string7.center(10))
Total = 10

10 - 7 = 3 spaces → 1 on left, 2 on right (Python adds extra space to the right if it's odd)

Output: " Welcome "
Length: 10 '''
# for more detail, print table and go through it.

from tabulate import tabulate
# Define table data as a list of lists (like rows)
data = [
    ["Even", "Even/Odd", "Even", "equal", "equal", "—"],
    ["Odd",  "Even/Odd", "Odd",  "<", ">", "✅ Right side"]
]# Define column headers
headers = ["Total width", "Text length", "Extra spaces", "Left", "Right", "Extra space goes to..."]

# Print the table
print(tabulate(data, headers=headers, tablefmt="github"))

# count() : returns the no. of times the given value has occured within the given string.
string8="AbhfgAnnaaii"
print(string8.count("A"))  # py is case sensitive so dont count small character(a).

# endswith(): checks if the strings end with a gtiven value. If yes, then  rerturn True else return False.
# returns boolean data type
string9="welcome to the console!!"
print(string9.endswith("!!"))   # true
print(string9.endswith("!!!"))   # false

# we can also check for a value in between the string by providing start and end index  positions.
print(string9.endswith("con",4,18))











