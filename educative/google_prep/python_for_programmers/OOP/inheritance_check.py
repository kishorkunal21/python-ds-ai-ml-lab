class Player:

    def __init__(self, name, age):
        print("super called")
        self.name=name
        self.age = age
    
    def print_details(self):
        print(self.age,self.name)


class UselessPlayer(Player):

    def __init__(self, name, age):
        print("useless called")
        super().__init__(name, age)


up = UselessPlayer("Kohli",35)
up.print_details()