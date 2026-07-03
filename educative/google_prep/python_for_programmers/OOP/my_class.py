class Player():
    team_name = 'india'
    former_team = []

    def __init__(self, name='kk',profession="NA"):
        self.name = name
        self.team_name = 'india : '+name
        self.former_team.append(name)
        self.__profession = profession
        print(" constructor call - default init",name)

    def get_profession(self):
        return self.__profession

    def over(self,p1=1,p2=2):
        print(p1,p2)

    def over(self, p1=1,p2=2,p3=3):
        print(p1,p2,p3)

    def over(self,p4,p1=1,p2=2,p3=3):
        print(p1,p2,p3,p4,self.__profession) ## only this one will be available

    def over_arg(self, *args):
        print(sum(args))    

    def _display_all(self):
        print("private method")    

    def how_many_goals(self):
        return 100    

    @staticmethod
    def static_check():
        print("this is static call")    

    # def kwargs_check(self, **kwargs):
    #     for k in kwargs:
    #         print(f'{k.keys} : {k.items}')    


    print(team_name)    

class UselessPlayer(Player):
    pass


print(Player.static_check())
obj1 = Player("omi")
print(obj1.name,Player.former_team)

obj2 = Player("omi2")
print(obj2._.name,Player.former_team)

obj2.over(1,2)


obj2.over(1,2,3)


obj2.over(1,2,3,4)

obj2.over_arg(1,2,3)
