import random

def roll_dice():
    i = random.randint(1,6)
    return i

while True:
    dice = roll_dice()
    print (dice)
    if dice == 6:
        break