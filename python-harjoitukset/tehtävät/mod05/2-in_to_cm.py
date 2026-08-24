print ("Converting inches -> cm...\nEnter a negative number to cancel.")
while True:
    value = int(input(f"Input amount of inches here: "))
    if value < 0:
        break
    print (f"{value} inches is")
    value = value * 2.54
    print (f"{value} cm")