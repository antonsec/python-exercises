number = int(input("Enter a positive number: "))

while True:
    if number <= -1:
        print ("Error: Please enter a positive number...")
        break
    elif number >= 0:
        print (number)
        number -= 1
        if number == -1:
            break