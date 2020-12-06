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

    window = Window("SimplePythonRPG", auto_size_text=True, default_element_size=(40, 1)).Layout(layout)

    event, values = window.Read()
    window.Close()


def walking():
    layout = [[Text('Pick a direction to go')],
              [T(' ' * 11), Button('Up')],
              [Button('Left'), T(' ' * 15),
               Button('Right')],
              [T(' ' * 9), Button('Down')],
              [Quit(button_color=('white', 'orange'))]]

    window = Window("SimplePythonRPG", auto_size_text=True, default_element_size=(40, 1)).Layout(layout)

    event, values = window.Read()
    window.Close()
    return event


def HPbars(enemy, char):
    layout = [[T(' ' * 30), Text(enemy.Name + ": Lv " + str(enemy.Level))],
              [T(' ' * 30), Text('HP: ' + str(enemy.currHp) + '/' + str(enemy.Hp))],
              [Text(char.Name + ": Lv " + str(char.Level))],
              [Text("HP:   " + str(char.currHp) + '/' + str(char.Hp))],
              [Text("Mana: " + str(char.currMana) + '/' + str(char.mana))],
              [Button('Attack'), Button('Item'), Button('Scan')],
              [Button('Stats'), Button('Special'), Button('Run')]]

    window = Window("SimplePythonRPG", auto_size_text=True, default_element_size=(40, 1)).Layout(layout)

    event, values = window.Read()
    window.Close()
    return event


def listItems(inven):
    stuff = list(set(inven))
    layout = [[Text("Select the Item you wish to use")],
              [Listbox(values=stuff, size=(20, 5))],
              [OK(), Button('Back')]]
    window = Window("SimplePythonRPG", auto_size_text=True, default_element_size=(40, 1)).Layout(layout)

    event, values = window.Read()
    window.Close()
    if event == 'Back':
        return event
    return values[0][0]

