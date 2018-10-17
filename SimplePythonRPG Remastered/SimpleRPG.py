from Classes import *
from Subclasses import *
from Monster import *
from BattleFunctions import *
from Recovery import *
from random import random, randint
import os

stats = {
    'Warrior':{'Bruiser': Bruiser, 'Paladin': Paladin},
    'Mage': {'Wizard': Wizard, 'Hemomancer': Hemomancer},
    'Assassin': {'Ninja': Ninja, 'Rogue': Rogue},
    'Marksman': {'Sniper': Sniper, 'Archer': Archer},
    'Tank': {'Vanguard': Vanguard, 'Warden': Warden}
}
items = ["Mango", "Chenette", "Doubles"]


def createCharacter():
    name = input("Enter Character Name \n")
    rpg_class = input("Enter Wanted Class (Warrior/Mage/Assassin/Marksman/Tank) \n")
    rpg_class = rpg_class.capitalize()
    while rpg_class != "Warrior" and rpg_class != "Mage" and rpg_class != "Assassin" and rpg_class != "Marksman" and rpg_class != "Tank":
        print('Please choose a valid class')
        rpg_class = input("Enter Wanted Class (Warrior/Mage/Assassin/Marksman/Tank) \n")
        rpg_class = rpg_class.capitalize()
    subclass_choice = list(stats[rpg_class].keys())
    subclass = input("Select a subclass from " + subclass_choice[0] + " or " + subclass_choice[1] + "\n")
    subclass = subclass.capitalize()
    while subclass not in subclass_choice:
        print('Please choose a subclass from the list provided')
        subclass = input("Select a subclass from " + subclass_choice[0] + " or " + subclass_choice[1] + "\n")
        subclass = subclass.capitalize()

    return stats[rpg_class][subclass](name)


def sits(num, char):
    if num == 1:
        print('You come face to face with an enemy. What will you do? (Type to choose choice)')
        battle(char, False)
    elif num == 2:
        emptyRoom(char)
    elif num == 3:
        getItem(char)


def battle(char, boss):
    ad_buff = 0
    df_buff = 0
    sp_buff = 0
    if boss:
        enemy = Boss(char.Level)
    else:
        enemy = Monster(char.Level)
    run_attempt = 1
    scanned = 2
    while enemy.isAlive() and char.isAlive():
        print('                             ' + enemy.Name + ": Lv " + str(enemy.Level))
        print('                             HP: ' + str(enemy.currHp) + '/' + str(enemy.Hp))
        print(char.Name + ": Lv " + str(char.Level))
        print("HP:   " + str(char.currHp) + '/' + str(char.Hp))
        print("Mana: " + str(char.currMana) + '/' + str(char.mana))
        print('Attack      Item        Scan')
        choice = input('Stats       Special     Run\n')
        choice = choice.lower()
        if choice == 'attack':
            crit, dodge, damage = char.Attack(enemy.Def)
            enCrit, enDodge, enAttack = enemy.Attack(char.Def)
            if turnOrder(char.Spd, enemy.Spd) == 1:
                if damage > 0:
                    if crit == 1:
                        print("SMASH! You did " + str(damage) + " critical damage!")
                    else:
                        print('You did ' + str(damage) + " damage!")
                    enemy.takeDamage(damage)
                else:
                    if dodge == 1:
                        print("Ooof, the monster dodged your attack")
                    else:
                        print('Your attack missed!')

                if not enemy.isAlive():
                    if not boss:
                        print('You won the battle!')
                    else:
                        print('You beat the boss!')
                        print('You Obtained an item!')
                        char.inventory.append(items[randint(0, 2)])
                    char.addExp(enemy.Level, boss)
                    return

                if enAttack > 0:
                    if enCrit == 1:
                        print("CRAP! Monster did " + str(enAttack) + " critical damage!")
                    else:
                        print('Monster did ' + str(enAttack) + " damage!")
                    char.takeDamage(enAttack)
                else:
                    if enDodge == 1:
                        print("Nice! you dodged the attack")
                    else:
                        print("Monster's attack missed!")

                if not char.isAlive():
                    print('You Died...')
                    return
            else:
                if enAttack > 0:
                    if enCrit == 1:
                        print("CRAP! Monster did " + str(enAttack) + " critical damage!")
                    else:
                        print('Monster did ' + str(enAttack) + " damage!")
                    char.takeDamage(enAttack)
                else:
                    if enDodge == 1:
                        print("Nice! you dodged the attack")
                    else:
                        print("Monster's attack missed!")

                if not char.isAlive():
                    print('You Died...')
                    return

                if damage > 0:
                    if crit == 1:
                        print("SMASH! You did " + str(damage) + " critical damage!")
                    else:
                        print('You did ' + str(damage) + " damage!")
                    enemy.takeDamage(damage)
                else:
                    if dodge == 1:
                        print("Ooof, the monster dodged your attack")
                    else:
                        print('Your attack missed!')

                if not enemy.isAlive():
                    if not boss:
                        print('You won the battle!')
                    else:
                        print('You beat the boss!')
                        print('You Obtained an item!')
                        char.inventory.append(items[randint(0, 2)])
                    char.addExp(enemy.Level, boss)
                    return

        elif choice == 'run':
            '''
            # if boss == True:
            # print ("You cannot run from the boss!")
            # else:
            '''
            num1 = enemy.Spd / 4
            if num1 < 1:
                num1 = 1
            chance = (((char.Spd * 32) / num1) + 30) * run_attempt / 256
            will_i_run = randint(0, 255)
            if chance < will_i_run:
                print(char.Name + " Ran Away!")
                return
            else:
                print(char.Name + " Tripped and couldn't run!")
                run_attempt += 1
                enCrit, enDodge, enAttack = enemy.Attack(char.Def)
                if enAttack > 0:
                    if enCrit == 1:
                        print("CRAP! Monster did " + str(enAttack) + " critical damage!")
                    else:
                        print('Monster did ' + str(enAttack) + " damage!")
                    char.takeDamage(enAttack)
                else:
                    if enDodge == 1:
                        print("Nice! you dodged the attack")
                    else:
                        print("Monster's attack missed!")

                if not char.isAlive():
                    print('You Died...')

        elif choice == 'item':
            if len(char.inventory) == 0:
                print("You have no items")
            else:
                print(char.inventory)
                item = input("Type which item you wish to use or type Back to go back\n")
                item = item.capitalize()
                while item not in char.inventory and item != 'Back':
                    print("This is not an item in your bag, try again")
                    item = input("Type which item you wish to use\n")
                    item = item.capitalize()
                if item in char.inventory:
                    char.inventory.remove(item)
                    if item == 'Mango':
                        char.currHp = healing(char.currHp, char.Hp)
                    elif item == 'Chenette':
                        char.currMana = manaRestore(char.currMana, char.mana)
                    elif item == 'Doubles':
                        add = randint(3, 5)
                        ad_buff += add
                        print("You ate a doubles\nAttack Raised by", add)
                if item == 'Back':
                    print("")

        elif choice == 'stats':
            print('Attack: ' + str(char.Atk + ad_buff) + "(" + str(ad_buff) + ")")
            print('Defense: ' + str(char.Def + df_buff) + "(" + str(df_buff) + ")")
            print('Speed: ' + str(char.Spd + sp_buff) + "(" + str(sp_buff) + ")")

        elif choice == 'scan':
            if scanned > 0:
                stat = randint(1, 10)
                if stat <= 4:
                    print("Monster's Attack:", enemy.Atk)
                if 4 < stat <= 8:
                    print("Monster's Defense:", enemy.Def)
                if stat > 8:
                    print("Monster's Speed:", enemy.spd)
                scanned -= 1
            else:
                print("You have already scanned this enemy!")

        elif choice == 'special':
            enCrit, enDodge, enAttack = enemy.Attack(char.Def)
            if turnOrder(char.Spd, enemy.Spd) == 1:
                char.specialAttack(enemy)

                if not enemy.isAlive():
                    if not boss:
                        print('You won the battle!')
                    else:
                        print('You beat the boss!')
                        print('You Obtained an item!')
                        char.inventory.append(items[randint(0, 2)])
                    char.addExp(enemy.Level, boss)
                    return

                if enAttack > 0:
                    if enCrit == 1:
                        print("CRAP! Monster did " + str(enAttack) + " critical damage!")
                    else:
                        print('Monster did ' + str(enAttack) + " damage!")
                    char.takeDamage(enAttack)
                else:
                    if enDodge == 1:
                        print("Nice! you dodged the attack")
                    else:
                        print("Monster's attack missed!")

                if not char.isAlive():
                    print('You Died...')
                    return

            else:

                if enAttack > 0:
                    if enCrit == 1:
                        print("CRAP! Monster did " + str(enAttack) + " critical damage!")
                    else:
                        print('Monster did ' + str(enAttack) + " damage!")
                    char.takeDamage(enAttack)
                else:
                    if enDodge == 1:
                        print("Nice! you dodged the attack")
                    else:
                        print("Monster's attack missed!")

                if not char.isAlive():
                    print('You Died...')
                    return

                char.specialAttack(enemy)

                if not enemy.isAlive():
                    if not boss:
                        print('You won the battle!')
                    else:
                        print('You beat the boss!')
                        print('You Obtained an item!')
                        char.inventory.append(items[randint(0, 2)])
                    char.addExp(enemy.Level, boss)
                    return

        else:
            print("Not a valid choice")
        os.system('pause')
        os.system('CLS')


def emptyRoom(char):
    print("It's an empty room...")
    rand = random()
    if rand <= 0.40:
        os.system('pause')
        print("You turn to leave and an enemy attacks you!")
        battle(char, False)
    if 0.40 < rand < 0.50:
        os.system('pause')
        print("The boss comes out of the shadows! You have to fight!")
        battle(char, True)


def getItem(char):
    print("You enter a room, there's a chest!")
    choice = input("Do you want to open it? (Yes/No)")
    choice = choice.lower()
    os.system('CLS')
    while choice != 'yes' and choice != 'no':
        choice = input("You must choose to open it or not! (Yes/No)")
        choice = choice.lower()
    if choice == 'no':
        print("You walked out. You don't trust what the chest might contain")
        return
    elif choice == 'yes':
        encounter = random()
        if encounter <= 0.4:
            print("You encounter an enemy!")
            return battle(char, False)
        else:
            print('You Obtained an item!')
            char.inventory.append(items[randint(0, 2)])
