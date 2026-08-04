import math

class Shape:

    def __init__(self):
        self.sides = 0
    
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, redius):
        self.redius = redius

    def get_area(self):
        return math.pi * (self.redius ** 2)

class Rectangle(Shape):
    def __init__(self, length,breadth):
        self.side = 4
        self.length=length
        self.breadth = breadth

    def get_area(self):
        return self.length * self.breadth    


areas = [Rectangle(4,5),Circle(5)] ## add more without chaning the looop
for shape in areas:
    print('area is :',shape.get_area())


