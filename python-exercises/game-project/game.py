import random # lets the game generate random scenarios and outcomes
import os # gives access to operating system commands
import ast # changes string list into actual list
from game_objects import Item, Player, Room

inventory = [] # players starting inventory
knight_inventory = ["Sword", "Helmet", "Chestplate", "Leggings", "Strange Stew", "Secret Note"] # items owned by the knight
health = 100 # players starting health
level = 0 # players starting level
choices = ["dungeon", "courtyard", "tower", "tower_chamber"] # locations that haven't been completed yet
dungeon_items = [] # keeps track of dungeon items
courtyard_items = [] # keeps track of courtyard items
tower_items = [] # keeps track of tower items
chamber_items = [] # keeps track of chamber items
good_choices = 0 # counts good decisions
bad_choices = 0 # counts bad decisions
knight_status = "none" # remembers what the player did to the knight / this acts as the global version of knight_status

def load_intro():
    with open("intro.txt", "r") as file: # opening intro.txt a READ and printing whats inside
        intro = file.read()
    return intro

def load_instructions():
    with open("instructions.txt", "r") as file:
        instructions = file.read()
    return instructions

def save_game(): # saving all items, choices, locations, player profile etc.. into save.txt
    with open("save.txt", "w") as file: # creates / overwrites a new file "save.txt" and writes all below mentioned stuff
        file.write(player.name + "\n")
        file.write(str(player.age) + "\n")
        file.write(str(player.inventory) + "\n")
        file.write(str(player.health) + "\n")
        file.write(str(player.level) + "\n")
        file.write(player.location.name + "\n")
        file.write(knight_status + "\n")
        file.write(str(choices) + "\n")
        file.write(str(good_choices) + "\n")
        file.write(str(bad_choices) + "\n")
        file.write(str(dungeon_items) + "\n")
        file.write(str(courtyard_items) + "\n")
        file.write(str(tower_items) + "\n")

        if starting_room.item is not None: # if the room still has an item
            file.write("True\n")
        else: file.write("False\n")

        if dungeon_room.item is not None:
            file.write("True\n")
        else: file.write("False\n")

        if courtyard_room.item is not None:
            file.write("True\n")
        else: file.write("False\n")

        if tower_room.item is not None:
            file.write("True\n")
        else: file.write("False\n")

def load_game(): # loads the games
    global choices, knight_status, good_choices, bad_choices, dungeon_items, courtyard_items, tower_items

    cleaned_lines = [] # store here clean version
    with open("save.txt", "r") as file: # opens save.txt in read mode
        lines = file.readlines() # reads save.txt
        for line in lines: # a loop to append whatever is saved into cleaned_lines in a clean way
            cleaned_lines.append(line.strip())

    rooms = { # turning rooms into dict. 
    "Castle": starting_room,
    "Dungeon": dungeon_room,
    "Courtyard": courtyard_room,
    "Tower": tower_room,
    "Tower Chamber": tower_chamber_room
    }

    loaded_name = cleaned_lines[0]
    loaded_age = int(cleaned_lines[1])
    loaded_inventory = ast.literal_eval(cleaned_lines[2]) # ast.literal_eval changes a string to list
    loaded_health = int(cleaned_lines[3])
    loaded_level = int(cleaned_lines[4])
    loaded_location = cleaned_lines[5]
    loaded_knight_status = cleaned_lines[6]
    loaded_choices = ast.literal_eval(cleaned_lines[7])
    loaded_good_choices = int(cleaned_lines[8])
    loaded_bad_choices = int(cleaned_lines[9])
    loaded_dungeon_items = ast.literal_eval(cleaned_lines[10])
    loaded_courtyard_items = ast.literal_eval(cleaned_lines[11])
    loaded_tower_items = ast.literal_eval(cleaned_lines[12])
    loaded_starting_item = cleaned_lines[13]
    loaded_dungeon_item = cleaned_lines[14]
    loaded_courtyard_item = cleaned_lines[15]
    loaded_tower_item = cleaned_lines[16]

    # making sure loaded values get saved

    player.name = loaded_name
    player.age = loaded_age
    player.inventory = loaded_inventory
    player.health = loaded_health
    player.level = loaded_level
    player.location = rooms[loaded_location]
    knight_status = loaded_knight_status
    choices = loaded_choices
    good_choices = loaded_good_choices
    bad_choices = loaded_bad_choices
    dungeon_items = loaded_dungeon_items
    courtyard_items = loaded_courtyard_items
    tower_items = loaded_tower_items

    if loaded_starting_item == "True": # checking if user doesnt have starting item
        starting_room.item = old_map
    else:
        starting_room.item = None

    if loaded_dungeon_item == "True": # checking if user doesnt have dungeon item
        dungeon_room.item = unlit_torch # adds unlit_torch into dungeon_rom.item
    else:
        dungeon_room.item = None

    if loaded_courtyard_item == "True":
        courtyard_room.item = lighter
    else:
        courtyard_room.item = None
    print ("Game loaded.")

def clear_screen(): # clears previous terminal text
    os.system("cls" if os.name == "nt" else "clear") # cls for Windows, clear for macOS/Linux

def take_damage(damage): # removes health from player
    player.health -= damage
    if player.health < 1: # normal events can't kill the player
        player.health = 1

def add_good_choice(): # records good decisions
    global good_choices
    good_choices += 1

def add_bad_choice(): # records bad decisions
    global bad_choices
    bad_choices += 1

def heal(life): # restores player health
    player.health += life
    if player.health > 100: # stops health from going over 100
        player.health = 100

def add_item(item): # gives an item to player
    player.inventory.append(item)

def pack_item(): # asks player for an item and adds it to inventory
    item = input("What item would you like to pack? ").strip()

    if item:
        add_item(item)
        print(f"Added {item} to your inventory.")
    else: print("Please enter an item name.")

def collect():

    if player.location.item is not None:
        item_name = player.location.item.name
        player.collect_item()

        if player.location.name == "Dungeon":
            add_dungeon_item(item_name)

        elif player.location.name == "Courtyard":
            add_courtyard_item(item_name)

        elif player.location.name == "Tower":
            add_tower_item(item_name)

        return f"You collected: {item_name}"
    else: return "No item to collect."

def quit_game(): # displays goodbye message when player quits
    print(f"See you again {player.name}...")

def add_dungeon_item(item): # remembers dungeon loot
    dungeon_items.append(item)

def add_courtyard_item(item): # remembers courtyard loot
    courtyard_items.append(item)

def add_tower_item(item): # remembers tower loot
    tower_items.append(item)

def show_dungeon_items(): # shows items found in dungeon
    if not dungeon_items: # if dungeon_items is empty
        print("No items found here.")
        print("")

    for item in dungeon_items: # if its not empty
        print(item)

def show_courtyard_items(): # shows items found in courtyard
    if not courtyard_items:
        print("No items found here.")
        print("")

    for item in courtyard_items:
        print(item)

def show_tower_items(): # shows items found in tower
    if not tower_items:
        print("No items found here.")
        print("")

    for item in tower_items:
        print(item)

def level_up(level_up): # increases player level
    player.level += level_up
    if player.level >= 5:
        print("Congrats! Level 5!")

def show_items(): # displays players inventory
    if not player.inventory: # if players inventory is empty
        print("Empty inventory..")
        print("")
    else:
        for item in player.inventory:
            print(f"Item: {item}")

def remove_knight_inv(item): # removes item from knight
    knight_inventory.remove(item)

def remove_player_inv(item): # removes item from player
    player.inventory.remove(item)


def profile(): # displays player information
    print(f"\n", ("-" * 5), " Player profile ", "-" * 5, f"\n")
    print(
f" " * 6, f"Name: {player.name}\n",
" " * 5, f"Age: {player.age}\n",
" " * 5, f"Health: {player.health}\n",
" " * 5, f"Level: {player.level}\n",
" " * 5, f"Location: {player.location.name}\n",
 " " * 5, "Inventory:")
    
    show_items()

def dungeon(): # controls random dungeon scenarios
    scenario = random.randint(1, 3) # chooses one of three events
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

Type "collect" to pick the torch up.
""")
        take_damage(15)

    elif scenario == 2:

        print("""
As you keep walking, you notice one of the stone walls looks slightly different from the others.
You push against it and a hidden doorway slowly opens.

Inside is a tiny storage room covered in dust.
Most of it has already been looted, but an old unlit torch is still hanging from the wall.

It might be useful later.

Type "collect" to pick the torch up.
""")

    else:

        print("""
Further down the hallway, you almost trip over something lying on the ground.
You look down and realise it's the remains of another adventurer.

Nearby, you notice an old unlit torch.
It isn't exactly impressive, but hopefully it will help.

Type "collect" to pick the torch up.
""")

def courtyard(): # controls courtyard events
    global knight_status # use global version of knight_status which is called at the beginning
    scenario = random.randint(1, 3) # chooses one random courtyard event

    if scenario == 1:
        print('''
You step into the courtyard.
The stone floor is cracked and covered in moss.

In the middle sits an old fountain, somehow still running.
The water looks unusually clear.
As you get closer, you notice fresh footprints around it.

Do you:

1. Drink from the fountain
2. Inspect the footprint
3. Leave it alone
''')

        while True: # starts another loop for more desicions
            courtyard_choice = int(input("Choice: "))
            clear_screen() # clear screen for nicer preview

            if courtyard_choice == 3:
                print("""
As you're leaving the courtyard you notice a lighter beside a bush.

Type "collect" to pick the lighter up.
""")
                break

            elif courtyard_choice == 1:
                courtyard_chance = random.randint(1, 3) # has 3 different random scenarios
                if courtyard_chance == 1:
                    print('''

You take a sip from the fountain..
It tastes strangely good and it makes you feel better.
As you're leaving the courtyard you notice a lighter beside a bush.

Type "collect" to pick the lighter up.
''')
                    level_up(5)
                    break

                else:
                    print('''
You take a sip from the fountain..

It tastes horrible and you start feeling dizzy.
You wobble back to the door and leave the courtyard, but you notice a lighter near a bush.

Type "collect" to pick the lighter up.
''')
                    add_bad_choice()
                    take_damage(20)
                    break

            elif courtyard_choice == 2:
                print('''
The footsteps lead you to an abandoned storage unit.

You find a lighter!

Type "collect" to pick the lighter up.
''')
                add_good_choice()
                level_up(5)
                break
            else: # incase user inputs something else
                print("Not a valid choice.")

    elif scenario == 2:

        print('''

You walk deeper into the courtyard and notice an old wooden chest under a dead tree.
The lock is rusty, but still intact.

Next to the chest is a skeleton holding a small note.

The note reads:
"Some things are locked for a reason."

Do you:

1. Try to force the chest open
2. Search the skeleton
3. Leave the chest and skeleton alone
''')

        while True:

            courtyard_choice = int(input("Choice: "))

            clear_screen()

            if courtyard_choice == 3:

                print("""
You leave the chest and skeleton alone.
As you're leaving the courtyard you notice a lighter near a bush.

Type "collect" to pick the lighter up.
                """)

                break

            elif courtyard_choice == 2:

                print('''
You search the skeleton, but find nothing besides a lighter.

Type "collect" to pick the lighter up.
''')
                level_up(5)
                break

            elif courtyard_choice == 1:

                print('''

You grab the rusty lock and pull as hard as you can.

For a moment, nothing happens.
Then the lock suddenly snaps.

You open the chest and find a lighter!

Type "collect" to pick the lighter up.
''')
                level_up(5)
                break

            else:

                print("Not a valid choice.")

    else: # wounded knight scenario

        print('''
You hear someone breathing heavily behind a broken stone wall.
You find a wounded knight sitting against it.

His armor is damaged and there is blood on the ground.
He looks at you and says:

Guts: "Please... help me."

Do you:

1. Help the knight
2. Search his belongings
3. Walk away

''')

        while True:

            courtyard_choice = int(input("Choice: "))

            clear_screen()

            if courtyard_choice == 3:

                print('''

You look at the wounded knight for a moment.
You decide you've already got enough problems of your own.
As you're walking away you notice a lighter near a bush.

Type "collect" to pick the lighter up.
''')
                knight_status = "ignored" # remembers choice for final chamber
                break

            elif courtyard_choice == 2:
                print("You try to search his pockets...")

                courtyard_chance = random.randint(1, 4)

                if courtyard_chance == 1:

                    print('''

The knight slowly falls asleep.
You carefully search through his belongings and notice a lighter.

Type "collect" to pick the lighter up.
''')

                    knight = Player('Guts', 32, knight_inventory, 25, 30, courtyard_room)
                    knight_status = "angered"
                    add_bad_choice()
                    level_up(5)
                    break

                else:
                    knight = Player('Guts', 32, knight_inventory, 25, 30, courtyard_room)

                    print('''

You reach toward the knight's belongings.
His eyes suddenly open.

Guts: "Seriously?"

Before you can react, he slices your hand.
You pull yourself away and run back toward the castle.

Guts: "Go ahead... run!"

Guts: "I'll remember you."

As you're running you see a lighter in a box.

Type "collect" to pick the lighter up.
''')

                    knight_status = "angered"
                    add_bad_choice()
                    take_damage(20)
                    break

            elif courtyard_choice == 1:
                print('''
You try to help the knight the best way you can..
You look around and find an old medkit that luckily hasn't been used!

You give the knight some medication and bandage him up.

Guts: "Thank you! I can't believe I was almost taken out by some goblins! Tsk."

Guts: "There's a lighter beside me. Take it if you need it."

Type "collect" to pick the lighter up.
''')

                knight = Player('Guts', 32, knight_inventory, 100, 30, courtyard_room)
                knight_status = "helped"
                add_good_choice()
                level_up(5)
                break

            else:
                print("Not a valid choice.")



def tower(): # controls tower event

    print('''
You climb the spiral staircase of the tower.
The higher you go, the darker it gets.

Eventually you reach a completely dark floor.
You can barely see your own hands.

Do you:
1. Try to continue through the darkness
2. Search your inventory for something useful
3. Go back downstairs
''')

    while True:
        choice = int(input("Choice: "))
        if choice == 3:
            print('''
Feeling scared you head back downstairs.
On your way down you stumble and hurt yourself.
''')
            add_bad_choice()
            take_damage(5)
            break

        elif choice == 2:
            print('''
You stop and think for a moment.
Walking blindly through the tower probably isn't the smartest idea.

You search through your inventory, hoping you brought something that could help.
''')
            show_items()

            if "Unlit Torch" in player.inventory and "Lighter" in player.inventory: # checking if user has correct items
                print('''
You pull out the unlit torch and the lighter.
After a few tries, the torch finally catches fire.

The dark hallway lights up around you.
You can now see an old wooden door at the end of the corridor that you completely missed before.
Looks like this tower might actually be hiding something.
''')
                remove_player_inv("Unlit Torch")
                add_item("Lit Torch")
                add_tower_item("Lit Torch")
                add_good_choice()
                break

            else:
                print('''
You search through your inventory and find nothing useful..
Well, nothing useful for lighting up an ancient tower anyway.

You decide it might be smarter to check the other rooms and come back again..
''')
                break
        elif choice == 1:

            print('''
You take a deep breath and keep walking forward.
You can barely see anything, so you keep one hand against the cold stone wall.

After a few steps, the floor suddenly disappears beneath you.
You stumble down a short flight of stairs and hit the ground hard.

You manage to get back up, but that definitely hurt.
''')
            break
        else:
            print("Not a valid choice.")



def tower_chamber(): # final area and ending
    global knight_status # inside this function, when i use/change knight_status, i mean the global version
    print('''
You return to the top of the tower.
With the hallway finally lit, you walk toward the old wooden door.

You push against it.
The hinges scream as the door slowly opens.

Behind it is a huge stone chamber.
Cold air blows through cracks in the walls.

On the other side of the room is a massive iron gate.
Through the small gaps in the gate you can see daylight.

This has to be the way out.
''')

    if knight_status == "none": # guarantees everyone gets the knight decision
        print('''
Before you reach the gate, you hear someone coughing behind you.

You turn around.
A wounded knight is sitting against the stone wall.

Guts: "Hey... you."

Guts: "Could use a hand over here."

Do you:
1. Help the knight
2. Leave him alone
3. Search his belongings
''')

        while True:
            chamber_choice = int(input("Choice: "))
            clear_screen()
            if chamber_choice == 1:
                print('''
You kneel beside the wounded knight.
You find some old bandages nearby and help patch up his wounds. After a while, he slowly manages to stand.

Guts: "Didn't think anyone in this place would actually stop to help me."

Guts: "Name's Guts."

Guts: "I owe you one."
''')

                knight_status = "helped"
                add_good_choice()
                break

            elif chamber_choice == 2:
                print('''
You look at the wounded knight for a moment.

You decide you've already got enough problems of your own.
You leave him behind and walk toward the gate.
''')
                knight_status = "ignored"
                add_bad_choice()
                break

            elif chamber_choice == 3:
                print('''
You notice a few useful things attached to the knight's armor.
You reach toward them.
His hand suddenly grabs your wrist.

Guts: "Seriously?"

You quickly pull yourself free and run toward the other side of the chamber.

Guts: "Go ahead."

Guts: "Run."

Guts: "I'll be waiting."
''')
                knight_status = "angered"
                add_bad_choice()
                break
            else: print("Not a valid choice.")

    if knight_status == "helped": # good ending
        print(f'''
You finally reach the massive iron gate.
You push against it.

Nothing.

You try again, but the gate barely moves.
Suddenly you hear footsteps behind you.

Guts: "Need a hand?"

You turn around and see the knight walking toward you.
He grabs the other side of the gate. Together, you push as hard as you can.
The old gate begins to move. Light pours into the chamber.

For the first time since waking up, you can see the world outside the castle.

Guts: "Told you I'd see you around."

The two of you step outside.
You escaped the castle!

Good choices: {good_choices}

Bad choices: {bad_choices}

Thanks for playing!
''')

    elif knight_status == "angered": # only ending where player dies

        print(f'''
You reach the massive iron gate. Something is strange.

You can see daylight through the gap. It's already slightly open.
You smile and start walking toward it.

Then you hear footsteps behind you... Slow footsteps.
The knight is standing in the middle of the chamber. You turn around.

Guts: "Remember me?"

Probably shouldn't have tried robbing a wounded knight.
He slowly pulls out his sword.

There is nowhere left to run.

You died.

Good choices: {good_choices}

Bad choices: {bad_choices}

Maybe don't steal from Guts next time.
''')

        player.health = 0 # knight is the only thing that can actually kill player

    else: # neutral ending after ignoring knight
        print(f'''

You reach the massive iron gate.
Nobody is coming to help you.
You push against it as hard as you can.

Nothing...

You step back and try again.
This time the gate moves slightly.

You keep pushing until there is just enough space to squeeze through.
You crawl through the opening and fall onto the grass outside.

For a moment, you just lie there.
Then you look back at the abandoned castle behind you.

Somehow...

You actually made it out.

Alone.

You escaped the castle!

Good choices: {good_choices}

Bad choices: {bad_choices}

Thanks for playing!
''')
name = "Pierre"#input("Hello traveler.. What is your name? ")
age = 18# int(input(f"\nOh.. well hello {name}, good to meet you! May I ask your age? "))

unlit_torch = Item("Unlit Torch", 2)
apple = Item("Apple", 1)
lighter = Item("Lighter", 1)
old_map = Item("Old Map", 1)

starting_room = Room("Castle", old_map) # creates starting room
dungeon_room = Room("Dungeon", unlit_torch) # creates dungeon_room with unlit torch
courtyard_room = Room("Courtyard", lighter) # creates courtyard_room with lighter

tower_room = Room("Tower", None) # creates tower_room without an item
tower_chamber_room = Room("Tower Chamber", None)# creates tower_chamber_room without an item

player = Player(name, age, inventory, health, level, starting_room) # creates main player and puts him in starting room
clear_screen()

def show_choices(): # shows locations that are currently available
    print("\nWhere will you go?")

    if "dungeon" in choices: # checks if dungeon is not visited
        print("1. Enter the dungeon")
    else: print ("1. Return to the dungeon.") # if its visited

    if "courtyard" in choices:
        print("2. Walk into the courtyard")
    else: print ("2. Return to the courtyard.")

    if "tower" in choices:
        print("3. Climb the tower")
    else: print ("3. Return to the tower.")

    if "dungeon" not in choices and "courtyard" not in choices and "tower" not in choices and "tower_chamber" in choices:
        print("4. Enter the tower chamber") # final location appears after other areas are finished

    print("Other choices: collect, pack, inventory, profile, instructions, save, load, quit")

if player.age < 12:
    print("Yikes! Sorry.. you're too young for this game!")

else:
    print(load_intro())

    while True: # main game loop
        show_choices()
        choice = input("Choice: ").strip().lower()
        clear_screen()

        if choice == "quit" or choice == "":
            quit_game()
            break

        elif choice == "pack":
            pack_item()

        elif choice == "inventory":
            show_items()

        elif choice == "profile":
            profile()

        elif choice == "collect":
            print (collect())

        elif choice == "instructions":
            print (load_instructions())

        elif choice == "save":
            save_game()
            print ("Game saved.")

        elif choice == "load":
            load_game()

        elif choice == "1":

            if "dungeon" not in choices:  # already visited
                player.move(dungeon_room)
                print('''
Hmm seems like we've already been to the dungeon,
but I guess we can check if we left something behind.
        ''')

                if dungeon_room.item is not None:
                    print("""
You notice the Unlit Torch is still here.

Type "collect" to pick the Unlit Torch up.
        """)
                else: print("Looks like there's nothing left to collect here.")

            else: # first dungeon visit
                player.move(dungeon_room)
                dungeon()
                choices.remove("dungeon")

        elif choice == "2":
            player.move(courtyard_room)
            if "courtyard" not in choices:
                print('''
Hmm seems like we've already been to the courtyard,
but I guess we can check if we left something behind.
''')
                if courtyard_room.item is not None:
                    print("""
You notice the Unlit Torch is still here.

Type "collect" to pick the Unlit Torch up.
""")
                else: print("Looks like there's nothing left to collect here.")

            else: # first courtyard visit
                player.move(courtyard_room)
                courtyard()
                choices.remove("courtyard") # marks courtyard completed

        elif choice == "3":
            if "tower" not in choices:
                print('''

Hmm seems like we've already climbed the tower,
but I guess we can check if we left something behind.

Here's what we got from the tower:
''')
                player.move(tower_room)
                show_tower_items()

            elif "Unlit Torch" in player.inventory and "Lighter" in player.inventory:
                print('''
This seems pretty scary, but it looks like we have what we need now.
You pull the Lighter and Unlit Torch out and set the Torch on fire.
It's pretty darn dark in there.
''')
                player.move(tower_room)
                tower()

                if "Lit Torch" in player.inventory: # tower only finishes if player successfully lights torch
                    choices.remove("tower")

            else:
                print('''

We shouldn't go there yet.
It's very dark and we seem like we're missing some items.

Maybe we should explore somewhere else first.
''')
                
        elif choice == "4":
            if "dungeon" not in choices and "courtyard" not in choices and "tower" not in choices and "tower_chamber" in choices:
                player.move(tower_chamber_room)
                tower_chamber()
                choices.remove("tower_chamber")
                break # chamber contains final ending so game finishes here
            else:
                print("You can't go there yet.")
        else:
            print("\nInvalid input..")
            print("Please choose one of the available choices.")