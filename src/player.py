# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, room, name, inventory):
        self.name = name
        self.room = room
        self.inventory = inventory

    def __str__(self):
        currentInv = ""
        for item in self.inventory:
            currentInv += str(item)
        if currentInv == "":
            currentInv = "None"
        return f"{self.name},\nYou are now at {self.room}. \nYour Inventory: {currentInv}"

    def add_items(self, item):
        self.inventory.append(item)

    def remove_items(self, item):
        self.inventory.remove(item)

    def move(self, direction):
        if getattr(self.room, f"{direction}_to") is not None:
            self.room = getattr(
                self.room, f"{direction}_to")
        else:
            print("You Cannot Move In That Direction")
