list  = []
print ("Input empy string to end program.")
while True:
    value = input(f"Input numbers here: ")
    list.append(value)
    if value == "":
        list.sort()
        print ((list[1]), (list[-1]))
        break
