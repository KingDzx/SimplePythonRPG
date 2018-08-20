from random import random,randint
import os
from math import *
''' Stats are HP, Attack, Defense, Speed'''
''' All Characters have a MAX power budget of 85 (Max values of each stat in total must not cross 85)'''
stats = {
    'Warrior':{'HP':randint(25,35),'Atk':randint(19,21),'Def':randint(20,22),'Spd':randint(1,7),'Mana':30,'Subclass':{'Brusier':False , 'Paladin':False}}, # +Atk +Def -HP
    'Mage':{'HP':randint(15,20),'Atk':randint(28,30),'Def':randint(17,22),'Spd':randint(5,13),'Mana':30,'Subclass':{'Wizard':False , 'Hemomancer':False}}, # +Atk +Mana -Spd
    'Assassin':{'HP':randint(15,20),'Atk':randint(32,34),'Def':randint(9,14),'Spd':randint(15,17),'Mana':30,'Subclass':{'Ninja':False , 'Rogue':False}}, # +Atk +Spd -HP
    'Marksman':{'HP':randint(20,25),'Atk':randint(14,19),'Def':randint(11,19),'Spd':randint(20,22),'Mana':30,'Subclass':{'Sniper':False , 'Archer':False}}, # +Spd -Def
    'Tank':{'HP':randint(35,40),'Atk':randint(1,8),'Def':randint(29,31),'Spd':randint(1,6),'Mana':30,'Subclass':{'Vanguard':False , 'Warden':False}} # +Def +HP -Atk
}
items = ["Mango","Chenette","Doubles"]
def createCharacter():  
    name = input("Enter Character Name \n")
    rpgClass = input("Enter Wanted Class (Warrior/Mage/Assassin/Marksman/Tank) \n")
    rpgClass = rpgClass.capitalize()
    level = 5
    inventory = []
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
    stats[rpgClass]['Subclass'][subclass] = True
    player = {name:[stats[rpgClass],level,inventory]}
    return player,rpgClass,name

def battle(num,player,pClass,subclass,name,exp,hp,mana,boss):
    enemyAlive = True
    Alive = True
    scanned = False
    enemyLevel = randint((player[name][1]-2),(player[name][1]+2))
    if enemyLevel < 1:
        enemyLevel = 1
    if enemyLevel > 100:
        enemyLevel = 100
    if boss == False:
        enemy = {'Monster':[round((randint(5,10) + round(randint(1,2) * (random()*3) * enemyLevel))) , round((randint(7,11) + round(randint(1,2) * (random()*2.5) * enemyLevel))), round((randint(7,11) + round(randint(1,2) * (random()*2.5) * enemyLevel))), round((randint(7,11) + round(randint(1,2) * (random()*2.5) * enemyLevel)))]}
    else:
        enemy = {'Monster':[round((randint(15,20) + round(randint(3,4) * (random()*2.75) * enemyLevel))) , round((randint(10,15) + round(randint(3,4) * (random()*2.25) * enemyLevel))), round((randint(10,15) + round(randint(3,4) * (random()*2.25) * enemyLevel))), round((randint(10,15) + round(randint(3,4) * (random()*2.25) * enemyLevel)))]}
    enemyHp = enemy['Monster'][0]
    runAttempt = 1
    while enemyAlive == True and Alive == True:
        #print ('                             ' + str(enemy['Monster']))
        if boss == False:
            print ('                             Monster: Lv ' + str(enemyLevel))
        else:
            print ('                             Boss: Lv ' + str(enemyLevel))
        print ('                             HP: ' + str(enemyHp) + '/' + str(enemy['Monster'][0]))
        print (name + " The " + subclass + ": Lv " + str(player[name][1]))
        print ("HP:   " + str(hp) + '/' + str(player[name][0]['HP']))
        print ("Mana: " + str(mana) + '/' + str(player[name][0]['Mana']))
        print ('Attack      Item        Scan')
        choice = input('Stats       Special     Run\n')
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
                    if boss == False:
                        print ('You won the battle!')
                    elif boss == True:
                        print ('You beat the boss!')
                        print ('You Obtained an item!')
                        player[name][2].append(items[randint(0,2)])
                    return levelUp(exp,player,pClass,hp,mana,enemyLevel,boss)
                
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
                    return exp,hp,mana
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
                    return exp,hp,mana
                
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
                    if boss == False:
                        print ('You won the battle!')
                    elif boss == True:
                        print ('You beat the boss!')
                        print ('You Obtained an item!')
                        player[name][2].append(items[randint(0,2)])
                    return levelUp(exp,player,pClass,hp,mana,enemyLevel,boss)
                
        elif choice == 'run':
            if boss == True:
                print ("You cannot run from the boss!")
            else:
                num1 = enemy['Monster'][3]/4
                if num1 < 1:
                    num1 = 1
                chance = (((player[name][0]['Spd'] * 32)/ num1) + 30) * runAttempt / 256
                willIRun = randint(0,255)
                if chance < willIRun:
                    print (name + " Ran Away!")
                    return exp,hp,mana
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
                        return exp,hp,mana
                    
        elif choice == 'item':
            if len(player[name][2]) == 0:
                print ("You have no items")
            else:
                print (player[name][2])
                item = input ("Type which item you wish to use or type Back to go back\n")
                item = item.capitalize()
                while (item not in player[name][2] and item != 'Back'):
                    print ("This is not an item in your bag, try again")
                    item = input ("Type which item you wish to use\n")
                    item = item.capitalize()
                if (item in player[name][2]):
                    player[name][2].remove(item)
                    if item == 'Mango':
                        hp = healing(hp)
                    if item == 'Chenette':
                        mana = manaRestore(mana)
                if (item == 'Back'):
                    print ("")
                
        elif choice == 'stats':
            stats = player[name][0]
            print ('Attack: ' + str(stats['Atk']))
            print ('Defense: ' + str(stats['Def']))
            print ('Speed: ' + str(stats['Spd']))
            
        elif choice == 'scan':
            if scanned == False:
                stat = randint(1,10)
                if stat <= 4:
                    print ("Monster's Attack:",enemy['Monster'][1])
                if stat > 4 and stat <= 8:
                    print ("Monster's Defense:",enemy['Monster'][2])
                if stat > 8:
                    print ("Monster's Speed:",enemy['Monster'][3])
                scanned = True
            else:
                print ("You have already scanned this enemy!")

        elif choice == 'special':
            enCrit,enDodge,enAttack = calDamage(enemy['Monster'][1],player[name][0]['Def'],enemyLevel)
            if turnOrder(player[name][0]['Spd'],enemy['Monster'][3]) == 1:                
                exp,hp,mana,enemyHp,enemyAlive = specialAttack(player,subclass,name,exp,hp,mana,enemy,enemyHp,boss,enemyLevel)
                if enemyAlive == False:         
                    return exp,hp,mana
                
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
                    return exp,hp,mana
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
                    return exp,hp,mana

                exp,hp,mana,enemyHp,enemyAlive = specialAttack(player,subclass,name,exp,hp,mana,enemy,enemyHp,boss,enemyLevel)
                if enemyAlive == False:
                    return exp,hp,mana
        else:
            print ("Not a valid choice")
        os.system('pause')
        os.system('CLS')

def specialAttack(player,subclass,name,exp,hp,mana,enemy,enemyHp,boss,enemyLevel):
    alive = True
    if subclass == 'Brusier':
        print("Coming Soon™!")
        
    elif subclass == 'Paladin':
        if mana >= 25:
            mana = mana - 25
            hp = hp + round(player[name][0]['HP'] * 0.75)
            print ("You blessed yourself with a holy light!")
            print ("You healed " + str(round(player[name][0]['HP'] * 0.75)) + " HP")
            if hp > player[name][0]['HP']:
                hp = player[name][0]['HP']
        else:
            print ("Not Enough Mana!")
            
    elif subclass == 'Wizard':
        print("Coming Soon™!")
        
    elif subclass == 'Hemomancer':
        if mana >= 20:
            mana = mana - 20
            print ("You use your magic to manipulate the enemy's blood!")
            damage = round(((((2 * player[name][1] / 5 + 2) * player[name][0]['Atk'] * randint(30,100) / enemy['Monster'][2]) / 50) + 2) * randint(1,100) / 100)
            hp = hp + round(damage * 0.67)
            if hp > player[name][0]['HP']:
                hp = player[name][0]['HP']
            enemyHp -= damage
            if damage == 0:
                print ("You tried to cast your magic but it failed!")
                mana = mana + 10
            else:
                print ("You dealt " + str(damage) + " damage and healed for two thirds of that")
            if enemyHp < 0:
                if boss == False:
                    print ('You won the battle!')
                elif boss == True:
                    print ('You beat the boss!')
                    print ('You Obtained an item!')
                    player[name][2].append(items[randint(0,2)])
                exp,hp,mana = levelUp(exp,player,pClass,hp,mana,enemyLevel,boss)
                alive = False
        else:
            print ("Not Enough Mana!")
            
    elif subclass == "Ninja":
        print("Coming Soon™!")
        
    elif subclass == "Rogue":
        print("Coming Soon™!")
        
    elif subclass == "Sniper":
        print("Coming Soon™!")
        
    elif subclass == "Archer":
        print("Coming Soon™!")
        
    elif subclass == "Vanguard":
        print("Coming Soon™!")
        
    elif subclass == "Warden":
        print("Coming Soon™!")
        
    return exp,hp,mana,enemyHp,alive
            
def levelUp(exp,player,Class,HP,mana,enemyLevel,boss):
    nextLevel = player[name][1]+1
    A = (enemyLevel * 2) + 10
    C = (enemyLevel + player[name][1] + 10)
    if boss == False:
        B = (randint(35,75) * enemyLevel) /5
    else:
        B = (randint(150,250) * enemyLevel) /5 * 1.5
    gain = floor(floor(sqrt(A) * (A*A)) * B / floor(sqrt(C) * (C*C)))+1
    exp = exp + gain 
    lvlup = floor(1.2 * nextLevel ** 3 - 15 * nextLevel ** 2 + 100 * nextLevel - 140) #(player[name][1]+1)**3
    print ('You gained ' + str(gain) + ' exp')
    while exp > lvlup:
        if player[name][1] == 100:
            break
        if player[name][1] < 100:                                   
            if exp > lvlup:
                print ('You gained a level!')
                hpGain = randint(2,7)
                if Class == 'Warrior' or Class == 'Assassin':
                    hpGain = int(floor(hpGain * 0.5))
                elif Class == 'Tank':
                    hpGain = randint(7,10)
                    
                atkGain = randint(1,4)
                if Class == 'Mage':
                    atkGain = int(floor(atkGain * 1.5))
                elif Class == 'Assassin' or Class == "Warrior":
                    atkGain = randint(3,5)
                elif Class == 'Tank':
                    atkGain = int(floor(atkGain * 0.5))
                    
                defGain = randint(1,4)
                if Class == 'Tank' or Class == 'Warrior':
                    defGain = randint(3,5)
                elif Class == 'Marksman':
                    defGain = int(floor(defGain * 0.5))
                    
                spdGain = randint(1,4)
                if Class == 'Marksman':
                    spdGain = int(floor(spdGain * 1.5))
                if Class == 'Assassin':
                    spdGain = randint(3,5)
                elif Class == 'Mage':
                    spdGain = int(floor(spdGain * 0.5))

                manaGain = randint(5,10)
                if Class == 'Mage':
                    manaGain = int(floor(manaGain * 1.5))
                
                print ('HP: ' + str(player[name][0]['HP']) + ' -> ' + str(player[name][0]['HP'] + hpGain) + ' +' + str(hpGain))
                print ('Attack: ' + str(player[name][0]['Atk']) + ' -> ' + str(player[name][0]['Atk'] + atkGain) + ' +' + str(atkGain))
                print ('Defense: ' + str(player[name][0]['Def']) + ' -> ' + str(player[name][0]['Def'] + defGain) + ' +' + str(defGain))
                print ('Speed: ' + str(player[name][0]['Spd']) + ' -> ' + str(player[name][0]['Spd'] + spdGain) + ' +' + str(spdGain))
                print ('Mana: ' + str(player[name][0]['Mana']) + ' -> ' + str(player[name][0]['Mana'] + manaGain) + ' +' + str(manaGain))
                print ('\n')
                player[name][1] = player[name][1] + 1
                player[name][0]['HP'] = player[name][0]['HP'] + hpGain
                player[name][0]['Atk'] = player[name][0]['Atk'] + atkGain
                player[name][0]['Def'] = player[name][0]['Def'] + defGain
                player[name][0]['Spd'] = player[name][0]['Spd'] + spdGain
                player[name][0]['Mana'] = player[name][0]['Mana'] + manaGain
                nextLevel = player[name][1]+1
                lvlup = floor(1.2 * nextLevel ** 3 - 15 * nextLevel ** 2 + 100 * nextLevel - 140)
                HP = HP + hpGain
                mana = mana + manaGain
    return exp,HP,mana

def situations(num,player,pClass,subclass,name,exp,hp,mana):
    if num == 1:
        print ('You come face to face with an enemy. What will you do? (Type to choose choice)')
        return battle(num,player,pClass,subclass,name,exp,hp,mana,False)
        
    elif num == 2:
        print ("It's an empty room...")
        rand = random()
        if rand <= 0.45:
            os.system('pause')
            print ("You turn to leave and an enemy attacks you!")
            return battle(num,player,pClass,subclass,name,exp,hp,mana,False)
        if rand >0.45 and rand < 0.50:
            os.system('pause')
            print ("The boss comes out of the shadows! You have to fight!")
            return battle(num,player,pClass,subclass,name,exp,hp,mana,True)
        else:
            return exp,hp,mana

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
            encounter = random()
            if encounter <= 0.4:
                print ("You encounter an enemy!")
                return battle(num,player,pClass,subclass,name,exp,hp,mana,False)
            else:
                print ('You Obtained an item!')
                player[name][2].append(items[randint(0,2)])
                return exp,hp,mana

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
    damage = round(((((2 * level / 5 + 2) * attack * randint(30,100) / defense) / 50) + 2) * randint(1,100) / 100)
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
        print ("You ate a Super Julie Starch Mango! HP fully restored!")
        hp = player[name][0]['HP']
    elif rand > 0.10 and rand <= 0.30:
        print ("You ate a Julie Starch Mango! Gained", round(player[name][0]['HP'] * 0.75), "HP!")
        hp += round(player[name][0]['HP'] * 0.75)
    elif rand > 0.30 and rand <= 0.65:
        print ("You ate a Julie Mango! Gained", round(player[name][0]['HP'] * 0.50), "HP!")
        hp += round(player[name][0]['HP'] * 0.50)
    elif rand > 0.65:
        print ("You ate a Starch Mango! Gained", round(player[name][0]['HP'] * 0.25), "HP!")
        hp += round(player[name][0]['HP'] * 0.25)

    if hp > player[name][0]['HP']:
        hp = player[name][0]['HP']
    return hp

def manaRestore(mana):
    rand = random()
    if rand <= 0.1:
        print ("You ate a Big Sweet Chenette! Mana fully restored!")
        mana = player[name][0]['Mana']
    elif rand > 0.10 and rand <= 0.30:
        print ("You ate a Sweet Chenette! Gained", round(player[name][0]['Mana'] * 0.75), "Mana!")
        mana += round(player[name][0]['Mana'] * 0.75)
    elif rand > 0.30 and rand <= 0.65:
        print ("You ate a Chenette! Gained", round(player[name][0]['Mana'] * 0.50), "Mana!")
        mana += round(player[name][0]['Mana'] * 0.50)
    elif rand > 0.65:
        print ("You ate an Ok Chenette! Gained", round(player[name][0]['Mana'] * 0.25), "Mana!")
        mana += round(player[name][0]['Mana'] * 0.25)

    if mana > player[name][0]['Mana']:
        mana = player[name][0]['Mana']
    return mana
player,pClass,name = createCharacter()
exp=player[name][1]**3
subclass = list(player[name][0]["Subclass"].keys())
if player[name][0]["Subclass"][subclass[0]] == True:
    subclass = subclass[0]
else:
    subclass = subclass[1]
leave = False
hp = player[name][0]['HP']
mana = player[name][0]['Mana']
print ("Your Stats are:")
print ('HP: ' + str(player[name][0]['HP']))
print ('Attack: ' + str(player[name][0]['Atk']))
print ('Defense: ' + str(player[name][0]['Def']))
print ('Speed: ' + str(player[name][0]['Spd']))
print ('Mana: ' + str(player[name][0]['Mana']))
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
        if sit <= 0.4:
            num = 1
        elif sit > 0.4 and sit <= 0.70:
            num = 2
        elif sit > 0.70 and sit <= 1.0:
            num = 3
        new = situations(num,player,pClass,subclass,name,exp,hp,mana)
        exp = new[0]
        hp = new[1]
        mana = new[2]
    else:
        print ("Not a choice, please enter a valid choice")
    os.system('pause')
    os.system('CLS')
    
print ("Thanks for playing!")
print ("You got to level " + str(player[name][1]))
os.system('pause')
