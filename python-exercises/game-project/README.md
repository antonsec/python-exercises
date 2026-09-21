# The Game...
**Pierre**

## What is this game?

The Game is a text based adventure game coded in Python.
You wake up inside an abandoned castle without knowing how you got there.
Your goal is to explore the rooms, collect useful items and find a way out.

The project follows these [instructions](https://metropolia-sw.github.io/sw1-python/en/programming_project_1.html).

## How to play

Open a terminal in the game-project folder and run:

```bash
python3 game.py
```

Enter your name and age. The game is for ages 12 and up.
Type numbers to choose rooms and answer questions.
You can visit the dungeon and courtyard in either order and revisit rooms to collect items.

- `collect` picks up an item from your current room
- `inventory` shows the items you have
- `profile` shows your name, age, health, level and location
- `pack` adds an item you type to your inventory, like in the original game
- `instructions` shows the instructions again
- `save` saves your progress to save.txt, replacing the previous save
- `load` continues from save.txt
- `quit` exits the game

Collect the unlit torch in the dungeon and the lighter in the courtyard.
In the tower, choose to search your inventory to light the torch.
After exploring the dungeon, courtyard and tower, the tower chamber becomes available.
If you leave the tower without lighting the torch, you can try again.
The map and tower key are extra collectibles. They aren't needed to escape.
Food and the healing potion are collected as loot. There isn't a use-item command.

## Choices and endings

The dungeon and courtyard have random events, so each game can be different.
Some choices change your health, level and inventory.
Normal events can't reduce your health below 1.

There are three story paths depending on what you do when you meet Guts:

1. Help the wounded knight. He helps you open the gate and you escape together.
2. Ignore the knight. You struggle with the gate but escape alone.
3. Try to steal from the knight. He remembers you and the game ends with your death.

If you don't meet him in the courtyard, you meet him in the final chamber.
The game counts good and bad choices and shows them at the end.
These counters describe your decisions. The knight's status decides the ending.

## Files

- game.py contains the menus, events and save/load functions
- intro.txt contains the opening story
- instructions.txt contains the instructions shown during the game
- save.txt stores one saved game as plain text
- game_objects/__init__.py imports the classes from the package
- game_objects/item.py contains the Item class
- game_objects/player.py contains the Player class
- game_objects/room.py contains the Room class

The save remembers your profile, inventory, location, completed rooms, knight decision,
good and bad choices, room loot and which items are still available to collect.
Run the game from its folder so it can find the text files.

## Sustainable Development

The game includes **Goal 3: Good Health and Well-being** through the wounded knight.
You can use medical supplies to help someone who is injured.
Helping him has a positive effect later when he helps you escape.
