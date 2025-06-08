# # elif statement:  sometimes we need to check multiple conditions.
# #In such cases, we can use elif statement. elif is short for else if. It is used to check multiple conditions in a single if-else statement.

# '''Write a program to check the grade of a student based on the marks obtained. If the marks are greater than or equal to 90, then the grade 
# is A. If the marks are greater than or equal to 80 but less than 90, then the grade is B. If the marks are greater than or equal to 70
# but less than 80, then the grade is C. If the marks are greater than or equal to 60 but less than 70, then the grade is D. Otherwise,
# the grade is F.'''

# #The program checks the marks obtained by the student and prints the grade based on the marks.

# marks = float(input("Enter your marks: ")) 
# if marks >= 90:
#     print("Your grade is A")

# elif marks >= 80: # elif is used to check multiple conditions
#     print("Your grade is B")
# elif marks >= 70:
#     print("Your grade is C")
# elif marks >= 60:
#     print("Your grade is D")
# else:
#     print("Your grade is F")
# '''Write a program to check the day of the week based on the number entered by the user.
# If the number is 1, then it is Monday and so on. If the number is greater than 7, 
# then it is an invalid input.'''

# day = int(input("Enter a number between 1 and 7: "))
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")

# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# else:
#     print("Invalid input, please enter a number between 1 and 7.")

    
# '''Write a program to check the type of triangle based on the lengths of the sides entered by the user.'''

# side1 = float(input("Enter the length of side 1: "))
# side2 = float(input("Enter the length of side 2: "))
# side3 = float(input("Enter the length of side 3: "))

# if side1 == side2 and side2 == side3:
#     print("The triangle is equilateral.")

# elif side1 == side2 or side2 == side3 or side1 == side3:
#     print("The triangle is isosceles.")
# else:
#     print("The triangle is scalene.")

# '''Write a program to check the type of number entered by the user. If the number is even, then it is an even number.
# If the number is odd, then it is an odd number. If the number is zero, then it is zero.'''

# number = int(input("Enter a number: "))
# if number == 0:
#     print("The number is zero.")  # to check no. as zero

# elif number % 2 == 0: # to check even no.
#     print("The number is even.")

# else:
#     print("The number is odd.") # to print odd no.

# '''Write a progrmam to check the type of character entered by the user. If the character is a vowel,consonant or digit.
# and if the character is a special character, then it is a special character.'''

# char = input("Enter a character: ")
# if char.isdigit():
#     print("The character is a digit.")
# elif char.lower() in 'aeiou':
#     print("The character is a vowel.")
# elif char.isalpha():
#     print("The character is a consonant.")
# else:
#    print("The character is a special character.")



   