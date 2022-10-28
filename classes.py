from os import system
from getkey import keys, getkey
import time

class Player:

  def __init__(self,
               name,
               gender,
               attr,
               inventory=[]):
    self.name = name
    self.gender = gender
    self.attr = attr
    self.gold = 15
    self.fame = 5
    self.love = 5
    self.weapon = Weapon("fist", 0, 10)
    self.health = 100
    self.max_health = 100
    self.gen = 1
    self.inventory = inventory

    
  def change_weapon(self, weapon):
    self.weapon = weapon

  def equip_item(self, inven, num):
      for i in range(5):
        if i == num - 1:
          
          self.weapon = self.inventory[num-1]
          print(f"You equipped {self.weapon.name}!")
          time.sleep(2)
          system("clear")
    
    
  def remove_item(self, dropping, inven):
    sure = input("are you sure?: [y]es or [n]o\n\n")
    
    if sure.upper() == "Y":
      for i in range(5):
        if i == dropping - 1:
          self.inventory.pop(dropping-1)
          system("clear")
    else:
      print("Phew, that was close!")
      time.sleep(2)
      system("clear")
        
  def view_inventory(self, inv):
    print(f"EQUIPPED: {self.weapon.name}")#add equipped_item variable somehow
    print("\nBACKPACK:")
    for i, item in enumerate(self.inventory):
      if item != "empty":
        print(f"{i+1}. {item.name}")
      
    print("\nPress [e] to equip an item, press [r] or [delete] to remove an item, press [i] or [esc] to close the menu.\n\n")

    inv_button = getkey()
    # drop_item
    # display_attributes
    # equip_item

    if inv_button == keys.ESCAPE or inv_button.upper() == "I":
      system("clear")
    elif inv_button.upper() == "R" or inv_button == keys.DELETE:
        dropping=int(input("Enter the inventory index to drop (1-5): "))
        Player.remove_item(self, dropping, inv)
    elif inv_button.upper() == "E" :
        equip = int(input("Enter the inventory index of the item you'd like to equip (1-5): "))
        Player.equip_item(self, inv, equip)


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.quantity = 0

    # method to add/subtract quantity of item
    def change(self, quantity):
        self.quantity = self.quantity + quantity

        

class Weapon(Item):
    def __init__(self, name, price, attack, range=False):
        # inherit name and price for the Item superclass 
        super().__init__(name, price)
        self.attack = attack
        self.range = range


class Potion(Item):
    def __init__(self, name: str, price: int, effect: str, amount = 0):
        super().__init__(name, price)
        self.effect = effect
        self.amount = amount