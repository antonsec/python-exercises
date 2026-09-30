phonebook = {
}

while True:
    choice = int(input("Choices: 1. Add a new contact 2. Search existing contact 3. Quit\n"))
    if choice == 3:
        print ("Ending program.")
        break

    elif choice == 1:
        name = input("Enter contact name: ").lower()
        number = input(f"Enter {name}'s number: ")
        phonebook[name] = number

    elif choice == 2:
        name = input("Enter conctact name: ").lower()
        if name in phonebook:
            print (f"{name}'s phone number is: {phonebook[name]}\n")
        else:
            print (f"{name} is not in the phonebook.\n")