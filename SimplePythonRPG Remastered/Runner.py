from SimpleRPG import *
from msvcrt import getch

main = createCharacter()
leave = False
print("Your Stats are:")
print('HP:', main.Hp)
print('Attack:', main.Atk)
print('Defense:', main.Def)
print('Speed:', main.Spd)
print('Mana:', main.Spd)
os.system('pause')
os.system('CLS')
while leave == False and main.currHp > 0:
    print('Pick a direction to go')
    print('       Up      ')
    print('Left       Right')
    print('      Down     ')
    print('                    Exit')
    print('Press direction or press Q to leave game \n')
    # choice = choice.lower()
    key = ord(getch())
    os.system('CLS')
    if key == 113:  # Q
        leave = True
    elif key == 224:
        key = ord(getch())
        if key == 72 or key == 80 or key == 77 or key == 75:
            sit = random()
            if sit <= 0.4:
                num = 1
            elif 0.4 < sit <= 0.75:
                num = 2
            elif 0.75 < sit <= 1.0:
                num = 3
            sits(num, main)
    else:
        print("Not a choice, please enter a valid choice")
    os.system('pause')
    os.system('CLS')

print("Thanks for playing!")
print("You got to level", main.Level)
os.system('pause')
