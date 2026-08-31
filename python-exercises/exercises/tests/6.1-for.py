while True:
    number = int(input("Give this program a number: "))
    if number <= 0:
        print ("Error.. Enter a positive number.")

    for i in range(number + 2):
        if i % 2 == 0:
            print (i)
