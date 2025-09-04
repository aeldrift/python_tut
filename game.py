# TASK: create a snake, water and gun game.

# Using random library to generate random nos.
import random
n=random.random()
print(n)

# to choose random no. between two given nos.

import random
print(random.randint(1,5))

# Game Implementation:

import random
def check(comp,user):
    if comp == user:
        return 0 
    if comp == 0 and user == 1:
        return -1
    if comp == 1 and user == 2:
        return -1
    if comp == 2 and user == 0:
        return -1
        
    return 1
            
comp=random.randint(0,2)
user= int(input("choose you opt: \n 0 for Snake \n 1 for Water \n 2 for Gun\n Choose your input: "))
if user not in[0,1,2]:
    print("Invalid choice! Please choose only 0, 1, or 2.")
else:
    score=check(comp,user)

    print("You choose:", user)
    print("Computer choose:",comp)


if score == 0:
    print("Match Draw")
elif score == -1:
    print("You Lose")
else:
    print("You Won 🎉")

# Expected output (as per loss and win condition opts choosen):
''' choose you opt: 
 0 for Snake 
 1 for Water 
 2 for Gun
 Choose your input: 2
You choose: 2
Computer choose: 0
You Won 🎉 '''



    



