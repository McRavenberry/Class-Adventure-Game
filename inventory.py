# View inventory DONE
#while true loop
#button press "i"
#display DONE ALL

# Use item in the inventory DONE
#button press 'i'
#item info

# Drop item DONE
#inventory movement NOT NECESSARY
#button press "DELETE" w/ "are you sure?" SUCCESS
#item removal SUCCESS

# Display all player attributes
#display inventory DONE
#call player variables 
#weapon type too (LATER ONCE EVERYTHING IMPORTED)
#show potion effects
from os import system
from getkey import keys, getkey
import time



# player = Player("Bob", "male", "male")

while True:
  print("You are in the map, Press i to open and close inventory.")
  uinput = getkey()
  if uinput.upper() == "I":
    system("clear")
    if len(player.inventory) > 0:
      player.view_inventory(player.inventory)

    elif len(player.inventory) == 0:
      print("Whoops, all nothing!")
      player.view_inventory()

    elif len(player.inventory) == 0:
      print("You have no inventory.")
      time.sleep(2)
      system("clear")

        
        
        #ACTUALLY USELESS
        # Dustin's Immortal Legendary Forever Stupidity or the DILFS rule
    # As a clause of Dustin's Immortal Stupidity, abuse to Dustin is allowed
    # In an additional clause, We can make Dustin feel stupid.
# def something():
#   def something_else():

        
#🥫ಠ__ಠ   еру иуые цфн ещ сщву ершы зкщпкфь шы ещ тще сщву ше фе фддю
