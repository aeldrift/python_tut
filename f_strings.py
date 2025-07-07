'''f-strings in python: A new way to format strings introduced by the PEP 498 in Python 3.6.
 It is also known as "string interpolation" or "formatted string literals".
 It is a convenient way to embed expressions in string literals,for formatting using curly braces '{}' to evaluate variables and expressions at runtime.'''
#cexample:1
letter= "My name is {} and I am from {}."
# Here, the curly braces '{}' are placeholders for the variables 'name' and 'country'.
name= "John"
country= "INDIA"
print(letter.format(name,country))
# example2:
letter= "My name is {1} and I am from {0}."
# Here, the curly braces '{}' are placeholders for the variables 'name' and 'country'.
name= "John"
country= "INDIA"
print(letter.format(country,name))


name= "teesha"
#But to avoid mistakes, use like this:
print(f"My name is {name} and I am from {country}.")

