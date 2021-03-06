# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room:
    def __init__(self, location, description, items):
        self.location = location
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items

    def __str__(self):
        item_string = ""
        for items in self.items:
            item_string += str(items)
        if item_string == "":
            item_string = 'None'
        return f"{self.location}. {self.description}.\nITEMS HERE: {item_string}"

    def add_items_to_room(self, item):
        self.items.append(item)

    def remove_items_in_room(self, item):
        self.items.remove(item)
