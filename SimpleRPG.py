from Character import Character
from Monster import Monster
from BattleFunctions import *
from Recovery import *
from random import random,randint
import os
from math import *
stats = {
    'Warrior':{'HP':randint(25,35),'Atk':randint(19,21),'Def':randint(20,22),'Spd':randint(1,7),'Mana':30,'Subclass':{'Brusier':False , 'Paladin':False}}, # +Atk +Def -HP
    'Mage':{'HP':randint(15,20),'Atk':randint(28,30),'Def':randint(17,22),'Spd':randint(5,13),'Mana':30,'Subclass':{'Wizard':False , 'Hemomancer':False}}, # +Atk +Mana -Spd
    'Assassin':{'HP':randint(15,20),'Atk':randint(32,34),'Def':randint(9,14),'Spd':randint(15,17),'Mana':30,'Subclass':{'Ninja':False , 'Rogue':False}}, # +Atk +Spd -HP
    'Marksman':{'HP':randint(20,25),'Atk':randint(14,19),'Def':randint(11,19),'Spd':randint(20,22),'Mana':30,'Subclass':{'Sniper':False , 'Archer':False}}, # +Spd -Def
    'Tank':{'HP':randint(35,40),'Atk':randint(1,8),'Def':randint(29,31),'Spd':randint(1,6),'Mana':30,'Subclass':{'Vanguard':False , 'Warden':False}} # +Def +HP -Atk
}

def createCharacter():  
    name = input("Enter Character Name \n")
    rpgClass = input("Enter Wanted Class (Warrior/Mage/Assassin/Marksman/Tank) \n")
    rpgClass = rpgClass.capitalize()
    level = 5
    while rpgClass != "Warrior" and rpgClass != "Mage" and rpgClass != "Assassin" and rpgClass != "Marksman" and rpgClass != "Tank":
        print ('Please choose a valid class')
        rpgClass = input("Enter Wanted Class (Warrior/Mage/Assassin/Marksman/Tank) \n")
        rpgClass = rpgClass.capitalize()
    subclassChoice = list(stats[rpgClass]['Subclass'].keys())
    subclass = input("Select a subclass from " + subclassChoice[0] + " or " + subclassChoice[1] + "\n")
    subclass = subclass.capitalize()
    while subclass not in subclassChoice:
        print ('Please choose a subclass from the list provided')
        subclass = input("Select a subclass from " + subclassChoice[0] + " or " + subclassChoice[1] + "\n")
        subclass = subclass.capitalize()
    return Character(stats[rpgClass]['HP'],stats[rpgClass]['Atk'],stats[rpgClass]['Def'],stats[rpgClass]['Spd'],level,stats[rpgClass]['Mana'],rpgClass,subclass,name)

def sits(num,char):
    if num == 1:
        print ('You come face to face with an enemy. What will you do? (Type to choose choice)')
        battle(char)
        
def battle(char):
    adBuff = 0
    dfBuff = 0
    spBuff = 0
    enemy = Monster(char.Level)
    runAttempt = 1
    scanned = 2
    while enemy.isAlive() == True and char.isAlive() == True:
        print ('                             '+ enemy.Name + ": Lv " + str(enemy.Level))
        print ('                             HP: ' + str(enemy.currHp) + '/' + str(enemy.Hp))
        print (char.Name + " The " + char.Subclass + ": Lv " + str(char.Level))
        print ("HP:   " + str(char.currHp) + '/' + str(char.Hp))
        print ("Mana: " + str(char.currMana) + '/' + str(char.mana))
        print ('Attack      Item        Scan')
        choice = input('Stats       Special     Run\n')
        choice = choice.lower()        
        if choice == 'attack':
            crit,dodge,damage = char.Attack(enemy.Def)
            enCrit,enDodge,enAttack = enemy.Attack(char.Def)
            if turnOrder(char.Spd,enemy.Spd) == 1:
                if damage > 0:
                    if crit == 1:
                        print ("SMASH! You did " + str(damage) + " critical damage!")
                    else:
                        print ('You did ' + str(damage) + " damage!")
                    enemy.takeDamage(damage)
                else:
                    if dodge == 1:
                        print ("Ooof, the monster dodged your attack")
                    else:
                        print ('Your attack missed!')
                
                if enemy.isAlive() == False:
                    print ("You won the battle!")
                    char.addExp(enemy.Level,False)
                    return
                    
                if enAttack > 0:
                    if enCrit == 1:
                        print ("CRAP! Monster did " + str(enAttack) + " critical damage!")
                    else:
                        print ('Monster did ' + str(enAttack) + " damage!")
                    char.takeDamage(enAttack)
                else:
                    if enDodge == 1:
                        print ("Nice! you dodged the attack")
                    else:
                        print ("Monster's attack missed!")
                        
                if char.isAlive()  == False:
                    print ('You Died...')
                    return
            else:
                if enAttack > 0:
                    if enCrit == 1:
                        print ("CRAP! Monster did " + str(enAttack) + " critical damage!")
                    else:
                        print ('Monster did ' + str(enAttack) + " damage!")
                    char.takeDamage(enAttack)
                else:
                    if enDodge == 1:
                        print ("Nice! you dodged the attack")
                    else:
                        print ("Monster's attack missed!")
                        
                if char.isAlive() == False:
                    print ('You Died...')
                    return
                    
                if damage > 0:
                    if crit == 1:
                        print ("SMASH! You did " + str(damage) + " critical damage!")
                    else:
                        print ('You did ' + str(damage) + " damage!")
                    enemy.takeDamage(damage)
                else:
                    if dodge == 1:
                        print ("Ooof, the monster dodged your attack")
                    else:
                        print ('Your attack missed!')
                
                if enemy.isAlive() == False:
                    print ("You won the battle!")
                    char.addExp(enemy.Level,False)
                    return
        elif choice == 'run':
            #if boss == True:
                #print ("You cannot run from the boss!")
            #else:
            num1 = enemy.Spd / 4
            if num1 < 1:
                num1 = 1
            chance = (((char.Spd * 32)/ num1) + 30) * runAttempt / 256
            willIRun = randint(0,255)
            if chance < willIRun:
                print (char.Name + " Ran Away!")
                return
            else:
                print (char.Name + " Tripped and couldn't run!")
                runAttempt += 1
                enCrit,enDodge,enAttack = enemy.Attack(char.Def)
                if enAttack > 0:
                    if enCrit == 1:
                        print ("CRAP! Monster did " + str(enAttack) + " critical damage!")
                    else:
                        print ('Monster did ' + str(enAttack) + " damage!")
                    char.takeDamage(enAttack)
                else:
                    if enDodge == 1:
                        print ("Nice! you dodged the attack")
                    else:
                        print ("Monster's attack missed!")
                        
                if char.isAlive()  == False:
                    print ('You Died...')
        elif choice == 'item':
            if len(char.inventory) == 0:
                print ("You have no items")
            else:
                print (char.inventory)
                item = input ("Type which item you wish to use or type Back to go back\n")
                item = item.capitalize()
                while (item not in char.inventory and item != 'Back'):
                    print ("This is not an item in your bag, try again")
                    item = input ("Type which item you wish to use\n")
                    item = item.capitalize()
                if (item in char.inventory):
                    char.inventory.remove(item)
                    if item == 'Mango':
                        char.currHp = healing(char.currHp,char.Hp)
                    elif item == 'Chenette':
                        char.currMana = manaRestore(char.currMana, char.mana)
                    elif item == 'Doubles':
                        add = randint(3,5)
                        adBuff += add
                        print ("You ate a doubles\nAttack Raised by", add)
                if (item == 'Back'):
                    print ("")                 
        elif choice == 'stats':
            print ('Attack: ' + str(char.Atk+adBuff) + "("+str(adBuff)+")")
            print ('Defense: ' + str(char.Def+dfBuff) + "("+str(dfBuff)+")")
            print ('Speed: ' + str(char.Spd+spBuff) + "("+str(spBuff)+")")
            
        elif choice == 'scan':
            if scanned > 0:
                stat = randint(1,10)
                if stat <= 4:
                    print ("Monster's Attack:",enemy.Atk)
                if stat > 4 and stat <= 8:
                    print ("Monster's Defense:",enemy.Def)
                if stat > 8:
                    print ("Monster's Speed:",enemy.spd)
                scanned -= 1
            else:
                print ("You have already scanned this enemy!")
        else:
            print ("Not a valid choice")
        os.system('pause')
        os.system('CLS')        