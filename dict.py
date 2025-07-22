# to create a dictionery 
# And applying different operatiions 

ep1={122:45, 123:89, 567:69, 670:69}  # dict created
ep2={222:67, 566:90}

ep1.update(ep2)   #dict2 is added to dict1 and updated
print(ep1)

ep1.pop(122)
print(ep1)

ep1.popitem()
print(ep1)

