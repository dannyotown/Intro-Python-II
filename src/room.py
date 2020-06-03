# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, location, description):
        self.location = location
        self.description = description

    def __str__(self):
        return f"{self.location}. {self.description}"
