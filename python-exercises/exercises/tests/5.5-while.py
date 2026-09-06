while True:
    number = int(input("Type and integer number: "))
    factorial = 1

    if number <= 0:
        break

    for i in range(1, number + 1):
        factorial *= i
    print (factorial)