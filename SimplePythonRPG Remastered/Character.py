from Entity import Entity
from math import floor
class Character(Entity):
    def __init__(self, Hp, Atk, Def, Spd, Level, mana, Name):
        Entity.__init__(self, Hp, Atk, Def, Spd, Level, Name)
        self.mana = mana
        self.currMana = mana
        self.exp = floor(1.2 * Level ** 3 - 15 * Level ** 2 + 100 * Level - 140)
        self.inventory = ["Mango", "Chenette", "Doubles"]