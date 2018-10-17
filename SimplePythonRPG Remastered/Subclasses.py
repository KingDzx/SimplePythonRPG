from Classes import *
from random import randint, random


class Wizard(Mage):
    def __init__(self, Name):
        Mage.__init__(self, Name)

    def specialAttack(self,enemy):
        if self.currMana >= 12:
            self.currMana -= 12
            print("You cast a dark magic to gain an advantage against the opponent!")
            buff = random()
            if buff <= 0.33:
                atkBuff = randint(3, 5)
                print("A harsh red light casts down upon you\nYou gained ", atkBuff, "Attack!")
                return 'Atk', atkBuff
            elif buff > 0.33 and buff <= 0.67:
                defBuff = randint(3, 5)
                print("A subtle green light casts down upon you\nYou gained ", defBuff, "Defense!")
                return 'Def', defBuff
            elif buff > 0.67:
                spdBuff = randint(3, 5)
                print("A quick blue light casts down upon you\nYou gained" , spdBuff, "Speed!")
                return 'Spd', spdBuff
        else:
            print("Not Enough Mana!")


class Hemomancer(Mage):
    def __init__(self, Name):
        Mage.__init__(self, Name)

    def specialAttack(self, enemy):
        if self.currMana >= 20:
            self.currMana -= 20
            print ("You use your magic to manipulate the enemy's blood!")
            damage = round(((((2 * self.Level / 5 + 2) * self.Atk * randint(30,100) / enemy.Def) / 50) + 2) * (randint(1,100) / 100))
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
                print ("You tried to cast your magic but it failed!")
                self.currMana += 10
            else:
                print ("You dealt", damage, "damage and healed for" , heal)
        else:
            print ("Not Enough Mana!")


class Bruiser(Warrior):
    def __init__(self, Name):
        Warrior.__init__(self, Name)

    def specialAttack(self, enemy):
        self.currMana -= 10
        damage = round(((((2 * self.Level / 5 + 2) * self.Atk * randint(150, 200) / enemy.Def) / 50) + 2) * (randint(1, 100) / 100))
        enemy.takeDamage(damage)
        self.currHp -= round(damage * 0.20)
        print("You strike with the force of give or take a few hundred suns")
        print("You dealt", damage, "holy damage!")
        print("You took", round(damage * 0.20), "splash damage!")
        if self.currHp < 0:
            self.currHp = 1
            print ("You barely hold on with 1 HP after that attack")


class Paladin(Warrior):
    def __init__(self, Name):
        Warrior.__init__(self, Name)

    def specialAttack(self, enemy):
        if self.currMana >= 25:
            self.currMana -= 25
            self.currHp += round(self.Hp * 0.75)
            print ("You blessed yourself with a holy light!")
            print ("You healed", round(self.Hp * 0.75), "HP")
            if self.currHp > self.Hp:
                self.currHp = self.Hp
        else:
            print ("Not Enough Mana!")


class Rogue(Assassin):
    def __init__(self,Name):
        Assassin.__init__(self,Name)

    def specialAttack(self, enemy):
        print("Coming Soon™!")


class Ninja(Assassin):
    def __init__(self, Name):
        Assassin.__init__(self, Name)

    def specialAttack(self, enemy):
        print("Coming Soon™!")


class Sniper(Marksman):
    def __init__(self, Name):
        Marksman.__init__(self, Name)

    def specialAttack(self, enemy):
        print("Coming Soon™!")


class Archer(Marksman):
    def __init__(self, Name):
        Marksman.__init__(self, Name)

    def specialAttack(self, enemy):
        print("Coming Soon™!")


class Vanguard(Tank):
    def __init__(self, Name):
        Tank.__init__(self, Name)

    def specialAttack(self, enemy):
        print("Coming Soon™!")


class Warden(Tank):
    def __init__(self, Name):
        Tank.__init__(self, Name)

    def specialAttack(self, enemy):
        print("Coming Soon™!")