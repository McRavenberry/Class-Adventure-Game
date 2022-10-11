"""
This is a simple Choose Your Own Adventure Game

Things we need to program:
1. Player 
    - Health ✅
    - Movement ✅
    - Name ✅
    - Appearance/Traits (charisma, etc.) ✅
    - Attack power/weapon ✅
    - Money
2. NPCs ✅
3. Enemies ✅
4. ASCII map ✅
5. Quests (find key, fall in love)
6. Shop (items for sell)
7. Emoji map
8. Battle system
9. In-Game Display (Textualize and/or Rich)
10. Menus
11. Inn/sleep/heal
12. Use potions
13. Fog of War ✅
14. Open world like Zelda
15. getkey for automatic key press recognition without the need to press ENTER
16. Save progress

✅ Save items on map into a dictionary (SEE BELOW) 
✅ Make fog of war map
✅ Remove fog of war in adjacent tiles
✅ If no fog of war present or no player present, draw item on map

"""

__author__ = "Mr McGarrah's 7th Period"
__version__ = "0.2"

from os import system
from functions import *
from classes import *
from getkey import getkey
import time

# World map and player starting location
world = [
        "###################",
        "#      K    #  S  #",
        "#           #     #",
        "#  HP    L  #     #",
        "########    #     #",
        "#    L #    #     #",
        "#      #    L     #",
        "#      #          #",
        "#  S  C   #       #",
        "#         # B     #",
        "#    C    #       #",
        "#         #       #",
        "###########       #",
        "#L B#             #",
        "#   #   #######   #",
        "#   #   #S        #",
        "#   #   #  ########",
        "#       #        E#",
        "###################"
    ]
# Makes a fog world map
fog_world = []

for row in range(len(world)):
    fog_world.append("")
    fog_world[row] = "/" * len(world[row])

# input()

"""Add the ability to turn map reveal on/off"""
keep_fog_off = False # True deletes fog as it is cleared.  False fills the fog back in after the player moves.
if not keep_fog_off:
    fog = fog_world

# Finds all of the items on the map and places them in a dictionary. Keys are stored in a list with coordinate pairs as tuples.

items = {}

for row in range(len(world)):
    for i, item in enumerate(world[row]): 
        if item not in items: 
            items[item] = [(row, world[row].index(item))]
        elif item in items:
            items[item].append((row, i))


# print(items["#"])
# input()
# # Removes an item from the dictionary by the index of the item in the list
# temp = items["C"]
# del temp[0]
# items["C"] = temp


# Finds the location of the player.  Even if multiple "P" are on the map, the very first "P" is the one that will be used.
location = list(items["P"][0])


def main(world, fog_world, items, location) -> None:    
    while True:
        """ Main entry point for the game """
        print("Love and Legends")
        print("""
        
        """)
        print("[S]tart New Game")
        print("[C]ontinue Old Game")
        start = input("> ")
        if start.upper() == "S":
            player = create_player()
            break
        elif start.upper() == "C":
            print("Load game code will go here")
            print("Press [C] to continue")
            input()
            break
        system("clear")
        






    
    # Create weapons
    sword = Weapon("Toby", 25, 50)
    fist = Weapon("fist", 0, 10)
    dagger = Weapon("Dolly Dagger", 15, 20)
    weapon_list = [sword, fist, dagger]

    # Create potions
    health_potion = Potion("Health Potion", 25, "heal", 50)
    poison_potion = Potion("Poison Potion", 35, "poison", 10)
    love_potion = Potion("Love Potion", 50, "love", 25)
    potion_list = [health_potion, poison_potion, love_potion]
    
    # Create characters, NPCs, and enemies
    name = "Trevor"
    gender = "male"
    attraction = "female"
    player = Player(name, gender, attraction)
    print(player.gold)
    input()

    while True:
        # time.sleep(0.2)
        system("clear")
        col = location[1]
        row = location[0]

        """Switch between fog modes"""
        if keep_fog_off:
            fog_world = remove_fog(fog_world, items, location)
        else:
            fog_world = remove_fog(fog, items, location)
  
        # fog_world = update_ascii_map(fog_world, row, col)
        
        # Turn ASCII map into an emoji map and prints it to the screen
        print_map(emoji_map(fog_world))

        world_list = map2dlist(fog_world)
        print(location)
        
        direction = getkey()
        time.sleep(0.2)
        world_list, location, items = check_collision(direction, world_list, location, items)
        fog_world = list2ascii(world_list)

if __name__ == "__main__":
    """ This is executed when the file is run from the command line """
    main(world, fog_world, items, location)