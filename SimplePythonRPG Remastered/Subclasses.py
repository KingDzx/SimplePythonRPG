from Classes import *
from random import randint, random, uniform
from PySimpleGUI import *


class Wizard(Mage):
    def __init__(self, Name):
        Mage.__init__(self, Name)

    def specialAttack(self, enemy):
        if self.currMana >= 12:
            self.currMana -= 12
            Popup("You cast a dark magic to gain an advantage against the opponent!")
            buff = random()
            if buff <= 0.33:
                atkBuff = round(randint(3, 5) * self.Level / 2)
                Popup("A harsh red light casts down upon you\nYou gained " + str(atkBuff) + "Attack!")
                return 'Atk', atkBuff
            elif 0.33 < buff <= 0.67:
                defBuff = round(randint(3, 5) * self.Level / 2)
                Popup("A subtle green light casts down upon you\nYou gained " + str(defBuff) + "Defense!")
                return 'Def', defBuff
            elif buff > 0.67:
                spdBuff = round(randint(3, 5) * self.Level / 2)
                Popup("A quick blue light casts down upon you\nYou gained" + str(spdBuff) + "Speed!")
                return 'Spd', spdBuff
        else:
            Popup("Not Enough Mana!")


class Hemomancer(Mage):
    def __init__(self, Name):
        Mage.__init__(self, Name)

    def specialAttack(self, enemy):
        if self.currMana >= 20:
            self.currMana -= 20
            Popup("You use your magic to manipulate the enemy's blood!")
            damage = round(((((2 * self.Level / 5 + 2) * self.Atk * randint(60, 125) / enemy.Def) / 50) + 2) * (
                        randint(1, 100) / 100))
            if enemy.Hp - damage < 0:
                heal = round(enemy.Hp * 0.67)
                self.currHp += heal
            else:
                heal = round(damage * 0.67)
                self.currHp += heal

            enemy.takeDamage(damage)

            if self.currHp > self.Hp:
                self.currHp = self.Hp

            if damage == 0:
                Popup("You tried to cast your magic but it failed!")
                self.currMana += 10
            else:
                Popup("You dealt " + str(damage) + " damage and healed for " + str(heal))
        else:
            Popup("Not Enough Mana!")
        return 'Atk', 0


class Bruiser(Warrior):
    def __init__(self, Name):
        Warrior.__init__(self, Name)

    def specialAttack(self, enemy):
        self.currMana -= 10
        damage = round(((((2 * self.Level / 5 + 2) * self.Atk * randint(200, 300) / enemy.Def) / 50) + 2) * (
                    randint(1, 100) / 100))
        enemy.takeDamage(damage)
        self.currHp -= round(damage * 0.20)
        Popup("You strike with the force of give or take a few hundred suns")
        Popup("You dealt " + str(damage) + " holy damage!")
        Popup("You took " + str(round(damage * 0.35)) + " splash damage!")
        if self.currHp < 0:
            self.currHp = 1
            Popup("You barely hold on with 1 HP after that attack")

        return 'Atk', 0


class Paladin(Warrior):
    def __init__(self, Name):
        Warrior.__init__(self, Name)

    def specialAttack(self, enemy):
        if self.currMana >= 25:
            self.currMana -= 25
            mult = uniform(0.5, 0.8)
            self.currHp += round(self.Hp * mult)
            Popup("You blessed yourself with a holy light!")
            Popup("You healed " + str(round(self.Hp * mult)) + " HP")
            if self.currHp > self.Hp:
                self.currHp = self.Hp
        else:
            Popup("Not Enough Mana!")

        return 'Atk', 0


class Rogue(Assassin):
    def __init__(self, Name):
        Assassin.__init__(self, Name)

    def specialAttack(self, enemy):
        Popup("Coming Soon™!")
        return 'Atk', 0


class Ninja(Assassin):
    def __init__(self, Name):
        Assassin.__init__(self, Name)

    def specialAttack(self, enemy):
        Popup("Coming Soon™!")
        return 'Atk', 0


class Sniper(Marksman):
    def __init__(self, Name):
        Marksman.__init__(self, Name)

    def specialAttack(self, enemy):
        Popup("Coming Soon™!")
        return 'Atk', 0


class Archer(Marksman):
    def __init__(self, Name):
        Marksman.__init__(self, Name)

    def specialAttack(self, enemy):
        Popup("Coming Soon™!")
        return 'Atk', 0


class Vanguard(Tank):
    def __init__(self, Name):
        Tank.__init__(self, Name)

    def specialAttack(self, enemy):
        Popup("Coming Soon™!")
        return 'Atk', 0


class Warden(Tank):
    def __init__(self, Name):
        Tank.__init__(self, Name)

    def specialAttack(self, enemy):
        Popup("Coming Soon™!")
        return 'Atk', 0
