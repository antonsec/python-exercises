class Player: # blueprint for creating characters
    def __init__(self, name, age, inventory, health, level, location): # values needed when making a character
        self.name = name # saves characters name
        self.age = age # saves characters age
        self.inventory = inventory # gives character an inventory
        self.health = health # saves characters health
        self.level = level # saves characters level
        self.location = location # saves character location

    def move(self, room):
        self.location = room # moving player to different rooms

    def collect_item(self): # collects item from current room
        if self.location.item is not None: # checking if theres an item available
            self.inventory.append(self.location.item.name) # adding item to inventory
            self.location.item = None # the room no longer contains an item
