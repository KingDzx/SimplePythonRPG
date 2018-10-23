from BattleFunctions import *
class Entity():
    def __init__(self,Hp,Atk,Def,Spd,Level,Name):
        self.Name = Name
        self.Hp = Hp
        self.currHp = Hp
        self.Atk = Atk
        self.Def = Def
        self.Spd = Spd
        self.Level = Level
        
    def Attack(self,Def):
        crit,dodge,damage = calDamage(self.Atk,Def,self.Level)
        return crit,dodge,damage
    
    def takeDamage(self,damage):
        self.currHp -= damage
        
    def isAlive(self):
        if self.currHp <= 0:
            return False
        else:
            return True
        