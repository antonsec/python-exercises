import random
number  = random.randint(1, 10) 

print ("Try to guess the randomly generated number!!")
while True:
    value = int(input(f"What's your guess?\n"))

    if value > number:
        print ("Too high.. TRY AGAIN!")
    elif value < number:
        print ("Too low.. TRY AGAIN!")
    elif value == number:
        print (f"Congrats!\nYou guessed the correct number! It was {value}!")
        break