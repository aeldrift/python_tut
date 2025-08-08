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
    if comp == user:   # Game conditions
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
# Score Evaluation
score=check(comp,user)

print("You choose:", user)
print("Computer choose:",comp)


if score == 0:
    print("Match Draw")
elif score == -1:
    print("You Lose")
else:
    print("You Won")

