# # Loops: 
# '''sometimes a programmer needs to repeat a block of code multiple times, so loops are used.
#  Classified into two main types:
#  * Foor loop   * While loop '''
# # For loop:used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects.

# name="abhishek" 
# for i in name:
#     print(i, end=",\n")  # end=",\n" is used to print each character on a new line 
#     if i== "b":
#         print("letter b found")
    
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
while count < 5:
    print("Count is:", count)
    count += 1  # increment count by 1
# Note: If the condition is never false, the loop will run indefinitely (infinite loop).

# Example of infinite loop (uncomment to run):
# count = 0
# while count < 5:
#     print("Count is:", count)
#     count += 1  # This will never make count >= 5, so it will run forever.

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