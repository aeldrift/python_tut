#conditional statements 

# if- else statements: sometimes,we need to check evaluation of certain expression(s) whether the expression(s)  evaluate to True or False. if the expression evaluates to True, then the code block inside the if statement is executed, otherwise the code block inside the else statement is executed.
# thr program execution follows a different path based on the evaluation of the eexpression.

# conditional operators : >, <, >=, <=, ==, != 
# Create a program to check if the candidate can vote or not.

age=int(input("enter your age: "))
print(" Your age is: ", age)  # print function is used to print the value of age.
print(age>=18)
if age>=18:
     print("You can vote")
else:
    print(" You cvan't vote")

# create a program to get input from the user and check if the person can drive or not.

a=int(input("Enter you age:"))
print(f"Your age is: {a}")  # formatted string is used to combine a string and an int value.

if a>=18:
    print(" You can drive")
else:
    print("You can't drive.")

# create a program to ask assistant to add apples to the cart if the user has more than 5 apples, otherwise ask to add oranges to the cart.
apples=int(input("Enter the number of apples you have: "))
if apples>5:
    print(" alexa add apples to the cart")
else:
    print(" alexa do not add apples to cart")
# create a program to check if the user is eligible for a scholarship or not. if the user has more than 90% marks, then the user is eligible for scholarship, otherwise not. 
total_marks= int(input("Enter total marks: ")                )
marks= float(input(" Enter your marks"))
print(" Your marks are: ", marks)
print("You scored" , marks, "out of" ,total_marks)
percentage= (marks/total_marks)*100
print(" Your percentage is: ", percentage)
if percentage>90:
    print("You are egligible of scholarship")
else:
    print("You are not egligible for scholarship")





