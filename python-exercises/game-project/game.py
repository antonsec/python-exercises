name = "Pierre" #str(input("Hello traveler.. What may your name be?\n"))
print (f"Welcome {name}. Let's get you started")
age = 13 #int(input(f"Oh.. well hello {name}, good to meet you! May I ask ye age?\n"))

inventory = [] # using this as players inventory

def adding_item(item):
    inventory.append(item) #using this function to add items ti inventory to avoid repetition

def showing_items(): # this function goes through every item in players inventory
    for i in inventory:
        print (i)

def profile(): # this function prints the players profile
    print ("--- Player profile ---")
    print (f"Name: {name}")
    print (f"Age: {age}")
    print (f"Inventory:")
    showing_items()
    
while True: # looping the program untill user input an empty string
    if age < 12: # checking age
        print ("Yikes! Sorry! You're too young for this game! Try again in a few years!")
        break

    print ("\nOptions: 1 Add items to inventory, 2 Check inventory and 3 Prints player profile.\n") # printing menu
    command = input("Command: ") # asking user for a command
    if command == "": # if empty string end program
        print (f"See you again {name}...")
        break

    if command == "1": # first option
        new_item = input(f"What item would you like to add? ") # asking user for item
        adding_item(new_item) # addig item using adding_item function
        print (f"Added {new_item} to inventory!") # printing what item added to user

    elif command =="2": #showing user inventory
        print ("Your invetory is... interesting to say the least.\nHeres what you have:")
        showing_items() # printing user inventory using showing_items function

    elif command == "3": 
        profile() # printing profile using profile function