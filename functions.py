from getkey import getkey, keys

def check_collision(direction, world_list, location):
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
    return world_list, location

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