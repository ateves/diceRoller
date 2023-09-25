import random 

num = 75

def rollD70(n):
    roll = random.randint(1,n)
    print("A roll of a dice with seventy-five sides was: " + str(roll) + ".")

count = 0

while (count<5):
    rollD70(num)
    count += 1
else:
    pass
#This program was written by ANTHONY T.
