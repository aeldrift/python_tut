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







