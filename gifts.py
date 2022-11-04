# from main import player
import random

# Available gifts that could have been bought from a store
possible_gifts = ["flower", "diamond", "food"]
shop_gift = random.choice(possible_gifts)
chosen_interest = None
interest1 = 0
interest2 = 0
interest3 = 0

# This is here just to show that you have an option to give a gift to someone.
give_gift = input("Would you like to give a gift? Y/N? ")


#All of these functions determine which love interest prefers which item from a gift.
def give_to_interest(interest, chosen_interest):
  if chosen_interest == 1:
    # Interest 1 prefers to have a flower over a diamond and food.
    if shop_gift == possible_gifts[0]:  # flower
      interest = interest + random.randint(10, 25)
    elif shop_gift == possible_gifts[1]:  # diamond
      interest = interest + random.randint(5, 15)
    elif shop_gift == possible_gifts[2]:  # food
      interest = interest + random.randint(1, 10)
    print(f"You gave {shop_gift} to {chosen_interest}")
    print(f"interest{chosen_interest} value: {interest}")

  elif chosen_interest == 2:
    # Interest 2 prefers to have a diamond over food and a flower.
    if shop_gift == possible_gifts[1]:  # diamond
      interest = interest + random.randint(10, 25)
    elif shop_gift == possible_gifts[2]:  # food
      interest = interest + random.randint(5, 15)
    elif shop_gift == possible_gifts[0]:  # flower
      interest = interest + random.randint(1, 10)
    print(f"You gave {shop_gift} to {chosen_interest}")
    print(f"interest{chosen_interest} value: {interest}")

  elif chosen_interest == 3:
    # Interest 3 prefers to have food over a flower and diamond.
    if shop_gift == possible_gifts[2]:  # food
      interest = interest + random.randint(10, 25)
    elif shop_gift == possible_gifts[0]:  # flower
      interest = interest + random.randint(5, 15)
    elif shop_gift == possible_gifts[1]:  # diamond
      interest = interest + random.randint(1, 10)
    print(f"You gave {shop_gift} to {chosen_interest}")
    print(f"interest{chosen_interest} value: {interest}")


"""
def interest1_gift(interest1):
# Interest 1 prefers to have a flower over a diamond and food.
  
  if shop_gift == possible_gifts[0]: # flower
    interest1 = interest1 + random.randint(10, 25)
  elif shop_gift == possible_gifts[1]: # diamond
    interest1 = interest1 + random.randint(5, 15)
  elif shop_gift == possible_gifts[2]: # food
    interest1 = interest1 + random.randint(1, 10)
  print(f"You gave {shop_gift} to {chosen_interest}")
  print(f"interest{chosen_interest} value: {interest1}")


def interest2_gift(interest2):
# Interest 2 prefers to have a diamond over food and a flower.
  
  if shop_gift == possible_gifts[1]: # diamond
    interest2 = interest2 + random.randint(10, 25)
  elif shop_gift == possible_gifts[2]: # food
    interest2 = interest2 + random.randint(5, 15)
  elif shop_gift == possible_gifts[0]: # flower
    interest2 = interest2 + random.randint(1, 10)
  print(f"You gave {shop_gift} to {chosen_interest}")
  print(f"interest{chosen_interest} value: {interest1}")

def interest3_gift(interest3):
# Interest 3 prefers to have food over a flower and diamond.
  if shop_gift == possible_gifts[2]: # food
    interest3 = interest3 + random.randint(10, 25)
  elif shop_gift == possible_gifts[0]: # flower
    interest3 = interest3 + random.randint(5, 15)
  elif shop_gift == possible_gifts[1]: # diamond
    interest3 = interest3 + random.randint(1, 10)
  print(f"You gave {shop_gift} to {chosen_interest}")
  print(f"interest{chosen_interest} value: {interest1}")
"""


def gifts_main(player):
  gifts = []
  gift_count = 1
  for i in player.inventory:
    if i in possible_gifts:
      gifts.append(i)
      print(f"{gift_count}) {i}")
  while True:
    if give_gift == "Y":
      chosen_interest = int(
        input("Who would you like to give your gift to? (1, 2, 3)? "))
      if chosen_interest == 1:
        give_to_interest(interest1, 1)
      elif chosen_interest == 2:
        give_to_interest(interest2, 2)
      elif chosen_interest() == 3:
        give_to_interest(interest3, 3)

    input()


class Item:

  def __init__(self, name, price):
    self.name = name
    self.price = price
    self.quantity = 0

  # method to add/subtract quantity of item
  def change(self, quantity):
    self.quantity = self.quantity + quantity


class Gift(Item):

  def __init__(self, name: str, price: int):
    super().__init__(name, price)

  def use(self, player):
    #
    player.inventory.pop(player.inventory.index(self))


class Weapon(Item):

  def __init__(self, name: str, price: int):
    super().__init__(name, price)

  def use(self, player):
    #
    player.inventory.pop(player.inventory.index(self))
