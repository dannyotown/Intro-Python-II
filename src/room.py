# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room:
    def __init__(self, location, description):
        self.location = location
        self.description = description
        self.items = []

    def __str__(self):
        item_string = ""
        for items in self.items:
            item_string += items
        return f"{self.location}. {self.description}."

    def add_items_to_room(self, item):
        self.items.append(item)
