import random # lets the game generate random scenarios and outcomes
import os # gives access to operating system commands

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


class Players: # blueprint for creating characters
    def __init__(self, name, age, inventory, health, level): # values needed when making a character
        self.name = name # saves characters name
        self.age = age # saves characters age
        self.inventory = inventory # gives character an inventory
        self.health = health # saves characters health
        self.level = level # saves characters level


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
    else:
        print("Please enter an item name.")


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
        " " * 5, f"Level: {player.level}"
    )

    print("")
    print(" " * 6, "Inventory:")
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
You find an unlit torch and a lighter and decide to walk back to the castle.
""")

        take_damage(15)
        add_item("Unlit Torch")
        add_item("Lighter")
        add_dungeon_item("Unlit Torch")
        add_dungeon_item("Lighter")

    elif scenario == 2:
        print("""
As you keep walking, you notice one of the stone walls looks slightly different from the others.
You push against it and a hidden doorway slowly opens.
Inside is a tiny storage room covered in dust.

Most of it has already been looted, but an old torch is still hanging from the wall with a lighter below it.
You take the torch and the lighter and head back toward the castle.
""")

        add_item("Unlit Torch")
        add_dungeon_item("Unlit Torch")

        add_item("Lighter")
        add_dungeon_item("Lighter")

    else:
        print("""
Further down the hallway, you almost trip over something lying on the ground.
You look down and realise it's the remains of another adventurer.
Beside them is a rusty dagger, a lighter and an unlit torch.
It isn't exactly impressive, but it's definitely better than fighting goblins with your bare hands.
You take the lighter and dagger and quickly head back.
""")

        add_item("Rusty Dagger")
        add_item("Lighter")
        add_item("Unlit Torch")
        
        add_dungeon_item("Rusty Dagger")
        add_dungeon_item("Unlit Torch")
        add_dungeon_item("Lighter")


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
2. Inspect the footprints
3. Leave it alone
''')

        while True: # starts another loop for more desicions
            courtyard_choice = int(input("Choice: "))
            clear_screen() # clear screen for nicer preview

            if courtyard_choice == 3:
                print("You leave the courtyard...")
                break

            elif courtyard_choice == 1:
                courtyard_chance = random.randint(1, 3) # has 3 different random scenarios

                if courtyard_chance == 1:
                    print('''
You take a sip from the fountain..
It tastes strangely good and it makes you feel better.
''')

                    add_good_choice()
                    heal(10)
                    level_up(5)
                    break

                else:
                    print('''
You take a sip from the fountain..
It tastes horrible and you start feeling dizzy.
You wobble back to the door and leave the courtyard.
''')

                    add_bad_choice()
                    take_damage(20)
                    break

            elif courtyard_choice == 2:
                print('''
The footsteps lead you to an abandoned storage unit.
You find a lighter and an apple!
Happy with your findings you head back to where you started.
''')

                add_good_choice()
                add_item("Apple")
                add_item("Lighter")
                add_courtyard_item("Apple")
                add_courtyard_item("Lighter")
                level_up(2)
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
                print("You leave the chest and skeleton alone..")
                break

            elif courtyard_choice == 2:
                print('''
You search the skeleton, but find nothing besides the note...
You put it in your pocket and head back.
''')

                add_item("Note")
                add_courtyard_item("Note")
                level_up(2)
                break

            elif courtyard_choice == 1:
                print('''
You grab the rusty lock and pull as hard as you can.
For a moment, nothing happens.
Then the lock suddenly snaps.

You open the chest and find a small pile of coins,
an old healing potion and a lighter.

Just as you reach inside, a hidden needle shoots out from the side of the chest and cuts your hand.
Probably should've listened to the note.
''')

                add_bad_choice()
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

    else: # wounded knight scenario
        print('''
You hear someone breathing heavily behind a broken stone wall.
You find a wounded knight sitting against it.
His armor is damaged and there is blood on the ground.

He looks at you and says:

Knight: "Please... help me."

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

You quickly walk away.
''')

                knight_status = "ignored" # remembers choice for final chamber
                break

            elif courtyard_choice == 2:
                print("You try to search his pockets...")

                courtyard_chance = random.randint(1, 4)

                if courtyard_chance == 1:
                    print('''
The knight slowly falls asleep.
You carefully search through his belongings.
You manage to take a gold coin, a lighter and his helmet.

Feeling lucky, you quickly run back.
As you leave, you hear something behind you.
Knight: "..."

Maybe he wasn't completely asleep.
''')

                    knight = Players('Guts', 32, knight_inventory, 25, 30)
                    knight_status = "angered"
                    add_bad_choice()
                    remove_knight_inv("Helmet")
                    add_item("Gold Coin")
                    add_item("Helmet")
                    add_item("Lighter")
                    add_courtyard_item("Gold Coin")
                    add_courtyard_item("Helmet")
                    add_courtyard_item("Lighter")
                    level_up(5)
                    break

                else:
                    knight = Players('Guts', 32, knight_inventory, 25, 30)

                    print('''
You reach toward the knight's belongings.
His eyes suddenly open.

Knight: "Seriously?"

Before you can react, he slices your hand.
You pull yourself away and run back toward the castle.

Knight: "Go ahead... run."

Knight: "I'll remember you."
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

Knight: "Thank you! I can't believe I was almost taken out by some goblins! Tsk."

Knight: "Anyways... thank you for your help.
I'm sure I'll see you around.

Here's a gold coin. It's all I've got."

You thank the knight and you both part ways.
''')

                knight = Players('Guts', 32, knight_inventory, 100, 30)
                knight_status = "helped"
                add_good_choice()
                add_item("Gold Coin")
                add_courtyard_item("Gold Coin")
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
You decide it might be smarter to come back another time.
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

            add_bad_choice()
            take_damage(15)
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

Knight: "Hey... you."

Knight: "Could use a hand over here."

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

Knight: "Didn't think anyone in this place would actually stop to help me."

Knight: "Name's Guts."

Knight: "I owe you one."
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
                break

            elif chamber_choice == 3:
                print('''
You notice a few useful things attached to the knight's armor.
You reach toward them.

His hand suddenly grabs your wrist.

Knight: "Seriously?"

You quickly pull yourself free and run toward the other side of the chamber.

Knight: "Go ahead."

Knight: "Run."

Knight: "I'll be waiting."
''')

                knight_status = "angered"
                add_bad_choice()
                break

            else:
                print("Not a valid choice.")

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

Knight: "Remember me?"

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
Nothing.
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


def show_choices(): # shows locations that are currently available
    print("\nWhere will you go?")

    if "dungeon" in choices:
        print("1. Enter the dungeon")

    if "courtyard" in choices:
        print("2. Walk into the courtyard")

    if "tower" in choices:
        print("3. Climb the tower")

    if "dungeon" not in choices and "courtyard" not in choices and "tower" not in choices and "tower_chamber" in choices:
        print("4. Enter the tower chamber") # final location appears after other areas are finished

    print("Other choices: pack, inventory, profile, quit")


name = input("Hello traveler.. What is your name? ")
age = int(input(f"\nOh.. well hello {name}, good to meet you! May I ask your age? "))

player = Players(name, age, inventory, health, level) # creates main player
clear_screen()

if player.age < 12:
    print("Yikes! Sorry.. you're too young for this game!")

else:
    print("""
You wake up inside an abandoned castle with no memory of how you got there.
The main gates are sealed shut.

Somewhere inside the castle is a way out,
but you'll need to explore the surrounding rooms and gather whatever might help you escape.
""")

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

        elif choice == "1":
            if "dungeon" not in choices:
                print('''
Hmm seems like we've already been to the dungeon..
Here's what we got from the dungeon:
''')
                show_dungeon_items()

            else:
                dungeon()
                choices.remove("dungeon") # marks dungeon completed

        elif choice == "2":
            if "courtyard" not in choices:
                print('''
Hmm seems like we've already been to the courtyard.
Here's what we got from the courtyard:
''')
                show_courtyard_items()

            else:
                courtyard()
                choices.remove("courtyard") # marks courtyard completed

        elif choice == "3":
            if "tower" not in choices:
                print('''
Hmm seems like we've already climbed the tower.
Here's what we got from the tower:
''')
                show_tower_items()

            elif "Unlit Torch" in inventory and "Lighter" in inventory:
                print('''
This seems pretty scary, but it looks like we have what we need now.
It's pretty darn dark in there...
''')

                tower()

                if "Lit Torch" in inventory: # tower only finishes if player successfully lights torch
                    choices.remove("tower")

            else:
                print('''
We shouldn't go there yet.
It's very dark and we seem like we're missing some items.
Maybe we should explore somewhere else first.
''')

        elif choice == "4":
            if "dungeon" not in choices and "courtyard" not in choices and "tower" not in choices and "tower_chamber" in choices:
                tower_chamber()
                choices.remove("tower_chamber")
                break # chamber contains final ending so game finishes here

            else:
                print("You can't go there yet.")

        else:
            print("\nInvalid input..")
            print("Please choose one of the available choices.")