from Character import Character
from math import floor, sqrt
from random import randint
from PySimpleGUI import Popup


class Mage(Character): # +Atk +Mana -Spd
    def __init__(self, Name):
        Character.__init__(self, randint(15, 20), randint(28, 30), randint(17, 22), randint(1, 7), 5, 30, Name)

    def addExp(self, enemyLevel, boss):
        nextLevel = self.Level + 1
        A = (enemyLevel * 2) + 10
        C = (enemyLevel + self.Level + 10)
        if not boss:
            B = (randint(35, 75) * enemyLevel) / 5
        else:
            B = (randint(150, 250) * enemyLevel) / 5 * 1.5
        gain = floor(floor(sqrt(A) * (A * A)) * B / floor(sqrt(C) * (C * C))) + 1
        self.exp += gain
        lvlup = floor(1.2 * nextLevel ** 3 - 15 * nextLevel ** 2 + 100 * nextLevel - 140)  # (player[name][1]+1)**3
        if self.Level < 100:
            Popup('You gained ' + str(gain) + ' exp')
        while self.exp > lvlup:
            if self.Level == 100:
                break
            if self.Level < 100:
                if self.exp > lvlup:

                    hpGain = randint(2, 7)
                    atkGain = int(floor(randint(1, 4) * 1.5))
                    defGain = randint(1, 4)
                    spdGain = int(floor(randint(1, 4) * 0.5))
                    manaGain = int(floor(randint(5, 10) * 1.25))

                    Popup('You gained a level!',
                          'HP: ' + str(self.Hp) + " + " + str(hpGain) + " = " + str(self.Hp + hpGain),
                          'Attack: ' + str(self.Atk) + " + " + str(atkGain) + " = " + str(self.Atk + atkGain),
                          'Defense: ' + str(self.Def) + " + " + str(defGain) + " = " + str(self.Def + defGain),
                          'Speed: ' + str(self.Spd) + " + " + str(spdGain) + " = " + str(self.Spd + spdGain),
                          'Mana: ' + str(self.mana) + " + " + str(manaGain) + " = " + str(self.mana + manaGain))

                    self.Level += 1
                    self.Hp += hpGain
                    self.Atk += atkGain
                    self.Def += defGain
                    self.Spd += spdGain
                    self.mana += manaGain
                    nextLevel = self.Level + 1
                    lvlup = floor(1.2 * nextLevel ** 3 - 15 * nextLevel ** 2 + 100 * nextLevel - 140)
                    self.currHp += hpGain
                    self.currMana += manaGain


class Assassin(Character): # +Atk +Spd -HP
    def __init__(self, Name):
        Character.__init__(self, randint(15, 20), randint(32, 34), randint(9, 14), randint(15, 17), 5, 30, Name)

    def addExp(self, enemyLevel, boss):
        nextLevel = self.Level + 1
        A = (enemyLevel * 2) + 10
        C = (enemyLevel + self.Level + 10)
        if not boss:
            B = (randint(35, 75) * enemyLevel) / 5
        else:
            B = (randint(150, 250) * enemyLevel) / 5 * 1.5
        gain = floor(floor(sqrt(A) * (A * A)) * B / floor(sqrt(C) * (C * C))) + 1
        self.exp += gain
        lvlup = floor(1.2 * nextLevel ** 3 - 15 * nextLevel ** 2 + 100 * nextLevel - 140)  # (player[name][1]+1)**3
        if self.Level < 100:
            Popup('You gained ' + str(gain) + ' exp')
        while self.exp > lvlup:
            if self.Level == 100:
                break
            if self.Level < 100:
                if self.exp > lvlup:
                    hpGain = int(floor(randint(2, 7) * 0.5))
                    atkGain = randint(3, 5)
                    defGain = randint(1, 4)
                    spdGain = randint(3, 5)
                    manaGain = randint(5, 10)

                    Popup('You gained a level!',
                          'HP: ' + str(self.Hp) + " + " + str(hpGain) + " = " + str(self.Hp + hpGain),
                          'Attack: ' + str(self.Atk) + " + " + str(atkGain) + " = " + str(self.Atk + atkGain),
                          'Defense: ' + str(self.Def) + " + " + str(defGain) + " = " + str(self.Def + defGain),
                          'Speed: ' + str(self.Spd) + " + " + str(spdGain) + " = " + str(self.Spd + spdGain),
                          'Mana: ' + str(self.mana) + " + " + str(manaGain) + " = " + str(self.mana + manaGain))

                    self.Level += 1
                    self.Hp += hpGain
                    self.Atk += atkGain
                    self.Def += defGain
                    self.Spd += spdGain
                    self.mana += manaGain
                    nextLevel = self.Level + 1
                    lvlup = floor(1.2 * nextLevel ** 3 - 15 * nextLevel ** 2 + 100 * nextLevel - 140)
                    self.currHp += hpGain
                    self.currMana += manaGain


class Warrior(Character): # +Atk +Def -HP
    def __init__(self, Name):
        Character.__init__(self, randint(25, 35), randint(19, 21), randint(20, 22), randint(1, 7), 5, 30, Name)

    def addExp(self, enemyLevel, boss):
        nextLevel = self.Level + 1
        A = (enemyLevel * 2) + 10
        C = (enemyLevel + self.Level + 10)
        if not boss:
            B = (randint(35, 75) * enemyLevel) / 5
        else:
            B = (randint(150, 250) * enemyLevel) / 5 * 1.5
        gain = floor(floor(sqrt(A) * (A * A)) * B / floor(sqrt(C) * (C * C))) + 1
        self.exp += gain
        lvlup = floor(1.2 * nextLevel ** 3 - 15 * nextLevel ** 2 + 100 * nextLevel - 140)  # (player[name][1]+1)**3
        if self.Level < 100:
            Popup('You gained ' + str(gain) + ' exp')
        while self.exp > lvlup:
            if self.Level == 100:
                break
            if self.Level < 100:
                if self.exp > lvlup:
                    hpGain = int(floor(randint(2, 7) * 0.5))
                    atkGain = randint(3, 5)
                    defGain = randint(3, 5)
                    spdGain = randint(1, 4)
                    manaGain = randint(5, 10)

                    Popup('You gained a level!',
                          'HP: ' + str(self.Hp) + " + " + str(hpGain) + " = " + str(self.Hp + hpGain),
                          'Attack: ' + str(self.Atk) + " + " + str(atkGain) + " = " + str(self.Atk + atkGain),
                          'Defense: ' + str(self.Def) + " + " + str(defGain) + " = " + str(self.Def + defGain),
                          'Speed: ' + str(self.Spd) + " + " + str(spdGain) + " = " + str(self.Spd + spdGain),
                          'Mana: ' + str(self.mana) + " + " + str(manaGain) + " = " + str(self.mana + manaGain))

                    self.Level += 1
                    self.Hp += hpGain
                    self.Atk += atkGain
                    self.Def += defGain
                    self.Spd += spdGain
                    self.mana += manaGain
                    nextLevel = self.Level + 1
                    lvlup = floor(1.2 * nextLevel ** 3 - 15 * nextLevel ** 2 + 100 * nextLevel - 140)
                    self.currHp += hpGain
                    self.currMana += manaGain


class Tank(Character):  # +Def +HP -Atk
    def __init__(self, Name):
        Character.__init__(self, randint(35, 40), randint(1, 8), randint(29, 31), randint(1, 6), 5, 30, Name)

    def addExp(self, enemyLevel, boss):
        nextLevel = self.Level + 1
        A = (enemyLevel * 2) + 10
        C = (enemyLevel + self.Level + 10)
        if not boss:
            B = (randint(35, 75) * enemyLevel) / 5
        else:
            B = (randint(150, 250) * enemyLevel) / 5 * 1.5
        gain = floor(floor(sqrt(A) * (A * A)) * B / floor(sqrt(C) * (C * C))) + 1
        self.exp += gain
        lvlup = floor(1.2 * nextLevel ** 3 - 15 * nextLevel ** 2 + 100 * nextLevel - 140)  # (player[name][1]+1)**3
        if self.Level < 100:
            Popup('You gained ' + str(gain) + ' exp')
        while self.exp > lvlup:
            if self.Level == 100:
                break
            if self.Level < 100:
                if self.exp > lvlup:
                    hpGain = randint(7, 10)
                    atkGain = int(floor(randint(1, 4) * 0.5))
                    defGain = randint(3, 5)
                    spdGain = randint(1, 4)
                    manaGain = randint(5, 10)

                    Popup('You gained a level!',
                          'HP: ' + str(self.Hp) + " + " + str(hpGain) + " = " + str(self.Hp + hpGain),
                          'Attack: ' + str(self.Atk) + " + " + str(atkGain) + " = " + str(self.Atk + atkGain),
                          'Defense: ' + str(self.Def) + " + " + str(defGain) + " = " + str(self.Def + defGain),
                          'Speed: ' + str(self.Spd) + " + " + str(spdGain) + " = " + str(self.Spd + spdGain),
                          'Mana: ' + str(self.mana) + " + " + str(manaGain) + " = " + str(self.mana + manaGain))

                    self.Level += 1
                    self.Hp += hpGain
                    self.Atk += atkGain
                    self.Def += defGain
                    self.Spd += spdGain
                    self.mana += manaGain
                    nextLevel = self.Level + 1
                    lvlup = floor(1.2 * nextLevel ** 3 - 15 * nextLevel ** 2 + 100 * nextLevel - 140)
                    self.currHp += hpGain
                    self.currMana += manaGain


class Marksman(Character): # +Spd -Def
    def __init__(self, Name):
        Character.__init__(self, randint(20, 25), randint(14, 19), randint(11, 19), randint(20, 22), 5, 30, Name)

    def addExp(self, enemyLevel, boss):
        nextLevel = self.Level + 1
        A = (enemyLevel * 2) + 10
        C = (enemyLevel + self.Level + 10)
        if not boss:
            B = (randint(35, 75) * enemyLevel) / 5
        else:
            B = (randint(150, 250) * enemyLevel) / 5 * 1.5
        gain = floor(floor(sqrt(A) * (A * A)) * B / floor(sqrt(C) * (C * C))) + 1
        self.exp += gain
        lvlup = floor(1.2 * nextLevel ** 3 - 15 * nextLevel ** 2 + 100 * nextLevel - 140)  # (player[name][1]+1)**3
        if self.Level < 100:
            Popup('You gained ' + str(gain) + ' exp')
        while self.exp > lvlup:
            if self.Level == 100:
                break
            if self.Level < 100:
                if self.exp > lvlup:
                    print('You gained a level!')
                    hpGain = randint(2, 7)
                    atkGain = randint(1, 4)
                    defGain = int(floor(randint(1, 4) * 0.5))
                    spdGain = int(floor(randint(1, 4) * 1.5))
                    manaGain = randint(5, 10)

                    Popup('You gained a level!',
                          'HP: ' + str(self.Hp) + " + " + str(hpGain) + " = " + str(self.Hp + hpGain),
                          'Attack: ' + str(self.Atk) + " + " + str(atkGain) + " = " + str(self.Atk + atkGain),
                          'Defense: ' + str(self.Def) + " + " + str(defGain) + " = " + str(self.Def + defGain),
                          'Speed: ' + str(self.Spd) + " + " + str(spdGain) + " = " + str(self.Spd + spdGain),
                          'Mana: ' + str(self.mana) + " + " + str(manaGain) + " = " + str(self.mana + manaGain))

                    self.Level += 1
                    self.Hp += hpGain
                    self.Atk += atkGain
                    self.Def += defGain
                    self.Spd += spdGain
                    self.mana += manaGain
                    nextLevel = self.Level + 1
                    lvlup = floor(1.2 * nextLevel ** 3 - 15 * nextLevel ** 2 + 100 * nextLevel - 140)
                    self.currHp += hpGain
                    self.currMana += manaGain
