# clear Cluttering
#example:
print("Hello! Alice")
print("Hello! Harry")
# instead of this,try to remove cluttering:

users=["Alice","Harry"]
for user in users:
    print(f"Hello! {user}")
# BASIC CLUTTER CLEARING RULES:
''' 1. Don't Repeat Yourself (DRY)
Repetition = future maintenance pain. Use functions.'''

# Instead of doing this:
print("Bye, Alice!")
print("Bye, Bob!")

# Do this:
def say_goodbye(name):
    print(f"Bye, {name}!")

say_goodbye("Alice")
say_goodbye("Bob")

''' 2. Name Things Clearly
Bad names = confusion. '''

# Bad:
def f(x):
    return (x **2 )* 3.14

# Good:
def calculate_area(radius):
    return (radius **2 )* 3.14
    
print(calculate_area(5))

# Use Built-in Python Features
''' Don’t write something manually if Python already has a tool for it. '''

# Bad:
words = "hi hi hello hi".split()
count = {}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(count)

# Good:
from collections import Counter
count = Counter("hi hi hello hi".split())
print(count)

# 🧪 5. Practice Task: Turn it into clean, reusable code.

''' name1 = "Sarah"
name2 = "Tom"
print("Hi " + name1)
print("Hi " + name2)
# More people?
# Might need to update '''

def greet_person(name):
    print(f"Hi {name}") 
    
names = ["Sarah", "Tom", "Alice", "Bob"] 
for name in names:
  greet_person(name)
