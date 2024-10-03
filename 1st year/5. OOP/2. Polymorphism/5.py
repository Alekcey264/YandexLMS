from math import pi


class Square:
    def __init__(self, side):
        self.side = side
    
    def extrude(self, h):
        return self.side * self.side * h
    
    
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def extrude(self, h):
        return self.a * self.b * h
    

class Triangle:
    def __init__(self, side):
        self.side = side

    def extrude(self, h):
        p = self.side * 3 / 2
        s = (p * ((p - self.side) ** 3)) ** 0.5
        return s * h


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def extrude(self, h):
        return pi * self.radius ** 2 * h
    

sq = Square(52)
rec = Rectangle(25, 44)
tr = Triangle(42)
cir = Circle(57)
for item in (sq, rec, tr, cir):
    print(item.extrude(49))