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

