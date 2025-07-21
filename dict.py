# to create a dictionery 
# And applying different operatiions 

ep1={122:45, 123:89, 567:69, 670:69}  # dict created
ep2={222:67, 566:90}

ep1.update(ep2)   #dict2 is added to dict1 and updated
print(ep1)  # {122: 45, 123: 89, 567: 69, 670: 69, 222: 67, 566: 90}

ep1.pop(122)
print(ep1)  # {123: 89, 567: 69, 670: 69, 222: 67, 566: 90}

ep1.popitem()
print(ep1)  # {123: 89, 567: 69, 670: 69, 222: 67}

# del ep1   # will deletes the dict ep1 
# print(ep1)  # so shows an error as now, no ep1 dict exists.

del ep1[670]
print(ep1)  # {123: 89, 567: 69, 222: 67}

# Some important things to know:

# SOME IMPORTANT THINGS TO KNOW:

# we can use else statement with for loop and while loop also.

# cse: For loop
for i in range(6):
  print(i)
  if i==4:    # If else executed then loop doesn't break. It exits sucessfully.
    break
else:
    print("sorry no i is there")   

#case: While loop
i=0
while i<7:
  print(i)
  i=i+1
  if i==4:
    break
else:
<<<<<<< HEAD
    print("sorry no i is there")
=======
    print("sorry no i is there")
>>>>>>> 9a2055321813c61ea9f4c297d2065883b8a6083c
