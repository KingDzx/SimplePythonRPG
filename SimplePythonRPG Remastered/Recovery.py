from random import random
from PySimpleGUI import Popup
def healing (currHP,hp):
    rand = random()
    if rand <= 0.1:
        Popup("You ate a Super Julie Starch Mango! HP fully restored!")
        currHp += hp
    elif 0.10 < rand <= 0.30:
        Popup("You ate a Julie Starch Mango! Gained " + str(round(hp * 0.75)) + " HP!")
        currHP += round(hp * 0.75)
    elif 0.30 < rand <= 0.65:
        Popup("You ate a Julie Mango! Gained " + str(round(hp * 0.50)) + " HP!")
        currHP += round(hp * 0.50)
    elif rand > 0.65:
        Popup("You ate a Starch Mango! Gained " + str(round(hp * 0.25)) + " HP!")
        currHP += round(hp * 0.25)

    if currHP > hp:
        currHP = hp
    return currHP


def manaRestore(currMana,mana):
    rand = random()
    if rand <= 0.1:
        Popup("You ate a Big Sweet Chenette! Mana fully restored!")
        currMana += mana
    elif 0.10 < rand <= 0.30:
        Popup("You ate a Sweet Chenette! Gained " + str(round(mana * 0.75)) + " Mana!")
        currMana += round(mana * 0.75)
    elif 0.30 < rand <= 0.65:
        Popup("You ate a Chenette! Gained " + str(round(mana * 0.50)) + " Mana!")
        currMana += round(mana * 0.50)
    elif rand > 0.65:
        Popup("You ate an Ok Chenette! Gained " + str(round(mana * 0.25)) + " Mana!")
        currMana += round(mana * 0.25)

    if currMana > mana:
        currMana = mana
    return currMana
