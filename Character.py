from Entity import Entity
from math import floor, sqrt
from random import randint, random
class Character(Entity):
    def __init__(self,Hp,Atk,Def,Spd,Level,mana,Class,Subclass,Name):
        Entity.__init__(self,Hp,Atk,Def,Spd,Level,Name)
        self.mana = mana
        self.currMana = mana
        self.exp = floor(1.2 * Level ** 3 - 15 * Level ** 2 + 100 * Level - 140)
        self.Class = Class
        self.Subclass = Subclass
        self.inventory = ["Mango", "Chenette", "Doubles"]

    def addExp(self,enemyLevel,boss):
        nextLevel = self.Level + 1
        A = (enemyLevel * 2) + 10
        C = (enemyLevel + self.Level + 10)
        if boss == False:
            B = (randint(35,75) * enemyLevel) /5
        else:
            B = (randint(150,250) * enemyLevel) /5 * 1.5
        gain = floor(floor(sqrt(A) * (A*A)) * B / floor(sqrt(C) * (C*C)))+1
        self.exp += gain 
        lvlup = floor(1.2 * nextLevel ** 3 - 15 * nextLevel ** 2 + 100 * nextLevel - 140) #(player[name][1]+1)**3
        print ('You gained ' + str(gain) + ' exp')
        while self.exp > lvlup:
            if self.Level == 100:
                break
            if self.Level< 100:                                   
                if self.exp > lvlup:
                    print ('You gained a level!')
                    hpGain = randint(2,7)
                    if self.Class == 'Warrior' or self.Class == 'Assassin':
                        hpGain = int(floor(hpGain * 0.5))
                    elif self.Class == 'Tank':
                        hpGain = randint(7,10)
                        
                    atkGain = randint(1,4)
                    if self.Class == 'Mage':
                        atkGain = int(floor(atkGain * 1.5))
                    elif self.Class == 'Assassin' or self.Class == "Warrior":
                        atkGain = randint(3,5)
                    elif self.Class == 'Tank':
                        atkGain = int(floor(atkGain * 0.5))
                        
                    defGain = randint(1,4)
                    if self.Class == 'Tank' or self.Class == 'Warrior':
                        defGain = randint(3,5)
                    elif self.Class == 'Marksman':
                        defGain = int(floor(defGain * 0.5))
                        
                    spdGain = randint(1,4)
                    if self.Class == 'Marksman':
                        spdGain = int(floor(spdGain * 1.5))
                    if self.Class == 'Assassin':
                        spdGain = randint(3,5)
                    elif self.Class == 'Mage':
                        spdGain = int(floor(spdGain * 0.5))
    
                    manaGain = randint(5,10)
                    if self.Class == 'Mage':
                        manaGain = int(floor(manaGain * 1.5))
                    
                    print ('HP:', self.Hp, "+", hpGain, "=", self.Hp + hpGain)
                    print ('Attack:', self.Atk, "+", atkGain, "=", self.Atk + atkGain)
                    print ('Defense:', self.Def, "+", defGain, "=", self.Def + defGain)
                    print ('Speed:', self.Spd, "+", spdGain, "=", self.Spd + spdGain)
                    print ('Mana:', self.mana, "+", manaGain, "=", self.mana + manaGain)
                    print ('\n')
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