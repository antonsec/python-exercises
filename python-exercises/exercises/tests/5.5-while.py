while True:
    number = int(input("Give this program a number: "))
    times = number -1
    if number <= 0:
        print ("Ending program..")
        break

    while times != 0:
        factorial = number * times
        print (factorial)
        number = number * times
        times -= 1
        