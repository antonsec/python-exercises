times = 0
number = int(input("Enter a positive number: "))

while number > 0:

    print (times)
    times += 2
    if times > number:
       break

if number <= 0:
    print ("Error")