# Lists in python
''' Ordered collection of data items,
# Lists are defined by square brackets [].
Lists can contain elements of different data types, including numbers, strings, and even other lists. 
allows duplicate elements, items are separated by commas(,) 
and are mutable( can be change or alter after creation).'''
#example:
marks=[3,5,6,"harry", True] # defining list of marks
print(marks)  # indexing starts from 0
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print("length of marks list is:",  len(marks))  # starts from 1

if 7 in marks:
    print("Yes,7 is there in the list")
else:
    print("no, 7 is not there in the list")