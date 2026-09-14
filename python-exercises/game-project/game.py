inventory = ["Dagger", "Torch"] 
health = 100

class Players: # adding class Players and giving player name, age and inventory
    def __init__(self, name, age, inventory, health):
        self.name = name
        self.age = age
        self.inventory = inventory
        self.health = health

def profile(): # this function prints the players profile
    print (f"--- Player profile ---")
    print (f"Name: {player.name}")
    print (f"Age: {player.age}")
    print (f"Health: {player.health}")
    print ("")
    print (f"Inventory:")
    showing_items()

def adding_item(item): #  this function to adds items to inventory to avoid repetition
    player.inventory.append(item) 

def showing_items(): # this function goes through every item in players inventory and prints them
        if not player.inventory: # checking if inventory empty
            print (f"Empty inventory..")
            return
        
        for items in player.inventory: # printing inventory if it's not empty
            print (items)


name = input("Hello traveler.. What is your name? ")
age = int(input(f"\nOh.. well hello {name}, good to meet you! May I ask ye age? "))
player = Players(name, age, inventory, health) # adding player into class Players


    
while True: # looping the program untill user input an empty string
    if player.age < 12: # checking age
        print ("Yikes! Sorry.. you're too young for this game! Try again in a few years!")
        break

    print ("\nOptions: 1 Add items to inventory, 2 Check inventory and 3 Prints player profile.\n") # printing menu
    command = input("Command: ") # asking user for a command

    if command == "": # if empty string end program
        print (f"See you again {player.name}...")
        break

    if command == "1": # first option
        new_item = " "
        print ("Alright adding items!\n")
        while new_item != "": # empty line ends adding item program
            new_item = input(f"\nWhat item would you like to add? ")

            if new_item == "":
                print ("\nDone adding items...")
                break
             # asking user for item
            adding_item(new_item) # addig item using adding_item function
            print (f"Added {new_item} to inventory!") # printing what item added to user


    elif command =="2": #showing user inventory
        print ("\nYour invetory is... interesting to say the least.\nHeres what you have:")
        showing_items() # printing user inventory using showing_items function

    elif command == "3": 
        profile() # printing profile using profile function