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
    self.weapon = Weapon("fist", "fist", 0, 10, 90)
    self.health = 100
    self.max_health = 100
    self.gen = 1
    self.inventory = inventory
    
  def change_weapon(self, weapon):
    self.weapon = weapon

  def equip_item(self, num):
      for i in range(5):
        if i == num - 1 and i < len(self.inventory):
          self.weapon = self.inventory[num-1]
          print(f"You equipped {self.weapon.name}!")
          
      else:
        print("You cannot equip that.")  
      time.sleep(2)
      system("clear")
    
    
  def remove_item(self, dropping, inven):
    sure = input("are you sure?: [y]es or [n]o\n\n")
    
    if sure.upper() == "Y":
      for i in range(5):
        if i == dropping - 1:
          self.inventory.pop(dropping-1)
          system("clear")
      self.inventory.append("empty")
    else:
      print("Phew, that was close!")
      time.sleep(2)
      system("clear")
        
  def view_inventory(self):
    print(f"EQUIPPED WEAPON: {self.weapon.name}")#add equipped_item variable somehow
    print("EQUIPMENT:")
    for i in range(5):
        if i < len(self.inventory):
            print(f"{i+1}. {self.inventory[i].name}")
        else:
            print(f"{i+1}. empty")
    # for i, item in enumerate(self.inventory):
    #   if item != "empty":
    #     print(f"{i+1}. {item.name}")
    #   else:
    #       print(f"{i+1}. open slot")
      
    print("\nPress [e] to equip an item, press [r] or [delete] to remove an item, press [i] or [esc] to close the menu.\n\n")

    inv_button = getkey()
    # drop_item
    # display_attributes
    # equip_item

    if inv_button == keys.ESCAPE or inv_button.upper() == "I":
      system("clear")
    elif inv_button.upper() == "R" or inv_button == keys.DELETE:
        dropping = input("Enter the inventory index to drop (1-5): ")
        dropping = int(dropping)
        Player.remove_item(self, dropping, inv)
    elif inv_button.upper() == "E" :
        equip = input("Enter the inventory index of the item you'd like to equip (1-5): ")
        equip = int(equip)
        Player.equip_item(self, equip)

    def __init__(self, name, gender, attr):
        self.name = name
        self.gender = gender
        self.attr = attr
        self.gold = 15
        self.fame = 5
        self.love = 5
        self.weapon = None
        self.health = 100
        self.max_health = 100
        self.gen = 1
        self.gold = gold
        self.fame = fame
        self.love = love
        self.weapon = weapon
        self.health = health
        self.gen = gen
        self.inventory = []

    def change_weapon(self, weapon):
        self.weapon = weapon



class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.quantity = 0

    # method to add/subtract quantity of item
    def change(self, quantity):
        self.quantity = self.quantity + quantity

        

class Gift(Item):
    def __init__(self, name: str, price: int = 100):
        super().__init__(name, price)
    def use(self, player):
        # 
        player.inventory.pop(player.inventory.index(self))

class Weapon(Item):
    def __init__(self, name, type, price, damage, accuracy):
        # inherit name and price for the Item superclass 
        super().__init__(name, price)
        self.type = type
        self.damage = damage
        self.accuracy = accuracy
        self.damage = damage

player_hp = 100
class Potion(Item):
    def __init__(self, name: str, price: int, effect: str, amount = 0):
        super().__init__(name, price)
        self.effect = effect
        self.amount = amount

class Enemy:
    def __init__(self, name, attack, defense, accuracy, health, max_health, gold, fame_exp):
      self.name = name
      self.attack = attack
      self.accuracy = accuracy
      self.health = health
      self.max_health = max_health
      self.gold = gold
      self.fame_exp = fame_exp