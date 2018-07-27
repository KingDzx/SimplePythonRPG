from random import random,randint
import os
from math import *
''' Stats are HP, Attack, Defense, Speed'''
''' All Characters have a MAX power budget of 85 (Max values of each stat in total must not cross 85)'''
stats = {
    'Warrior':{'HP':randint(25,35),'Atk':randint(16,21),'Def':randint(20,22),'Spd':randint(1,7)}, # +Def -HP
    'Mage':{'HP':randint(15,20),'Atk':randint(28,30),'Def':randint(17,22),'Spd':randint(5,13)}, # +Atk -Spd
    'Rogue':{'HP':randint(15,20),'Atk':randint(32,34),'Def':randint(9,14),'Spd':randint(15,17)}, # +Atk +Spd -HP
    'Archer':{'HP':randint(20,25),'Atk':randint(14,19),'Def':randint(11,19),'Spd':randint(20,22)}, # +Spd -Def
    'Tank':{'HP':randint(35,40),'Atk':randint(3,10),'Def':randint(26,28),'Spd':randint(1,7)} # +Def +HP -Atk
}
def createCharacter():  
    name = input("Enter Character Name \n")
    rpgClass = input("Enter Wanted Class (Warrior/Mage/Rogue/Archer/Tank) \n")
    level = 5
    inventory = []
    while rpgClass != "Warrior" and rpgClass != "Mage" and rpgClass != "Rogue" and rpgClass != "Archer" and rpgClass != "Tank":
        print ('Please choose a valid class')
        rpgClass = input("Enter Wanted Class (Warrior/Mage/Rogue/Archer/Tank) \n")
    player = {name:[stats[rpgClass],level,inventory]}
    return player,rpgClass,name

def battle(num,player,pClass,name,exp,hp):
    enemyAlive = True
    Alive = True
    enemyLevel = randint((player[name][1]-2),(player[name][1]+2))
    if enemyLevel < 1:
        enemyLevel = 1
    if enemyLevel > 100:
        enemyLevel = 100
    enemy = {'Monster':[round((randint(8,10) + (randint(1,3) * enemyLevel))) , round((randint(7,9) + (randint(1,2) * enemyLevel))), round((randint(7,9) + (randint(1,2) * enemyLevel))), round((randint(7,9) + (randint(1,2) * enemyLevel)))]}
    enemyHp = enemy['Monster'][0]
    runAttempt = 1
    while enemyAlive == True and Alive == True:
        print ('                             ' + str(enemy['Monster']))
        print ('                             Monster: Lv ' + str(enemyLevel))
        print ('                             ' + str(enemyHp) + '/' + str(enemy['Monster'][0]))
        print (name + ": Lv " + str(player[name][1]))
        print (str(hp) + '/' + str(player[name][0]['HP']))
        print ('Attack     Item')
        choice = input('Run        Stats \n')
        choice = choice.lower()
        if choice == 'attack':
            crit,dodge,damage = calDamage(player[name][0]['Atk'],enemy['Monster'][2],player[name][1])
            enCrit,enDodge,enAttack = calDamage(enemy['Monster'][1],player[name][0]['Def'],enemyLevel)           
            if turnOrder(player[name][0]['Spd'],enemy['Monster'][3]) == 1:
                if damage > 0:
                    if crit == 1:
                        print ("SMASH! You did " + str(damage) + " critical damage!")
                    else:
                        print ('You did ' + str(damage) + " damage!")
                    enemyHp = enemyHp - damage
                else:
                    if dodge == 1:
                        print ("Ooof, the monster dodged your attack")
                    else:
                        print ('Your attack missed!')
                    
                if enemyHp <= 0:
                    enemyAlive = False
                    print ('You won the battle!')
                    if player[name][1] < 100:
                        gain = round(((randint(35,75) * enemyLevel) * 1.5) / 7)
                        print ('You gained ' + str(gain) + ' exp')
                        newExp = exp + gain
                        lvlup = (player[name][1]+1)**3
                        if newExp > lvlup:
                            hp = levelUp(newExp,lvlup,player,pClass,hp)
                        return newExp,hp
                    return exp,hp
                
                if enAttack > 0:
                    if enCrit == 1:
                        print ("CRAP! Monster did " + str(enAttack) + " critical damage!")
                    else:
                        print ('Monster did ' + str(enAttack) + " damage!")
                    hp = hp - enAttack 
                else:
                    if enDodge == 1:
                        print ("Nice! you dodged the attack")
                    else:
                        print ("Monster's attack missed!")
                    
                if hp <= 0:
                    Alive = False
                    print ('You Died...')
                    return exp,hp
            else:
                if enAttack > 0:
                    if enCrit == 1:
                        print ("CRAP! Monster did " + str(enAttack) + " critical damage!")
                    else:
                        print ('Monster did ' + str(enAttack) + " damage!")
                    hp = hp - enAttack 
                else:
                    if enDodge == 1:
                        print ("Nice! you dodged the attack")
                    else:
                        print ("Monster's attack missed!")
                    
                if hp <= 0:
                    Alive = False
                    print ('You Died...')
                    return exp,hp
                
                if damage > 0:
                    if crit == 1:
                        print ("SMASH! You did " + str(damage) + " critical damage!")
                    else:
                        print ('You did ' + str(damage) + " damage!")
                    enemyHp = enemyHp - damage
                else:
                    if dodge == 1:
                        print ("Ooof, the monster dodged your attack")
                    else:
                        print ('Your attack missed!')
                    
                if enemyHp <= 0:
                    enemyAlive = False
                    print ('You won the battle!')
                    if player[name][1] < 100:
                        gain = round(((randint(35,75) * enemyLevel) * 1.5) / 7)
                        print ('You gained ' + str(gain) + ' exp')
                        newExp = exp + gain
                        lvlup = (player[name][1]+1)**3
                        if newExp > lvlup:
                            hp = levelUp(newExp,lvlup,player,pClass,hp)
                        return newExp,hp
                    return exp,hp
                
        elif choice == 'run':
            chance = (((player[name][0]['Spd'] * 32)/enemy['Monster'][3]) +30) * runAttempt
            if chance > 255:
                print (name + " Ran Away!")
                return exp,hp
            else:
                willIRun = randint(0,255)
                if chance < willIRun:
                    print (name + " Ran Away!")
                    return exp,hp
                else:
                    print (name + " Tripped and couldn't run!")
                    runAttempt += 1
                    enCrit,enDodge,enAttack = calDamage(enemy['Monster'][1],player[name][0]['Def'],enemyLevel)
                    if enAttack > 0:
                        if enCrit == 1:
                            print ("CRAP! Monster did " + str(enAttack) + " critical damage!")
                        else:
                            print ('Monster did ' + str(enAttack) + " damage!")
                        hp = hp - enAttack 
                    else:
                        if enDodge == 1:
                            print ("Nice! you dodged the attack")
                        else:
                            print ("Monster's attack missed!")
                    if hp <= 0:
                        Alive = False
                        print ('You Died...')
                        return exp,hp
                    
        elif choice == 'item':
            if len(player[name][2]) == 0:
                print ("You have no items")
            else:
                print (player[name][2])
                item = input ("Type which item you wish to use or type Back to go back\n")
                while (item not in player[name][2] and item != 'Back'):
                    print ("This is not an item in your bag, try again")
                    item = input ("Type which item you wish to use\n")
                if (item in player[name][2]):
                    player[name][2].remove(item)
                    if item == 'Mango':
                         hp = healing(hp)
                if (item == 'Back'):
                    print ("")
                
        elif choice == 'stats':
            stats = player[name][0]
            print ('HP: ' + str(stats['HP']))
            print ('Attack: ' + str(stats['Atk']))
            print ('Defense: ' + str(stats['Def']))
            print ('Speed: ' + str(stats['Spd']))
            
        elif choice == 'heal':
            print ("Shhhhhhh don't tell anyone about this command ;)")
            hp = player[name][0]['HP']
            
        else:
            print ("Not a valid choice")
            
        os.system('pause')
        os.system('CLS')
            
def levelUp(gain,lvlup,player,Class,HP):
    while gain > lvlup:
        if player[name][1] == 100:
            break
        print ('You gained a level!')
        hpGain = randint(2,7)
        if Class == 'Warrior' or Class == 'Rogue':
            hpGain = int(floor(hpGain * 0.5))
        elif Class == 'Tank':
            hpGain = randint(7,10)
        atkGain = randint(1,5)
        if Class == 'Mage':
            atkGain = int(floor(atkGain * 2))
        elif Class == 'Rogue':
            atkGain = randint(4,6)
        elif Class == 'Tank':
            atkGain = int(floor(atkGain * 0.5))
        defGain = randint(1,5)
        if Class == 'Warrior':
            defGain = int(floor(defGain * 2))
        elif Class == 'Tank':
            defGain = randint(4,6)
        elif Class == 'Archer':
            defGain = int(floor(defGain * 0.5))
        spdGain = randint(1,5)
        if Class == 'Archer':
            spdGain = int(floor(spdGain * 2))
        if Class == 'Rogue':
            spdGain = randint(4,6)
        elif Class == 'Mage':
            spdGain = int(floor(spdGain * 0.5))

        print ('HP: ' + str(player[name][0]['HP']) + ' -> ' + str(player[name][0]['HP'] + hpGain) + ' +' + str(hpGain))
        print ('Attack: ' + str(player[name][0]['Atk']) + ' -> ' + str(player[name][0]['Atk'] + atkGain) + ' +' + str(atkGain))
        print ('Defense: ' + str(player[name][0]['Def']) + ' -> ' + str(player[name][0]['Def'] + defGain) + ' +' + str(defGain))
        print ('Speed: ' + str(player[name][0]['Spd']) + ' -> ' + str(player[name][0]['Spd'] + spdGain) + ' +' + str(spdGain))
        print ('\n')
        player[name][1] = player[name][1] + 1
        player[name][0]['HP'] = player[name][0]['HP'] + hpGain
        player[name][0]['Atk'] = player[name][0]['Atk'] + atkGain
        player[name][0]['Def'] = player[name][0]['Def'] + defGain
        player[name][0]['Spd'] = player[name][0]['Spd'] + spdGain
        lvlup = (player[name][1]+1)**3
        HP = HP + hpGain
    return HP

def situations(num,player,pClass,name,exp,hp):
    if num == 1:
        print ('You come face to face with an enemy. What will you do? (Type to choose choice)')
        return battle(num,player,pClass,name,exp,hp)
        
    elif num == 2:
        print ("It's an empty room...")
        rand = random()
        if rand <= 0.5:
            os.system('pause')
            print ("You turn to leave and an enemy attacks you!")
            return battle(num,player,pClass,name,exp,hp)
        else:
            return exp,hp

    elif num == 3:
        print ("You enter a room, there's a chest!")
        choice = input("Do you want to open it? (Yes/No)")
        choice = choice.lower()
        os.system('CLS')
        while choice != 'yes' and choice != 'no':
            choice = input ("You must choose to open it or not! (Yes/No)")
            choice = choice.lower()
        if choice == 'no':
            print ("You walked out. You don't trust what the chest might contain")
            return exp,hp
        elif choice == 'yes':
            encounter = randint(1,10)
            if encounter%2 == 0:
                print ("You encounter an enemy!")
                return battle(num,player,pClass,name,exp,hp)
            else:
                print ('You Obtained an item!')
                player[name][2].append('Mango')
                return exp,hp

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
    damage = round(((((2 * level / 5 + 2) * attack * randint(30,100) / defense) / 50) + 2) * random())
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

def healing (hp):
    rand = random()
    if rand <= 0.1:
        hp = player[name][0]['HP']
    elif rand > 0.1 and rand <= 0.25:
        hp += round(player[name][0]['HP'] * 0.75)
    elif rand > 0.25 and rand <= 0.50:
        hp += round(player[name][0]['HP'] * 0.50)
    elif rand > 0.50:
        hp += round(player[name][0]['HP'] * 0.25)

    if hp > player[name][0]['HP']:
        hp = player[name][0]['HP']
    return hp
player,pClass,name = createCharacter()
exp=player[name][1]**3
leave = False
hp = player[name][0]['HP']
print ("Your Stats are:")
print ('HP: ' + str(player[name][0]['HP']))
print ('Attack: ' + str(player[name][0]['Atk']))
print ('Defense: ' + str(player[name][0]['Def']))
print ('Speed: ' + str(player[name][0]['Spd']))
os.system('pause')
os.system('CLS')
print ("You enter into Laventille Square")
while leave == False and hp > 0:
    print ('Pick a direction to go')
    print ('       Up      ')
    print ('Left       Right')
    print ('      Down     ')
    print ('                    Exit')
    choice = input('Type direction or exit to leave game \n')
    choice = choice.lower()
    os.system('CLS')
    if choice == 'exit':
        leave = True
    elif choice == 'up' or choice == 'down' or choice == 'left' or choice == 'right' :
        sit = random()
        if sit <= 0.5:
            num = 1
        elif sit > 0.5 and sit <= 0.75:
            num = 2
        elif sit > 0.75 and sit <= 1.0:
            num = 3
        new = situations(num,player,pClass,name,exp,hp)
        exp = new[0]
        hp = new[1]
    else:
        print ("Not a choice, please enter a valid choice")
    os.system('pause')
    os.system('CLS')
    
print ("Thanks for playing!")
print ("You got to level " + str(player[name][1]))
os.system('pause')
