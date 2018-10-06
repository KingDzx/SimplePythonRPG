from SimpleRPG import *
main = createCharacter()
leave = False
print ("Your Stats are:")
print ('HP: ' + str(main.Hp))
print ('Attack: ' + str(main.Atk))
print ('Defense: ' + str(main.Def))
print ('Speed: ' + str(main.Spd))
print ('Mana: ' + str(main.Spd))
os.system('pause')
os.system('CLS')
while leave == False and main.currHp> 0:
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
            num = 1
        elif sit > 0.70 and sit <= 1.0:
            num = 1
        new = sits(num,main)
    else:
        print ("Not a choice, please enter a valid choice")
    os.system('pause')
    os.system('CLS')
    
print ("Thanks for playing!")
print ("You got to level " + main.Level)
os.system('pause')