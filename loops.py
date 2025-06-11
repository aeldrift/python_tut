# Loops: 
'''sometimes a programmer needs to repeat a block of code multiple times, so loops are used.
 Classified into two main types:
 * Foor loop   * While loop '''
# For loop:used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects.

name="abhishek" 
for i in name:
    print(i, end=",\n")  # end=",\n" is used to print each character on a new line 
    if i== "b":
        print("letter b found")
    
# using a list:
colors=["red", "blue", "green", "blue", "yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

# using range 
for k in range(5):  # Here last value is  not included.
    print(k)

for k in range(6):
    print(k+1)

for k in range(1,6):  # now, the value is specified, so no need to add +1 (i.e. k+1) to include last value.
    print(k)

# for complex range:
# example:
for k in range(20001):
    print(k)

# Write a program to print the first 10 even numbers:
for k in range(0, 20, 2):  # start at 0, end at 20, step by 2
    print(k)

# Write a program to print the first 10 odd numbers:

for k in range(1, 20, 2):  # start at 1, end at 20, step by 2
    print(k)

# While loop: used to execute a block of code repeatedly as long as a given condition is true.
    
# Example:
count = 0
while (count < 10):
    print("Count is:", count)
    count += 1  # increment count by 1
# Note: If the condition is never false, the loop will run indefinitely (infinite loop).


# Using break statement to exit a loop:
for i in range(10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break  # exit the loop when i is 5
    print(i)

# Using continue statement to skip the current iteration:
for i in range(10):
    if i == 5:
        print("Skipping the iteration at i =", i)
        continue  # skip the rest of the loop when i is 5
    print(i)
# another example:

i=int(input(" Enter a number: "))
while (i<=5):
    i= int(input(" Enter a number"))
    print(i)
print("Done with the loop")

# program for decrement:

count=5
while(count>0):
    print(count)
    count=count-1  # decrement count by 1           

# else with while loop: we can even us else with while loop. As soon as the while loop condition becomes false, the interpreter comes out of the while loop and else statement is executed.

count=5
while (count>0):
    print(count)
    count=count-2
else:
    print(" I'm out of while loop now")

# Note: The else block will not execute if the loop is terminated by a break statement.

# QUICK NOTE:
'''Python does not have a built-in do...while loop like C, C++, or Java.However,
you can simulate a do...while loop in Python using a while True loop with a break condition inside.'''

# break: is used when to go out of  the loop in between.
# continue: is to goout of loop after the iteration.

# example of break:

for i in range(12):
    if (i==10): 
        break
    print("5 *",i+1, "=", 5*(i+1))
print("its out of the loop")

# Example of continue:

for i in range(12):
    if i == 10:
        print("Skip the iteration")
        continue
    print("5 *", i, "=", 5* (i))

# Emutate a do while loop:
# It wil execute at least once( irrespective of the condition)

i=0
while True:          # * also known as exit-controlled loop
    print(i)
    i=i+1
    if i%5==0 :
        break
# note: What if use False instead of true?
'''Nothing will be printed.
Because: means the loop never runs (not even once) as the loop body skipped. So, it’s not an exit-controlled loop. The body is skipped entirely.'''