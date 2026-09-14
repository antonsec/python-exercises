import random # importing random, gonna use this throughout the project to randomise items, moments..

inventory = [] # default values
knight_inventory = ["Sword", "Helmet", "Chestplate", "Leggings", "Strange Stew", "Secret Note"] 
health = 100
level = 0
choices = ["dungeon", "courtyard", "tower"]
dungeon_items = []
courtyard_items = []


class Players: # adding class Players and giving player name, age, inventory, health and level
    def __init__(self, name, age, inventory, health, level): # init function for creating the player
        self.name = name # setting self.name as name so we can use ex. player.name, player.age etc...
        self.age = age
        self.inventory = inventory
        self.health = health
        self.level = level


def take_damage(damage): # this function removes health from player whenever they take damage
    player.health -= damage

    if player.health <= 0: # checking if player health reaches 0 or below
        print("You died.. Ending game.")
        return True

    return False

def heal(life):
    player.health += life

    if player.health > 100:
        player.health = 100


def add_item(item): # this function adds items to inventory to avoid repetition
    player.inventory.append(item)

def add_dungeon_item(item):
    dungeon_items.append(item)

def add_courtyard_item(item):
    courtyard_items.append(item)

def show_dungeon_items():
    if not player.inventory: # checking if inventory empty
        print("Empty inventory..")
        print("")
    for item in dungeon_items:
        print (item)

def show_courtyard_items():
    if not player.inventory: # checking if inventory empty
        print("Empty inventory..")
        print("")
    for item in courtyard_items:
            print (item)

def level_up(level_up): # this function adds levels to player
    player.level += level_up

    if player.level >= 5: # checking if player has reached level 5
        print("Congrats! Level 5!")

def showing_items(): # this function goes through every item in players inventory and prints them
    if not player.inventory: # checking if inventory empty
        print("Empty inventory..")
        print("")

    else:
        for item in player.inventory: # printing inventory if it's not empty
            print(f"Item: {item}")


def profile(): # this function prints the players profile
    print(f"\n", ("-" * 5), " Player profile ", "-" * 5, f"\n")

    print(
        f" " * 6,f"Name: {player.name}\n",
        " " * 5, f"Age: {player.age}\n",
        " " * 5, f"Health: {player.health}\n",
        " " * 5, f"Level: {player.level}"
    )

    print("")
    print(" " * 6, "Inventory:")

    showing_items()

def dungeon(): # dungeon function, random scenario happens whenever player enters
    scenario = random.randint(1, 3)

    print("""
You enter the dungeon questioning why are you even here in the first place..
As you walk across the hallway, you smell.. almost taste the eerie scent of goblins.
You've encountered goblins before, but you have a feeling this isn't gonna end well.
""")

    if scenario == 1:
        print("""
As you keep walking down the hallway a goblin reaches out and scratches your arm.
You get startled and fall down a flight of stairs.
You find an unlit torch and decide to walk back to the castle.
""")

        take_damage(10) # removing 10 health from player
        add_item("Unlit Torch") # adding torch into players inventory
        add_dungeon_item("Unlit Torch")

    elif scenario == 2:
        print("""
As you keep walking down the hallway a goblin reaches out and tries to scratch your arm.
You get startled, but dodge his attack and quickly head back.
On the way back you find an unlit torch and decide to walk back to the castle.
""")

        add_item("Unlit Torch") # adding torch into players inventory
        add_dungeon_item("Unlit Torch")

    else:
        print("""
As you keep walking down the hallway a goblin reaches out and tries to scratch your arm.
You get startled, but dodge his attack and quickly head back.
On the way back you find a dagger and decide to walk back to the castle.
""")

        add_item("Dagger") # adding dagger into players inventory
        add_dungeon_item("Dagger")


def courtyard(): # dungeon function, random scenario happens whenever player enters
    scenario = random.randint(1, 3)

    if scenario == 1:
        print ('''
You step into the courtyard.
The stone floor is cracked and covered in moss.
In the middle sits an old fountain, somehow still running.
The water looks unusually clear.
As you get closer, you notice fresh footprints around it.

Do you:
1. Drink from the fountain
2. Inspect the footprints
3. Leave it alone
''')
        while True:
            courtyard_choice = int(input("Choice: "))
            if courtyard_choice == 3:
                print ("You leave the courtyard...")
                break

            elif courtyard_choice == 1:
                courtyard_chance = random.randint(1,3)
                if courtyard_choice == 1:
                    print ('''
You take a sip from the fountain..
It tastes strangley good and it makes you feel better.
''')
                    heal(10)
                    level_up(5)
                    break
                else:
                    print ('''
You take a sip from the fountain..
It tastes horrible and you start feeling dizzy
                    ''')
                    take_damage(20)
                    break

            elif courtyard_choice == 2:
                print ('''
The footsteps lead you to an abandoned storage unit.
You find a lighter and an apple!
Happy with your finding you head back to where you started
''')
                add_item("Apple")
                add_item("Lighter")
                add_courtyard_item("Apple")
                add_courtyard_item("Lighter")
                level_up(2)
                break


    elif scenario == 2:
            print ('''
You walk deeper into the courtyard and notice an old wooden chest under a dead tree.
The lock is rusty, but still intact.
Next to the chest is a skeleton holding a small note.
The note reads:
“Some things are locked for a reason.”

Do you:
1. Try to force the chest open
2. Search the skeleton
3. Leave the chest and skeleton alone''')
            
            while True:
                courtyard_choice = int(input("Choice: "))
                if courtyard_choice == 3:
                    print ("You leave the chest and skeleton alone..")
                    break

                elif courtyard_choice == 2:
                    print ('''
You search the skeleton, but find nothing besides the note...
You put it in your pocket and head back.''')
                    add_item("Note")
                    add_courtyard_item("Note")
                    level_up(2)
                    break

    elif scenario == 3:
                print ('''
You hear someone breathing heavily behind a broken stone wall.
You find a wounded knight sitting against it.
His armor is damaged and there is blood on the ground.
He looks at you and says:
“Please... help me.”

Do you:
1. Help the knight
2. Search his belongings
3. Walk away
''')
                while True:
                    courtyard_choice = int(input("Choice: "))
                    if courtyard_choice == 3:
                        print ("You walk quickly away..")
                        break

                    elif courtyard_choice == 2:
                        print ('You try to search his pockets')
                        courtyard_chance = random.randint(1,4)
                        
                        if courtyard_chance == 1:
                            print ('''
The knight falls asleep and you successfully take a gold coin and his helmet!
Feeling lucky you run back..''')
                            add_item("Gold Coin")
                            add_courtyard_item("Gold Coin")
                            level_up(5)
                            break

                        else:
                            print ('''
The knight slices your hand and you lose some health!
You decide to run back before he gains his strength back.''')
                            break
                            
                    elif courtyard_choice == 1:
                        print ('''
You try to help the knight the best way you can..
You look around and find an old medkit that luckily hasn't been used!
You give the knight some medication and bandage him up.
Knight: Thank you! I can't belive I was almost taken out by some goblins! Tsk.
        Anyways thank you for your help.. I'm sure I'll see you around. Heres a gold coin.. It's all I got.
You thank the knight and you both part ways..
        ''')
                        knight = Players('Guts', 32, knight_inventory, 100, 30) # adding player into class Players
                        add_item("Gold Coin")
                        add_courtyard_item("Gold Coin")
                        level_up(5)
                        break

def show_choices(): # this function prints all main choices player can make
    print("\nWhere will you go?")
    if "dungeon" in choices:

        print("1. Enter the dungeon")

    if "courtyard" in choices:
        print("2. Walk into the courtyard")

    if "tower" in choices:
        print("3. Climb the tower")

    print("Other choices: inventory, profile, quit")
    

name = input("Hello traveler.. What is your name? ")
age = int(input(f"\nOh.. well hello {name}, good to meet you! May I ask your age? "))

player = Players(name, age, inventory, health, level) # adding player into class Players


if player.age < 12: # checking if age < 12 else: starts game
    print("Yikes! Sorry.. you're too young for this game!")

else:
    print("""
You wake up inside an abandoned castle.
A torch flickers beside three doorways.
""")

    while True: # starting game loop
        show_choices()

        choice = input("Choice: ").strip().lower() # removes extra spaces and makes uppercase/lowercase irrelevant

        if choice == "quit" or choice == "": # if user inputs quit or empty line ending program
            print(f"See you again {player.name}...")
            break

        elif choice == "inventory": # if input inventory shows inventory
            showing_items()

        elif choice == "profile": # if input profile shows profile
            profile()

        elif choice == "1": # entering dungeon
            if "dungeon" not in choices:
                print (f'''
Hmm seems like we've aready been to the dungeon..
Heres what we got from the dungeon:
''')
                show_dungeon_items()
            else:
                dungeon()
                choices.remove('dungeon')

            if player.health <= 0: # ending game if player died
                break

        elif choice == "2":
            if "courtyard" not in choices:
                print (f'''
\nHmm seems like we've aready been to the courtyard..
Heres what we got from the courtyard:
                ''')
                show_courtyard_items()
            else:
                courtyard()
                choices.remove("courtyard")

        elif choice == "3":
            print("You climb the tower.")

        else: # if input is not correct restarts loop and prints
            print("\nInvalid input..")
            print("Please choose 1, 2, 3, inventory, profile, or quit.")