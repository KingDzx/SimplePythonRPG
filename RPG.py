from random import random,randint
import os
from math import *
''' Stats are HP, Attack, Defense, Speed'''
''' All Characters have a power budget of 75'''
stats = {
    'Warrior':{'HP':35,'Atk':18,'Def':17,'Spd':3}, # +Def -HP
    'Mage':{'HP':20,'Atk':27,'Def':15,'Spd':13}, # +Atk -Spd
    'Rogue':{'HP':15,'Atk':31,'Def':8,'Spd':21}, # +Atk -Def
    'Archer':{'HP':25,'Atk':19,'Def':17,'Spd':14}, # +Spd -Def
    'Tank':{'HP':50,'Atk':5,'Def':20,'Spd':3} # +Def +HP -Atk
}
def createCharacter():  
    name = raw_input("Enter Character Name \n")
    rpgClass = raw_input("Enter Wanted Class (Warrior/Mage/Rogue/Archer/Tank) \n")
    level = 5
    inventory = []
    while rpgClass != "Warrior" and rpgClass != "Mage" and rpgClass != "Rogue" and rpgClass != "Archer" and rpgClass != "Tank":
        print ('Please choose a valid class')
        rpgClass = raw_input("Enter Wanted Class (Warrior/Mage/Rogue/Archer/Tank) \n")
    player = {name:[stats[rpgClass],level,inventory]}
    return player,rpgClass,name

def battle(num,player,pClass,name,exp,hp):
    enemyAlive = True
    Alive = True
    enemyLevel = randint((player[name][1]-4),(player[name][1]+4))
    if enemyLevel < 1:
        enemyLevel = 1
    enemy = {'Monster':[round((randint(11,15)*enemyLevel +5)/ player[name][1]) , round((randint(6,15)*enemyLevel +5)/ player[name][1]), round((randint(6,15)*enemyLevel +5) / player[name][1]), round((randint(6,10)*enemyLevel +5) / player[name][1])]}
    enemyHp = enemy['Monster'][0]
    runAttempt = 1
    while enemyAlive == True and Alive == True:
        print ('                             ' + str(enemy['Monster']))
        print ('                             Monster: Lv ' + str(enemyLevel))
        print ('                             ' + str(enemyHp) + '/' + str(enemy['Monster'][0]))
        print (name + ": Lv " + str(player[name][1]))
        print (str(hp) + '/' + str(player[name][0]['HP']))
        print ('Attack     Item')
        choice = raw_input('Run        Stats \n')
        choice = choice.lower()
        if choice == 'attack':
            damage = round(((((2 * player[name][1] / 5 + 2) * player[name][0]['Atk'] * randint(30,100) / enemy['Monster'][2]) / 50) + 2) * random()*100/100)
            enAttack = round(((((2 * enemyLevel / 5 + 2) * enemy['Monster'][1] * randint(30,100) / player[name][0]['Def']) / 50) + 2) * random()*100/100)
            if player[name][0]['Spd'] > enemy['Monster'][3]:
                print ('You did ' + str(damage) + " damage!")
                enemyHp = enemyHp - damage
                if enemyHp <= 0:
                    enemyAlive = False
                    print ('You won the battle!')
                    gain = round(((random() * 100 * enemyLevel) * 1.25) / 7)
                    print ('You gained ' + str(gain) + ' exp')
                    newExp = exp + gain
                    lvlup = (player[name][1]+1)**3
                    if newExp > lvlup:
                        hp = levelUp(newExp,lvlup,player,pClass,hp)
                    return newExp,hp
                print ('Monster did ' + str(enAttack) + " damage!")
                hp = hp - enAttack                                
                if hp <= 0:
                    Alive = False
                    print ('You Died...')
                    return exp,hp
            else:
                print ('Monster did ' + str(enAttack) + " damage!")
                hp = hp - enAttack                                
                if hp <= 0:
                    Alive = False
                    print ('You Died...')
                    return exp,hp
                print ('You did ' + str(damage) + " damage!")
                enemyHp = enemyHp - damage
                if enemyHp <= 0:
                    enemyAlive = False
                    print ('You won the battle!')
                    gain = round(((random() * 100 * enemyLevel) * 1.25) / 7)
                    print ('You gained ' + str(gain) + ' exp')
                    newExp = exp + gain
                    lvlup = (player[name][1]+1)**3
                    if newExp > lvlup:
                        hp = levelUp(newExp,lvlup,player,pClass,hp)
                    return newExp,hp
                
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
                    runAttempt = runAttempt + 1
                    enAttack = round(((((2 * player[name][1] / 5 + 2) * enemy['Monster'][1] * 40 / player[name][0]['Def']) / 50) + 2) * random()*100/100)
                    print ('Monster did ' + str(enAttack) + " damage!")
                    hp = hp - enAttack
                    if hp <= 0:
                        Alive = False
                        print ('You Died...')
                        return exp,hp
                    
        elif choice == 'item':
            if len(player[name][2]) == 0:
                print ("You have no items")
            else:
                print (player[name][2])
                item = raw_input ("Type which item you wish to use or type Back to go back\n")
                while (item not in player[name][2] and item != 'Back'):
                    print ("This is not an item in your bag, try again")
                    item = raw_input ("Type which item you wish to use\n")
                if (item in player[name][2]):
                    player[name][2].remove(item)
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
        print ('You gained a level!')
        hpGain = randint(1,10)
        if Class == 'Warrior':
            hpGain = int(floor(hpGain * 0.5))
        elif Class == 'Tank':
            hpGain = randint(5,10)
        atkGain = randint(1,5)
        if Class == 'Mage' or Class == 'Rogue':
            atkGain = int(floor(atkGain * 2))
        elif Class == 'Tank':
            atkGain = int(floor(atkGain * 0.5))
        defGain = randint(1,5)
        if Class == 'Warrior':
            defGain = int(floor(defGain * 2))
        elif Class == 'Tank':
            defGain = randint(4,7)
        elif Class == 'Archer' or Class == 'Rogue':
            defGain = int(floor(defGain * 0.5))
        spdGain = randint(1,5)
        if Class == 'Archer':
            spdGain = int(floor(spdGain * 2))
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
        return exp,hp

    elif num == 3:
        print ("You enter a room, there's a chest!")
        choice = raw_input("Do you want to open it? (Yes/No)")
        choice = choice.lower()
        os.system('CLS')
        while choice != 'yes' and choice != 'no':
            choice = raw_input ("You must choose to open it or not! (Yes/No)")
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
                player[name][2].append('Test')
                return exp,hp
            
player,pClass,name = createCharacter()
exp=0
leave = False
hp = player[name][0]['HP']
os.system('CLS')
print ("You enter into the Beetham to find the misstress")
while leave == False and hp > 0:
    print ('Pick a direction to go')
    print ('       Up      ')
    print ('Left       Right')
    print ('      Down     ')
    print ('                    Exit')
    choice = raw_input('Type direction or exit to leave game \n')
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

