from Classes import *
from Subclasses import *
from Monster import *
from BattleFunctions import *
from Recovery import *
from random import random, randint
from GUI import *

stats = {
    'Warrior': {'Bruiser': Bruiser, 'Paladin': Paladin},
    'Mage': {'Wizard': Wizard, 'Hemomancer': Hemomancer},
    'Assassin': {'Ninja': Ninja, 'Rogue': Rogue},
    'Marksman': {'Sniper': Sniper, 'Archer': Archer},
    'Tank': {'Vanguard': Vanguard, 'Warden': Warden}
}
items = ["Mango", "Chenette", "Doubles"]


def createCharacter():
    layout = [[Text("Enter your character's name")],
              [InputText()],
              [Text("Please choose a class")],
              [InputCombo(['Mage', 'Assassin', 'Warrior', 'Tank', "Marksman"])],
              [OK()]]

    event, values = Window("SimplePythonRPG", auto_size_text=True, default_element_size=(40, 1)).Layout(layout).Read()
    name = values[0]
    rClass = values[1]

    subclass_choice = list(stats[rClass].keys())
    layout = [[Text("Select a subclass from " + subclass_choice[0] + " or " + subclass_choice[1])],
              [InputCombo([subclass_choice[0], subclass_choice[1]])],
              [OK()]]
    event, values = Window("SimplePythonRPG", auto_size_text=True, default_element_size=(40, 1)).Layout(
        layout).Read()
    subclass = values[0]

    return stats[rClass][subclass](name)


def sits(num, char):
    if num == 1:
        Popup('You come face to face with an enemy.')
        battle(char, False)
    elif num == 2:
        emptyRoom(char)
    elif num == 3:
        getItem(char)


def getSit(sit):
    if sit <= 0.4:
        num = 1
    elif 0.4 < sit <= 0.75:
        num = 2
    elif 0.75 < sit <= 1.0:
        num = 3
    return num


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
        '''
        print('                             ' + enemy.Name + ": Lv " + str(enemy.Level))
        print('                             HP: ' + str(enemy.currHp) + '/' + str(enemy.Hp))
        print(char.Name + ": Lv " + str(char.Level))
        print("HP:   " + str(char.currHp) + '/' + str(char.Hp))
        print("Mana: " + str(char.currMana) + '/' + str(char.mana))
        print('Attack      Item        Scan')
        choice = input('Stats       Special     Run\n')
        choice = choice.lower()
        '''
        choice = HPbars(enemy,char)
        if choice == 'Attack':
            crit, dodge, damage = char.Attack(enemy.Def)
            enCrit, enDodge, enAttack = enemy.Attack(char.Def)
            if turnOrder(char.Spd, enemy.Spd) == 1:
                if damage > 0:
                    if crit == 1:
                        Popup("SMASH! You did " + str(damage) + " critical damage!")
                    else:
                        Popup('You did ' + str(damage) + " damage!")
                    enemy.takeDamage(damage)
                else:
                    if dodge == 1:
                        Popup("Ooof, the monster dodged your attack")
                    else:
                        Popup('Your attack missed!')

                if not enemy.isAlive():
                    if not boss:
                        Popup('You won the battle!')
                    else:
                        Popup('You beat the boss!', 'You Obtained an item!')
                        char.inventory.append(items[randint(0, len(items) - 1)])
                    char.addExp(enemy.Level, boss)
                    return

                if enAttack > 0:
                    if enCrit == 1:
                        Popup("CRAP! Monster did " + str(enAttack) + " critical damage!")
                    else:
                        Popup('Monster did ' + str(enAttack) + " damage!")
                    char.takeDamage(enAttack)
                else:
                    if enDodge == 1:
                        Popup("Nice! you dodged the attack")
                    else:
                        Popup("Monster's attack missed!")

                if not char.isAlive():
                    Popup('You Died...')
                    return
            else:
                if enAttack > 0:
                    if enCrit == 1:
                        Popup("CRAP! Monster did " + str(enAttack) + " critical damage!")
                    else:
                        Popup('Monster did ' + str(enAttack) + " damage!")
                    char.takeDamage(enAttack)
                else:
                    if enDodge == 1:
                        Popup("Nice! you dodged the attack")
                    else:
                        Popup("Monster's attack missed!")

                if not char.isAlive():
                    Popup('You Died...')
                    return

                if damage > 0:
                    if crit == 1:
                        Popup("SMASH! You did " + str(damage) + " critical damage!")
                    else:
                        Popup('You did ' + str(damage) + " damage!")
                    enemy.takeDamage(damage)
                else:
                    if dodge == 1:
                        Popup("Ooof, the monster dodged your attack")
                    else:
                        Popup('Your attack missed!')

                if not enemy.isAlive():
                    if not boss:
                        Popup('You won the battle!')
                    else:
                        Popup('You beat the boss!', 'You Obtained an item!')
                        char.inventory.append(items[randint(0, len(items) - 1)])
                    char.addExp(enemy.Level, boss)
                    return

        elif choice == 'Run':
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
                Popup(char.Name + " Ran Away!")
                return
            else:
                Popup(char.Name + " Tripped and couldn't run!")
                run_attempt += 1
                enCrit, enDodge, enAttack = enemy.Attack(char.Def)
                if enAttack > 0:
                    if enCrit == 1:
                        Popup("CRAP! Monster did " + str(enAttack) + " critical damage!")
                    else:
                        Popup('Monster did ' + str(enAttack) + " damage!")
                    char.takeDamage(enAttack)
                else:
                    if enDodge == 1:
                        Popup("Nice! you dodged the attack")
                    else:
                        Popup("Monster's attack missed!")

                if not char.isAlive():
                    Popup('You Died...')

        elif choice == 'Item':
            if len(char.inventory) == 0:
                Popup("You have no items")
            else:
                item = listItems(char.inventory)
                if item in char.inventory:
                    char.inventory.remove(item)
                    if item == 'Mango':
                        char.currHp = healing(char.currHp, char.Hp)
                    elif item == 'Chenette':
                        char.currMana = manaRestore(char.currMana, char.mana)
                    elif item == 'Doubles':
                        add = randint(3, 5)
                        ad_buff += add
                        Popup("You ate a doubles\nAttack Raised by", add)

        elif choice == 'Stats':
            Popup('Attack: ' + str(char.Atk + ad_buff) + "(+" + str(ad_buff) + ")",
                  'Defense: ' + str(char.Def + df_buff) + "(+" + str(df_buff) + ")",
                  'Speed: ' + str(char.Spd + sp_buff) + "(+" + str(sp_buff) + ")")

        elif choice == 'Scan':
            if scanned > 0:
                stat = randint(1, 10)
                if stat <= 4:
                    Popup("Monster's Attack: " + str(enemy.Atk))
                if 4 < stat <= 8:
                    Popup("Monster's Defense: " + str(enemy.Def))
                if stat > 8:
                    Popup("Monster's Speed: " + str(enemy.Spd))
                scanned -= 1
                Popup("You can scan " + str(scanned) + " more times")
            else:
                Popup("You have already scanned this enemy!")

        elif choice == 'Special':
            enCrit, enDodge, enAttack = enemy.Attack(char.Def)
            if turnOrder(char.Spd, enemy.Spd) == 1:
                stat, amt = char.specialAttack(enemy)
                if stat == 'Atk':
                    ad_buff += amt
                elif stat == 'Def':
                    df_buff += amt
                else:
                    sp_buff += amt

                if not enemy.isAlive():
                    if not boss:
                        Popup('You won the battle!')
                    else:
                        Popup('You beat the boss!')
                        Popup('You Obtained an item!')
                        char.inventory.append(items[randint(0, len(items) - 1)])
                    char.addExp(enemy.Level, boss)
                    return

                if enAttack > 0:
                    if enCrit == 1:
                        Popup("CRAP! Monster did " + str(enAttack) + " critical damage!")
                    else:
                        Popup('Monster did ' + str(enAttack) + " damage!")
                    char.takeDamage(enAttack)
                else:
                    if enDodge == 1:
                        Popup("Nice! you dodged the attack")
                    else:
                        Popup("Monster's attack missed!")

                if not char.isAlive():
                    Popup('You Died...')
                    return

            else:

                if enAttack > 0:
                    if enCrit == 1:
                        Popup("CRAP! Monster did " + str(enAttack) + " critical damage!")
                    else:
                        Popup('Monster did ' + str(enAttack) + " damage!")
                    char.takeDamage(enAttack)
                else:
                    if enDodge == 1:
                        Popup("Nice! you dodged the attack")
                    else:
                        Popup("Monster's attack missed!")

                if not char.isAlive():
                    Popup('You Died...')
                    return

                stat, amt = char.specialAttack(enemy)
                if stat == 'Atk':
                    ad_buff += amt
                elif stat == 'Def':
                    df_buff += amt
                else:
                    sp_buff += amt

                if not enemy.isAlive():
                    if not boss:
                        Popup('You won the battle!')
                    else:
                        Popup('You beat the boss!')
                        Popup('You Obtained an item!')
                        char.inventory.append(items[randint(0, len(items) - 1)])
                    char.addExp(enemy.Level, boss)
                    return

        else:
            Popup("Not a valid choice")


def emptyRoom(char):
    layout = [[Text("It's an empty room...")],
              [OK()]]
    event, values = Window("SimplePythonRPG").Layout(layout).Read()
    rand = random()
    if rand <= 0.40:
        layout = [[Text("You turn to leave and an enemy attacks you!")],
                  [OK()]]
        event, values = Window("SimplePythonRPG").Layout(layout).Read()
        battle(char, False)
    if 0.40 < rand < 0.50:
        layout = [[Text("The boss comes out of the shadows! You have to fight!")],
                  [OK()]]
        event, values = Window("SimplePythonRPG").Layout(layout).Read()
        battle(char, True)


def getItem(char):
    layout = [[Text("You enter a room, there's a chest!")],
              [Text("Will you open it?")],
              [Yes(), No()]]
    choice, values = Window("SimplePythonRPG").Layout(layout).Read()
    if choice == 'No':
        Popup("You walked out. You don't trust what the chest might contain")
        #return
    elif choice == 'Yes':
        encounter = random()
        if encounter <= 0.4:
            Popup("You encounter an enemy!")
            return battle(char, False)
        else:
            Popup('You Obtained an item!')
            char.inventory.append(items[randint(0, len(items) - 1)])
