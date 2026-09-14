import random # importing random, gonna use this throughout the project to randomise items, moments..
import os # importing operating system module

inventory = [] # default values
knight_inventory = ["Sword", "Helmet", "Chestplate", "Leggings", "Strange Stew", "Secret Note"] 
health = 100
level = 0
choices = ["dungeon", "courtyard", "tower"]
dungeon_items = []
courtyard_items = []
tower_items = []


class Players: # adding class Players and giving player name, age, inventory, health and level
    def __init__(self, name, age, inventory, health, level): # init function for creating the player
        self.name = name # setting self.name as name so we can use ex. player.name, player.age etc...
        self.age = age
        self.inventory = inventory
        self.health = health
        self.level = level


def clear_screen(): # clears terminal
    os.system("cls" if os.name == "nt" else "clear") # run the correct terminal clear command depending on the operating system


def take_damage(damage): # this function removes health from player whenever they take damage
    player.health -= damage


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

def add_tower_item(item):
    tower_items.append(item)


def show_dungeon_items():
    if not dungeon_items:
        print("No items found here.")
        print("")

    for item in dungeon_items:
        print(item)


def show_courtyard_items():
    if not courtyard_items: # checking if inventory empty
        print("No items found here.")
        print("")

    for item in courtyard_items:
        print(item)

def show_tower_items():
    if not tower_items: # checking if inventory empty
            print("No items found here.")
            print("")

    for item in tower_items:
        print(item)

def level_up(level_up): # this function adds levels to player
    player.level += level_up

    if player.level >= 5: # checking if player has reached level 5
        print("Congrats! Level 5!")


def show_items(): # this function goes through every item in players inventory and prints them
    if not player.inventory: # checking if inventory empty
        print("Empty inventory..")
        print("")

    else:
        for item in player.inventory: # printing inventory if it's not empty
            print(f"Item: {item}")


def remove_knight_inv(item):
    knight_inventory.remove(item)

def remove_player_inv(item):
    player.inventory.remove(item)


def profile(): # this function prints the players profile
    print(f"\n", ("-" * 5), " Player profile ", "-" * 5, f"\n")

    print(
        f" " * 6, f"Name: {player.name}\n",
        " " * 5, f"Age: {player.age}\n",
        " " * 5, f"Health: {player.health}\n",
        " " * 5, f"Level: {player.level}"
    )

    print("")
    print(" " * 6, "Inventory:")

    show_items()


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
You find an unlit torch and a lighter and decide to walk back to the castle.
""")

        take_damage(15) # removing 15 health from player
        add_item("Unlit Torch") # adding torch into players inventory
        add_item("Lighter")
        add_dungeon_item("Unlit Torch") # adding torch into dungeon items
        add_dungeon_item("Lighter")

    elif scenario == 2:
        print("""
As you keep walking, you notice one of the stone walls looks slightly different from the others.
You push against it and a hidden doorway slowly opens.
Inside is a tiny storage room covered in dust. Most of it has already been looted, but an old torch is still hanging from the wall.
You take the torch and head back toward the castle.
""")

        add_item("Unlit Torch") # adding torch into players inventory
        add_dungeon_item("Unlit Torch")

    else:
        print("""
Further down the hallway, you almost trip over something lying on the ground.
You look down and realise it's the remains of another adventurer.
Beside them is a rusty dagger and a lighter. It isn't exactly impressive, but it's definitely better than fighting goblins with your bare hands.
You take the lighter and dagger and quickly head back.
""")

        add_item("Rusty Dagger") # adding Unlit Torch into players inventor
        add_item("Lighter")
        add_dungeon_item("Rusty Dagger")
        add_dungeon_item("Lighter")


def courtyard(): # dungeon function, random scenario happens whenever player enters
    scenario = random.randint(1, 3) # 1-3 random s enario

    if scenario == 1: # if randomizer hits 1
        print('''
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

        while True: # new loop for new choice
            courtyard_choice = int(input("Choice: "))

            clear_screen() # clearing courtyard choices after player makes a choice

            if courtyard_choice == 3:
                print("You leave the courtyard...")
                break

            elif courtyard_choice == 1:
                courtyard_chance = random.randint(1, 3)

                if courtyard_chance == 1: # a about 33% chance  of healing and leveling up
                    print('''
You take a sip from the fountain..
It tastes strangley good and it makes you feel better.
''')

                    heal(10)
                    level_up(5)
                    break

                else: # about 67% chance of feeling worse and taking damage
                    print('''
You take a sip from the fountain..
It tastes horrible and you start feeling dizzy.
You wobble back to the door and leave the courtyard.
''')

                    take_damage(20)
                    break

            elif courtyard_choice == 2:
                print('''
The footsteps lead you to an abandoned storage unit.
You find a lighter and an apple!
Happy with your findings you head back to where you started.
''')

                add_item("Apple")
                add_item("Lighter")
                add_courtyard_item("Apple")
                add_courtyard_item("Lighter")
                level_up(2)
                break


    elif scenario == 2:
        print('''
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

            clear_screen() # clearing courtyard choices after player makes a choice

            if courtyard_choice == 3:
                print("You leave the chest and skeleton alone..")
                break

            elif courtyard_choice == 2:
                print('''
You search the skeleton, but find nothing besides the note...
You put it in your pocket and head back.''')

                add_item("Note")
                add_courtyard_item("Note")
                level_up(2)
                break

            elif courtyard_choice == 1:
                print('''
You grab the rusty lock and pull as hard as you can.
For a moment, nothing happens.
Then the lock suddenly snaps.
You open the chest and find a small pile of coins, an old healing potion and a lighter.
Just as you reach inside, a hidden needle shoots out from the side of the chest and cuts your hand.
Probably should've listened to the note.
''')

                take_damage(15)
                add_item("Healing Potion")
                add_item("Coins")
                add_item("Lighter")
                add_courtyard_item("Healing Potion")
                add_courtyard_item("Coins")
                add_courtyard_item("Lighter")
                level_up(5)
                break

            else:
                print("Not a valid choice.")


    else:
        print('''
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

            clear_screen() # clearing knight choices after player makes a choice

            if courtyard_choice == 3:
                print("You quickly walk away..")
                break

            elif courtyard_choice == 2:
                print("You try to search his pockets")

                courtyard_chance = random.randint(1, 4)

                if courtyard_chance == 1: # a 25 % chance
                    print('''
The knight falls asleep and you successfully take a gold coin, a lighter and his helmet!
Feeling lucky you run back.''')

                    knight = Players('Guts', 32, knight_inventory, 25, 30) # creating a new player "knight"
                    remove_knight_inv("Helmet")
                    add_item("Gold Coin")
                    add_item("Helmet")
                    add_item("Lighter")

                    add_courtyard_item("Gold Coin")
                    add_courtyard_item("Helmet")
                    add_courtyard_item("Lighter")
                    level_up(5)
                    break

                else: # a 75% chance the knight retaliates
                    knight = Players('Guts', 32, knight_inventory, 25, 30)
                    print('''
The knight slices your hand and you lose some health!
You decide to run back before he gains his strength back.''')
                    take_damage(20)
                    break

            elif courtyard_choice == 1:
                print('''
You try to help the knight the best way you can..
You look around and find an old medkit that luckily hasn't been used!
You give the knight some medication and bandage him up.

Knight: Thank you! I can't belive I was almost taken out by some goblins! Tsk.
        Anyways thank you for your help.. I'm sure I'll see you around. Heres a gold coin.. It's all I got.

You thank the knight and you both part ways..
''')

                knight = Players('Guts', 32, knight_inventory, 100, 30) # adding player into class Players
                add_item("Gold Coin") # adding gold coin to inventory
                add_courtyard_item("Gold Coin") # and to courtyard items
                level_up(5) # leveling character up
                break
            else:
                print("Not a valid choice.")


def tower():
    print('''
You climb the spiral staircase of the tower.
The higher you go, the darker it gets.
Eventually you reach a completely dark floor.
You can barely see your own hands.

Do you:
1. Try to continue through the darkness
2. Search your inventory for something useful
3. Go back downstairs''')
    while True:
        choice = int(input("Choice: "))
        if choice == 3:
            print ('''
Feeling scared you head back downstairs. On your way down you stumble and hurt yourself.''')
            take_damage(5)
            break

        elif choice == 2:
            print ('''
You stop and think for a moment.
Walking blindly through the tower probably isn't the smartest idea.
You search through your inventory, hoping you brought something that could help.''')
            show_items()

            if "Unlit Torch" in player.inventory and "Lighter" in player.inventory:
                print ('''
You pull out the unlit torch and the lighter.
After a few tries, the torch finally catches fire.
The dark hallway lights up around you.
You can now see an old wooden door at the end of the corridor that you completely missed before.
Looks like this tower might actually be hiding something.''')
                remove_player_inv("Unlit Torch")
                add_item("Lit Torch")
                add_tower_item("Lit Torch")
                break
            else:
                print ('''
You search through your inventory...
Nothing.
Well, nothing useful for lighting up an ancient tower anyway.
You decide it might be smarter to come back another time.''')
                break
        elif choice == 1:
            print ('''
You take a deep breath and keep walking forward.
You can barely see anything, so you keep one hand against the cold stone wall.
After a few steps, the floor suddenly disappears beneath you.
You stumble down a short flight of stairs and hit the ground hard.
You manage to get back up, but that definitely hurt.''')
            take_damage(15)
            break
        else:
            print("Not a valid choice.")
        
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

clear_screen() # clearing name and age questions before starting the game


if player.age < 12: # checking if age < 12 else: starts game
    print("Yikes! Sorry.. you're too young for this game!")

else:
    print("""
You wake up inside an abandoned castle with no memory of how you got there.
The main gates are sealed shut.
Somewhere inside the castle is a way out, but you'll need to explore the surrounding rooms and gather whatever might help you escape.
""")

    while True: # starting game

        show_choices()
        if not choices: # if all locations discovered
            print ("You escaped!!")
            break
        
        choice = input("Choice: ").strip().lower() # removes extra spaces and makes uppercase/lowercase irrelevant
        clear_screen() # clearing main menu after player makes a choice

        if choice == "quit" or choice == "": # if user inputs quit or empty line ending program
            print(f"See you again {player.name}...")
            break

        elif choice == "inventory": # if input inventory shows inventory
            show_items()

        elif choice == "profile": # if input profile shows profile
            profile()

        elif choice == "1": # entering dungeon
            if "dungeon" not in choices: # checking is user has already been in dungeon
                print(f'''
Hmm seems like we've aready been to the dungeon..
Heres what we got from the dungeon:
''')
                show_dungeon_items() # showing what items were gotten in dungeons incase users enters 1 again

            else:
                dungeon()
                if player.health <= 0: # checking if player health reaches 0 or below
                    print("You died.. Ending game.")
                    break
                choices.remove("dungeon") # removing dumgeon from choices listsx

        elif choice == "2":
            if "courtyard" not in choices: # same check
                print(f'''
Hmm seems like we've aready been to the courtyard.
Heres what we got from the courtyard:''')
                show_courtyard_items()
            else:
                courtyard()
                if player.health <= 0: # checking if player health reaches 0 or below
                    print("You died.. Ending game.")
                    break
                choices.remove("courtyard")

        elif choice == "3":
            if "tower" not in choices: # same check
                print(f'''
Hmm seems like we've aready climbed the tower.
Heres what we got from the tower: ''')
                show_tower_items()
            else:
                tower()
                if player.health <= 0: # checking if player health reaches 0 or below
                    print("You died.. Ending game.")
                    break
                choices.remove("tower")

        else: # if input is not correct restarts loop and prints
            print("\nInvalid input..")
            print("Please choose 1, 2, 3, inventory, profile, or quit.")