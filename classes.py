class Character:
    # def __init__(self, name, attack = {"fist":10}, charisma = 5, health = 100):
    def __init__(self, name, weapon = None, charisma = 5, health = 100):
        self.name = name
        self.weapon = weapon
        self.charisma = charisma
        self.health = health

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