# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, room, name, inventory):
        self.name = name
        self.room = room
        self.inventory = [inventory]

    def __str__(self):
        currentInv = ""
        for item in self.inventory:
            currentInv += str(item)
        return f"{self.name}, you are now at {self.room}. Items: {currentInv}"

    def add_items(self, item):
        self.inventory.append(item)

    def remove_items(self, item):
        self.inventory.remove(item)
