while True:
    n = int(input("Enter a number: "))

    if n <= 0:
        break

    n1 = 1
    factorial = 1

    while n1 <= n:
        factorial = factorial * n1
        n1 += 1

    print (factorial)