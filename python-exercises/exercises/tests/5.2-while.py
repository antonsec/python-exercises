number = int(input("Enter a positive number: "))
limit = number
number = 0

while True:
    if limit <= 0:
        print ("Error. Please input a positive number...")
        break

    if number % 2 == 0:
        print (number)
        number += 2
        if number > limit:
            break