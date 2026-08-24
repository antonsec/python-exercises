name = str(input("Hello traveler.. What may your name be?\n"))

print (f"Welcome {name}. Let's get you started")

age = int(input(f"Oh.. well hello {name}, good to meet you! May I ask ye age?\n"))

while True:
    if age < 12:
        print ("Yikes! Sorry! You're too young for this game! Try again in a few years!")
        break

    print ("\nOptions: 1 Prints name, 2 Prints age and 3 Prints player profile.\n")
    command = input("Command: ")

    if command == "stop":
        print (f"See you again {name}!")
        break

    if command == "1":
        print (f"Name: {name}")
    elif command =="2":
        print (f"Age: {age}")
    elif command == "3":
        print ("--- Player profile ---")
        print (f"Name: {name}")
        print (f"Age: {age}")