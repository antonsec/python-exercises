import random

def roll_dice(sides): # were making a program that requires 1 parameter (sides)
    i = random.randint(1, sides) #generating a random number between 1 and (sides)
    return i

sides_for_dice = int(input("How many sides does our dice have? ")) # WE ARE asking USER how many sides our dice has

while True:
    dice = roll_dice(sides_for_dice) # dice = how many sides our dice has calling back to line 4
    print (dice) # which is 1 inbetween dice
    if dice == sides_for_dice: # If the rng is same as sides = break
        break