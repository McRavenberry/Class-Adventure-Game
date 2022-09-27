from getkey import getkey, keys
from emoji import emojize, is_emoji # add is_emoji

def check_collision(direction, world_list, location, items):
    """Checks player movement (WASD) for collisions"""
    row = location[0]
    col = location[1]
    
    if direction.upper() == "W" or direction == keys.UP:
        if world_list[row-1][col] != "#":
            location = [row-1, col]
            world_list[row-1][col] = "P"
            world_list[row][col] = "/"
        else:
            location = [row, col]            
    elif direction.upper() == "S" or direction == keys.DOWN:
        if world_list[row+1][col] != "#":
            location = [row+1, col]
            world_list[row+1][col] = "P"
            world_list[row][col] = "/"
        else:
            location = [row, col]
    elif direction.upper() == "A" or direction == keys.LEFT:
        if world_list[row][col-1] != "#":
            location = [row, col-1]
            world_list[row][col-1] = "P"
            world_list[row][col] = "/" 
        else:
            location = [row, col]
    elif direction.upper() == "D" or direction == keys.RIGHT:
        if world_list[row][col+1] != "#":
            location = [row, col+1]
            world_list[row][col+1] = "P"
            world_list[row][col] = "/"
        else:
            location = [row, col]
    items["P"][0] = location
    return world_list, location, items

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
            "B" : ":angry_face_with_horns:", # boss
            "C" : ":warning: ", # cave
            "K" : ":crown:", # king
            "L" : ":revolving_hearts:", # love interest
            "P" : ":smirking_face:", # player
            "S" : ":shopping_cart:", # shop/tavern
            "H" : ":bed: ", # hotel
            "E" : ":chequered_flag:" # exit
    }
    em = []
    # Compares the ASCII map values to the emoji map key and inserts the cooresponding emoji for the emoji map.  If the value is not in the map key, then it  gets printed as empty strings on the map.
    for row in range(len(map)):
        trow = ""
        for col in range(len(map[row])):
            symbol = map[row][col]
            if symbol != " ":
                symbol = emojize(map_key[symbol])
            else:
                symbol = "  "
    """Use this code instead to handle the cases if the emoji code in the dictionary does not exist.  Places a red question mark in its place on the emoji map."""
    # for row in range(len(map)):
    #     trow = ""
    #     for col in range(len(map[row])):
    #         symbol = map[row][col]
    #         if symbol == " ":
    #             symbol = "  "
    #         elif symbol != " ":
    #             symbol = emojize(map_key[symbol])
    #             if not (is_emoji(symbol) or is_emoji(symbol[:-1])):
    #                 symbol = emojize(":red_question_mark:")
                    
            trow = trow + symbol
        em.append(trow)
    return em