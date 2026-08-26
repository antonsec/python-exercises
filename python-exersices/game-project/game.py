name = "Pierre" #str(input("Hello traveler.. What may your name be?\n"))
print (f"Welcome {name}. Let's get you started")
age = 13 #int(input(f"Oh.. well hello {name}, good to meet you! May I ask ye age?\n"))

inventory = []

def adding_item(item):
    inventory.append(item)

def showing_items():
    for i in inventory:
        print (i)

def profile():
    print ("--- Player profile ---")
    print (f"Name: {name}")
    print (f"Age: {age}")
    print (f"Inventory:")
    showing_items()

while True:
    if age < 12:
        print ("Yikes! Sorry! You're too young for this game! Try again in a few years!")
        break

    print ("\nOptions: 1 Add items to inventory, 2 Check inventory and 3 Prints player profile.\n")
    command = input("Command: ")
    if command == "":
        print (f"See you again {name}...")
        break

    if command == "1":
        new_item = input(f"What item would you like to add? ")
        adding_item(new_item)
        print (f"Added {new_item} to inventory!")

    elif command =="2":
        print ("Your invetory is... interesting to say the least.\nHeres what you have:")
        showing_items()

    elif command == "3":
        profile()