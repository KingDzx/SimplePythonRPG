from random import random
def healing (currHP,hp):
    rand = random()
    if rand <= 0.1:
        print ("You ate a Super Julie Starch Mango! HP fully restored!")
        currHp += hp
    elif rand > 0.10 and rand <= 0.30:
        print ("You ate a Julie Starch Mango! Gained", round(hp * 0.75), "HP!")
        currHP += round(hp * 0.75)
    elif rand > 0.30 and rand <= 0.65:
        print ("You ate a Julie Mango! Gained", round(hp * 0.50), "HP!")
        currHP += round(hp * 0.50)
    elif rand > 0.65:
        print ("You ate a Starch Mango! Gained", round(hp * 0.25), "HP!")
        currHP += round(hp * 0.25)

    if currHP > hp:
        currHP = hp
    return currHP

def manaRestore(currMana,mana):
    rand = random()
    if rand <= 0.1:
        print ("You ate a Big Sweet Chenette! Mana fully restored!")
        currMana += mana
    elif rand > 0.10 and rand <= 0.30:
        print ("You ate a Sweet Chenette! Gained", round(mana * 0.75), "Mana!")
        currMana += round(mana * 0.75)
    elif rand > 0.30 and rand <= 0.65:
        print ("You ate a Chenette! Gained", round(mana * 0.50), "Mana!")
        currMana += round(mana * 0.50)
    elif rand > 0.65:
        print ("You ate an Ok Chenette! Gained", round(mana * 0.25), "Mana!")
        currMana += round(mana * 0.25)

    if currMana > mana:
        currMana = mana
    return currMana
