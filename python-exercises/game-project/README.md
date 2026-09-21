# The Game...

**Pierre**

## About

The Game is a text-based adventure game made with Python.

The player explores an abandoned castle, collects items and tries to escape.

## Project structure

game-project/
├── game.py
├── intro.txt
├── instructions.txt
├── save.txt
├── README.md
└── game_objects/
    ├── __init__.py
    ├── item.py
    ├── player.py
    └── room.py

- `game.py` contains the main game, menus, events and save/load functions.
- `intro.txt` contains the introduction.
- `instructions.txt` contains the game instructions.
- `save.txt` stores the saved game.
- `game_objects/item.py` contains the `Item` class.
- `game_objects/player.py` contains the `Player` class.
- `game_objects/room.py` contains the `Room` class.

## Classes

The game uses `Player`, `Room` and `Item` objects.

- `Item` has a name and weight.
- `Room` has a name and can contain an item.
- `Player` has a name, inventory and current room.
- The player can move between rooms and collect items.

## Saving

The game reads the introduction and instructions from separate text files.

The player's progress can be saved to `save.txt` and loaded later to continue the game.