from room import Room
from item import Item
from player import Player

# Declare all the rooms

items = {
    "sword": Item('Sword', 'Sharp word, helps Fight off the bad guys.'),
    "dagger": Item('Dagger', 'Small dagger, helps fight off the bad guys.')
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items['dagger']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [])
}

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Link rooms together

#
# Main
#


# Make a new player object that is currently in the 'outside' room.
# player_name = input('Please Enter Your Name:')
# player = Player(room['outside'], player_name)
# where_to = input(
#     '[n] for north, [s] for south, [e] for east, [w] for west:').lower()
# if(where_to == 'n'):
#     player.room = room['outside'].n_to
# else:
#     print('You Cannot Go This command')

player_name = input('Please Enter Your Name:')
player = Player(room['outside'], player_name, [items['sword']])
while True:
    try:
        print(player)
        command = input(
            '[n] for north, [s] for south, [e] for east, [w] for west, [f] to drop item, [t] to pick up item, [q] to exit:').lower()
        if command == 'q':
            print('Thanks For Playing')
            break
        if command == 'f':
            drop_cmd = input(
                'Which Item Did You Want To Drop?').lower()
            if items.get(drop_cmd):
                player.remove_items(items[drop_cmd])
                player.room.add_items_to_room(items[drop_cmd])
            else:
                print('****************\n Item Does Not Exist \n****************')
        if command == 't':
            pick_up_cmd = input('Which Item Did You Want To Pick Up?').lower()
            if items[pick_up_cmd] in player.room.items:
                player.room.remove_items_in_room(items[pick_up_cmd])
                player.add_items(items[pick_up_cmd])
            else:
                print('****************\n Item Does Not Exist \n****************')
        if command == 's' or command == 'n' or command == 'e' or command == 'w':
            player.move(command)
    except ValueError:
        print('Error')

    # Write a loop that:
    #
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    #
    # If the user enters a cardinal command, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
