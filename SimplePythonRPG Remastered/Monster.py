from Entity import Entity
from math import floor
from random import randint, random
class Monster(Entity):
    def __init__(self,Level):
        names = ["Phantomteeth", "Spitesnare", "Hellsnake", "Soulwing", "Dawnsoul"]
        enemyLevel = randint((Level-3),(Level+2))
        if enemyLevel < 1:
            enemyLevel = 1
        if enemyLevel > 100:
            enemyLevel = 100
        HP = round((randint(5,10) + round(randint(1,2) * (random()*3) * enemyLevel)))
        Atk = round((randint(7,11) + round(randint(1,2) * (random()*2.5) * enemyLevel)))
        Def = round((randint(7,11) + round(randint(1,2) * (random()*2.5) * enemyLevel)))
        Spd = round((randint(7,11) + round(randint(1,2) * (random()*2.5) * enemyLevel)))
        Entity.__init__(self,HP,Atk,Def,Spd,enemyLevel,names[randint(0,4)])