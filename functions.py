from getkey import getkey, keys
from os import system
from emoji import emojize, is_emoji
import time
from classes import Player
from battle import random_battle
import poi
from random import randint
from classes import Player, Weapon, Gift, Potion
import poi
from store import Shop

from classes import Player, Weapon, Gift, Potion
import poi
from store import Shop


shop = Shop([
    Weapon("Wooden Sword", "sword", 50, 20, 70),
    Weapon("Iron Sword", "sword", 200, 30, 75),
    Gift("Red Rose", 30),
    Gift("Blue Sapphire", 500),
    Potion("Health Potion", 200, "heal", 50)
])


def check_collision(direction, world_list, location, items, player):
    """Checks player movement (WASD) for collisions"""
    row = location[0]
    col = location[1]

    if direction.upper() == "W" or direction == keys.UP:
        if world_list[row-1][col] != "  " and randint(1,10) < 2:
            player = random_battle(player)
        if world_list[row-1][col] != "#":
            location = [row-1, col]
            world_list[row-1][col] = "P"
            world_list[row][col] = "/"
        else:
            location = [row, col]            
    elif direction.upper() == "S" or direction == keys.DOWN:
        if world_list[row-1][col] != "  " and randint(1,10) < 2:
            player = random_battle(player)
        if world_list[row+1][col] != "#":
            location = [row+1, col]
            world_list[row+1][col] = "P"
            world_list[row][col] = "/"
        else:
            location = [row, col]
    elif direction.upper() == "A" or direction == keys.LEFT:
        if world_list[row-1][col] != "  " and randint(1,10) < 2:
            player = random_battle(player)
        if world_list[row][col-1] != "#":
            location = [row, col-1]
            world_list[row][col-1] = "P"
            world_list[row][col] = "/" 
        else:
            location = [row, col]
    elif direction.upper() == "D" or direction == keys.RIGHT:
        if world_list[row-1][col] != "  " and randint(1,10) < 2:
            player = random_battle(player)
        if world_list[row][col+1] != "#":
            location = [row, col+1]
            world_list[row][col+1] = "P"
            world_list[row][col] = "/"
        else:
            location = [row, col]
    items["P"][0] = location

    for key in items:
        if tuple(location) in items[key] and key != " ":
            if key == "C":
                print("Castle")
            elif key == "I":
                poi.event()
            elif key == "B":
                print("Boss")
            elif key == "S":
                shop.buy(player)
                break
            elif key == "E":
                print("Exit")
            input()
        # for i in range(len(dict[item])):
        #     if tuple(location) in item:
        #         print("hello")
    return world_list, location, items, player

def update_ascii_map(world, row, col):
    """Updates the player position on the map"""
    pworld = []
    for i in range(len(world)):
        if i == row:
            pworld.append(world[row][:col]+"P"+world[row][col+1:])
        else:
            pworld.append(world[i])
    world = pworld
    return world

def map2dlist(world) -> list:
        """Converts the world map into a 2d list for easier collision detection and returns world_list"""
        world_list = []
        for i in range(len(world)):
            temp = list(world[i])
            world_list.append(temp)
        return world_list

def print_map(world):
    """Prints viewable map"""
    for i in range(len(world)):
        print(world[i])

def list2ascii(world_list):
    """Convert world_list back into ascii map """
    temp = []
    for i in range(len(world_list)):
        j = "".join(world_list[i])
        temp.append(j)
    return temp


def remove_fog(map, items, location: list) -> list:
    """Pass the map and the coordinate of the player as a list. Returns a map with the fog of war removed for the 3x3 grid around the player."""
    row, col = location
    clist = []

    # Finds the 3x3 grid around the player's location
    for i in range(3):
        for j in range(3):
            if [row-1+i,col-1+j] not in clist:
                clist.append([row-1+i,col-1+j])

    # Converts the map into a list of lists
    new_map = []
    for row in map:
        new_map.append(list(row))

    # Removes the fog of war from the map
    for i, row in enumerate(new_map):
        for j, col in enumerate(row):
            if new_map[i][j] == "/" and [i, j] in clist:
                new_map[i][j] = " "

    # Adds items onto map if discovered
    for item in items:
        locations = items[item]
        # Adds player to fog_world at location
        if item == "P":
            row, col = locations[0]
            new_map[row][col] = "P"
            
        # Adds other items to the map if discovered
        else:
            for i in range(len(locations)):
                row, col = locations[i]
                if new_map[row][col] not in "#/P":
                    new_map[row][col] = item
    # Coverts the list back into a string
    map = []
    for row in new_map:
        temp = "".join(row)
        map.append(temp)

    return map
    
def emoji_map(map: "ASCII map") -> "emoji map":
    """Converts an ASCII map into an emoji map, then prints it to the screen"""
    map_key = {
            "#" : ":mountain: ", # wall
            "/" : ":fog: ", # fog
            "B" : ":dragon_face:", # boss
            "I" : ":magnifying_glass_tilted_left:", # cave
            "C" : ":castle:", # castle
            "E" : ":chequered_flag:", # exit
            "S" : ":shopping_cart:", # store
            "P" : ":frog:" # PLAYER
    }
    em = []
    # Compares the ASCII map values to the emoji map key and inserts the cooresponding emoji for the emoji map.  If the value is not in the map key, then it gets printed as empty strings on the map.
    for row in range(len(map)):
        trow = ""
        for col in range(len(map[row])):
            symbol = map[row][col]
            # Adds the emoji to the map if the item is in the dictionary.  Adds a red exclamation mark to the map if the item is in the dictionary but does not include a proper emoji code
            if symbol in map_key.keys():
                symbol = emojize(map_key[symbol])
                if not(is_emoji(symbol) or is_emoji(symbol[:-1])):
                    symbol = emojize(":red_exclamation_mark:")
            # Adds a double space to the map instead of a single space to accommodate the emojis that are two spaces in size
            elif symbol == " ":
                symbol = "  "
            # Adds a red question mark to the map if the item is not in the dictionary 
            else:
                symbol = emojize(":red_question_mark:")
            trow = trow + symbol
        em.append(trow)
    return em

def create_player():
    system("clear")
    while True:
        name = input("Character Name: ")
        if len(name) > 19:
            system("clear")
            print("Please enter a name that is less than 19 characters long.")
        else:
            break
            
    while True:
        gender = input("Male or Female? ")
        if gender[0].upper() == "M":
            gender = "male"
            break
        elif gender[0].upper() == "F":
            gender = "female"
            break
        else:
            system("clear")
            print("Please enter male or female")

    while True:
        attraction = input("Attracted to Male or Female? ")
        if attraction[0].upper() == "M":
            attraction = "male"
            break
        elif attraction[0].upper() == "F":
            attraction = "female"
            break
        else:
            system("clear")
            print("Please enter male or female")
            
    print("\nYou created the following player: ")
    print("Name: " + name)
    print("Gender: " + gender)
    print("Attracted to " + attraction)
    print("\nPress any key to continue")
    return Player(name, gender, attraction)

def load_map():
    world = [
        "###################",
        "#S     I    #  I  #",
        "#           #     #",
        "#  CP    I  #     #",
        "########    #     #",
        "#     S#    #     #",
        "#      #    I     #",
        "#      #          #",
        "#  I  I   #       #",
        "#         # I     #",
        "#    I    #       #",
        "#         #       #",
        "###########       #",
        "#I B#             #",
        "#   #   #######   #",
        "#   #   #I        #",
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
    # Finds the location of the player.  Even if multiple "P" are on the map, the very first "P" is the one that will be used.
    location = list(items["P"][0])

    return map, fog_world, items, location, keep_fog_off, fog