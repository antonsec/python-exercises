numbers  = []
print ("Input empty string to end program.")

while True:
    value = input(f"Input numbers here: ")

    if value == "":
        print ("")
        numbers.sort(reverse=True)
        break

    numbers.append(int(value))

x = 0
print ("The 5 largest numbers are:")

for i in range(5):
    print (numbers[x])
    x += 1