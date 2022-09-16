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
13. Fog of War
14. Open world like Zelda
15. getkey for automatic key press recognition without the need to press ENTER
16. Save progress

"""

__author__ = "Mr McGarrah's 7th Period"
__version__ = "0.1"

from os import system
from functions import *
from classes import *
from getkey import getkey, keys

# World map and player starting location
world = [
        "######################",
        "#                    #",
        "#                    #",
        "#                    #",
        "#                    #",
        "#                    #",
        "#                    #",
        "#                    #",
        "#                    #",
        "#                    #",
        "#                    #",
        "######################"
    ]  
location = [3, 3]

def main(world, location) -> None:    
    """ Main entry point for the game """
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
    player = Character(name  = "Trevor", weapon = fist, health = 200)
    shopkeeper = Character(name = "Keeper of Shops", weapon = sword)
    thief = Character(name = "Zaam", weapon = dagger, health = 100)

    while True:
        system("clear")
        col = location[1]
        row = location[0]
        
        world = update_ascii_map(world, row, col)
        print_map(world)
        world_list = map2dlist(world)
        print(location)
        
        direction = getkey()
        world_list, location = check_collision(direction, world_list, location)
        world = list2ascii(world_list)

if __name__ == "__main__":
    """ This is executed when the file is run from the command line """
    main(world, location)