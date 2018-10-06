from random import random, randint
def critChance():
    Crit=0
    critChance = random()
    if critChance <= 0.1:
        Crit = 1
    else:
        Crit = 0
    return Crit

def dodgeChance():
    Dodge = 0
    dodChance = random()
    if dodChance <= 0.1:
        Dodge = 1
    else:
        Dodge = 0
    return Dodge

def calDamage(attack,defense,level):
    crit = critChance()
    dodge = dodgeChance()
    damage = round(((((2 * level / 5 + 2) * attack * randint(30,100) / defense) / 50) + 2) * (randint(1,100) / 100))
    if crit == 1:
        damage *= 1.5
    if dodge == 1:
        damage = 0
    return crit,dodge,round(damage)

def turnOrder(speed,enSpeed):
    if speed > enSpeed:
        return 1
    elif speed < enSpeed:
        return 0
    elif speed == enSpeed:
        return randint(0,1)
