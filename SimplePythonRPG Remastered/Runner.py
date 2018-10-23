from SimpleRPG import *
from GUI import *

main = createCharacter()
leave = False
initialScreen(str(main.Hp), str(main.Atk), str(main.Def), str(main.Spd), str(main.mana))

while leave == False and main.currHp > 0:
    x = walking()
    up = random()
    down = random()
    left = random()
    right = random()
    if x == 'Quit':
        leave = True
    else:
        if x == 'Up':
            sit = getSit(up)
        elif x == 'Down':
            sit = getSit(down)
        elif x == 'Left':
            sit = getSit(left)
        else:
            sit = getSit(right)
        sits(sit, main)

Popup("Thanks for playing!", "You got to level " + str(main.Level))
