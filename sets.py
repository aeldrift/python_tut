# Sets: are unordered collections of data items that are unique.
# They are mutable, meaning you can add or remove items, but the items themselves must be immutable.
# Sets are useful for membership testing, removing duplicates from a sequence, and performing mathematical set operations.

# Example of creating a set
my_set = {1, 2, 3, 4,2, 5}  # duplicates are ignored
print("my set:",my_set)

info= {"john", 19, "USA", 19.5, True,19}  # mixed data types
print("info set:", info)

for value in info:
    print(value)

name_set=set()
print(name_set)  # empty set
print(type(name_set))  # <class 'set'>

cities= {"Delhi", "Mumbai", "Kolkata", "Chennai"}
cities2= {"Delhi", "seoul","Madrid", "Kolkata", "Chennai"}
# cities.add("Bangalore")  # adding an element
# print("cities after adding Bangalore:", cities)
cities3=cities.union(cities2)
print(cities3)
print(cities) # remains unchanged
cities.update(cities2)
print(cities)  # cities is updated with elements from cities2

# intersection case
juice={"apple", "orange", "banana","guava"}
juice2={"banana", "kiwi", "orange"}
juice3=juice.intersection(juice2)
print("juice3 is:",juice3)
print("juice set\(when not updated) is:", juice) # remains unchanged  
juice.intersection_update(juice2)
print("when juice set updated:", juice)
