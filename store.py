"""
Shop System Description
--------------------------

The shop sells two weapons, two gifts, and one health potion at any given time.

Weapons
Weapons have random names, damage, and price
Gifts
Gift items are random, but will gain you favor with different love interests depending on what they are
Health potions
The shop only hold five items at a time. After a purchase is made, the item slot will be placed with a new item on the next visit. Every 14 days, all of the items in the shop will be swapped out.

If you purchase anything from the shop, it takes a day off of your time.
"""


"""
https://replit.com/@ElNayrb/Adventure-Game-Group-1#shop.py
"""

day = 0
from classes import Gift, Weapon, Potion
import os
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
def enter_to_continue(pre="\n", post="\n"):
    return input(f"{pre}Enter to continue...{post}")

player_gold = 1000

class Shop:
    def __init__(self, items=[]):
        # item name : cost
        self.items = items
    def _add_to_stock(self, item):
        self.items.append(item)
    def sell(self):
        """
        menu
        get choice
        check price
            continue to next step if player has enough money
            return to beginning menu if not
        run transaction
            subtract cost
            give item
            
            print reciept
            
        """
        pass

    def restock(self, inventory=[
            Weapon("Weapon 1", 0, 0),
            Weapon("Weapon 2", 0, 0),
            Gift("Gift 1", 0),
            Gift("Gift 2", 0),
            Potion("Health Potion", 0, 0)
        ]):
        self.inventory = inventory
    """"""
    def _get_choice(self, choice):
        """Get, evaluate, and format which item the player wants"""
        
        # While the choice isn't within the amount of items in ther shop...
        while choice not in [str(x + 1) for x in range(len(self.items))]:
            clear_screen()

            print(f"You have ${player_gold}.")
            print("Press \"x\" to exit.")

            # Print out every available item
            print("\nAvailable Items:")
            for i in range(len(self.items)):
                item = self.items[i]
                print(f"\t{str(i + 1)}) {item.name} - ${str(item.price)}")

            # Exit if the player inputs "x"
            if str(choice).upper() == "X":
                clear_screen()
                print("You have exited the shop.")
                enter_to_continue()
                return "X"

            # A little shortcut so that stuff doesn't have to be typed twice
            if choice != None:
                print("\nThat isn't an option.")

            # Get the player's choice
            choice = input("\nWhat would you like to buy?\n> ")
        return choice

    def buy(self, player):
        global player_gold, day
        # The following adds a little readability when accessing items
        name = 0
        cost = 1
        supply = 2

        # If there isn't enough space, tell the player and exit
        if len(player.inventory) > 5:
            print("There isn't enough space in you inventory to buy.")
            enter_to_continue()
            return
        else:
            pass
        
        # Ask for the player's choice. If the player's input doesn't match with any options, continue asking.
        choice = self._get_choice(None)
        # If player wants to exit...
        if choice == "X":
            return
        # After getting the player's choice, store the chosen item in a variable for easier reference
        chosen_item = self.items[int(choice) - 1]



        total_price = (chosen_item.price)

        # Check if the player can afford the transaction
        # If so, bill the player, subtract the item's supply and give it to the player, and print the transaction
        # If not, return to the beginning
        if total_price <= player_gold:
            while True:
                clear_screen()
                
                player_gold -= total_price
                
                player.inventory.append(chosen_item.name)
                
                print(f"You bought {chosen_item.name} for ${total_price}.")
                print(f"\nYou now have ${player_gold}.")
                
                # If the player wants to buy somehting else, loop to beginning
                # If not, exit
                # If input is invalid, ask again                
                choice = input("\nDo you want to buy something else? (y/n)\n> ")
                if choice.upper().find("Y") != -1:
                    return self.buy(player)
                elif choice.upper().find("N") != -1:
                    print("You have exited the shop.")
                    day += 1
                    enter_to_continue()
                    return
                else:
                    print("That isn't an option.")
                    enter_to_continue()
                    continue
        else:
            print("\nYou don't have enough money.")
            enter_to_continue()
            return self.buy(player)
    


