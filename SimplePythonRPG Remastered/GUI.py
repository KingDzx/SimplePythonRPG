from PySimpleGUI import *

ChangeLookAndFeel('GreenMono')


def initialScreen(hp, Atk, Def, Spd, mana):
    layout = [[Text("Stats", font=("Arial", 30, 'underline'), text_color='green')],
              [Text("HP:"), Text(hp)],
              [Text("Attack:"), Text(Atk)],
              [Text("Defense:"), Text(Def)],
              [Text("Speed:"), Text(Spd)],
              [Text("Mana:"), Text(mana)],
              [OK()]]

    event, values = Window("SimplePythonRPG", auto_size_text=True, default_element_size=(40, 1)).Layout(layout).Read()


def walking():
    layout = [[Text('Pick a direction to go')],
              [T(' ' * 11), Button('Up', default_value='Up')],
              [Button('Left', default_value='Left'), T(' ' * 15),
               Button('Right', default_value='Right')],
              [T(' ' * 9), Button('Down', default_value='Down')],
              [Quit(button_color=('white', 'orange'))]]

    event, values = Window("SimplePythonRPG", auto_size_text=True, default_element_size=(40, 1)).Layout(layout).Read()
    return event


def HPbars(enemy, char):
    layout = [[T(' ' * 30), Text(enemy.Name + ": Lv " + str(enemy.Level))],
              [T(' ' * 30), Text('HP: ' + str(enemy.currHp) + '/' + str(enemy.Hp))],
              [Text(char.Name + ": Lv " + str(char.Level))],
              [Text("HP:   " + str(char.currHp) + '/' + str(char.Hp))],
              [Text("Mana: " + str(char.currMana) + '/' + str(char.mana))],
              [Button('Attack'), Button('Item'), Button('Scan')],
              [Button('Stats'), Button('Special'), Button('Run')]]

    event, values = Window("SimplePythonRPG", auto_size_text=True, default_element_size=(40, 1)).Layout(layout).Read()
    return event


def listItems(inven):
    stuff = list(set(inven))
    layout = [[Text("Select the Item you wish to use")],
              [Listbox(values=stuff, size=(20, 5))],
              [OK(), Button('Back', default_value='Back')]]
    event, values = Window("SimplePythonRPG", auto_size_text=True, default_element_size=(40, 1)).Layout(layout).Read()
    if event == 'Back':
        return event
    return values[0][0]

