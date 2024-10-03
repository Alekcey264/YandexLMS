from math import pi


class SquareIntoCircle:
    def __init__(self, size_of):
        self.size_of = size_of

    def size(self):
        return round(2 * self.size_of / pi, 3)
    
    def area(self):
        return round(4 / pi * self.size_of ** 2, 3)


class CircleIntoSquare:
    def __init__(self, radius):
        self.radius = radius

    def size(self):
        return round(pi * self.radius / 2, 3)

    def area(self):
        return round(pi ** 2 * self.radius ** 2 / 4, 3)

sq = SquareIntoCircle(1)
print(sq.size(), sq.area(), sep='\n')
print()
circle = CircleIntoSquare(sq.size())
print(circle.size(), circle.area(), sep='\n')