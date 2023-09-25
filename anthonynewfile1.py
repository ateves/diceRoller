'''random package'''
import random 

'''this is how many sidse we want the dice to have'''
num = 75

'''this the method for the dice roll'''
def rollD75(n):
    
    '''this code produces the random roll between 1 and 75'''
    roll = random.randint(1,n)

    '''The final print statement for our program, including text
    and the string type numeric description'''
    print("A roll of a dice with seventy-five sides was: " + str(roll) + ".")

'''count initialized at zero. we will count up 
and when we get to 5 rolls, the program will stop'''
count = 0

'''while loop for rolling the dice five times'''
while (count<5):

    '''dice rolling method is called '''
    rollD75(num)

    '''count increases by one'''
    count += 1

'''else (exit) for the while loop'''
if (count==5):
    pass

'''This program was written by ANTHONY T'''