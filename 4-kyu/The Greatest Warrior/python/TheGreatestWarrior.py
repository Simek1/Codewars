class Warrior():
    def __init__(self):
        self.level=1
        self.rank="Pushover"
        self.ranks=["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
        self.experience=100
        self.achievements=[]
    def level_up(self):
        self.level=int(self.experience/100)
        self.rank=self.ranks[int(self.level/10)]
    def battle(self,enemy_level):
        if enemy_level<1 or enemy_level>100:
            return "Invalid level"
        else:
            if enemy_level==self.level:
                self.experience+=10
                if self.experience>10000:
                    self.experience=10000
                self.level_up()
                return "A good fight"
            elif enemy_level==self.level-1:
                self.experience+=5
                if self.experience>10000:
                    self.experience=10000
                self.level_up()
                return "A good fight"
            elif enemy_level<self.level-1:
                return "Easy fight"
            elif enemy_level>self.level and (enemy_level<self.level+5 or int(enemy_level/10)<=int(self.level/10)):
                diff=enemy_level-self.level
                self.experience+=20*diff*diff
                if self.experience>10000:
                    self.experience=10000
                self.level_up()
                return "An intense fight"
            else:
                return "You've been defeated"
    def training(self, args):
        desc, exp, min_lvl=args[0],args[1],args[2]
        if self.level>=min_lvl:
            self.experience+=exp
            if self.experience>10000:
                    self.experience=10000
            self.level_up()
            self.achievements.append(desc)
            return desc
        else:
            return "Not strong enough"
