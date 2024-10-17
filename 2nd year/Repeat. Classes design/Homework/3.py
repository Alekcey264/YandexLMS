class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{self.name}({self.x}, {self.y})"
    
    def __invert__(self):
        return Point(self.name, self.y, self.x)
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_coords(self):
        return (self.x, self.y)
    
    def __repr__(self):
        return f"Point('{self.name}', {self.x}, {self.y})"
    
    def __eq__(self, other):
        return (self.name, self.x, self.y) == (other.name, other.x, other.y)

    def __gt__(self, other):
        return (self.name, self.x, self.y) > (other.name, other.x, other.y)
    
    def __lt__(self, other):
        return (self.name, self.x, self.y) < (other.name, other.x, other.y)
    
    def __ge__(self, other):
        return (self.name, self.x, self.y) >= (other.name, other.x, other.y)
    
    def __le__(self, other):
        return (self.name, self.x, self.y) <= (other.name, other.x, other.y)
    

class CheckMark:
    def __init__(self, point_a, point_b, point_c):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.points = [self.point_a, self.point_b, self.point_c]

    def __get_status(self, point_a, point_b, point_c):
        determinant = (point_b.x - point_a.x) * (point_c.y - point_b.y) - \
                      (point_c.x - point_b.x) * (point_b.y - point_a.y)
        return determinant != 0

    def __str__(self):
        return ''.join([item.name for item in self.points])

    def __bool__(self):
        return self.__get_status(self.point_a, self.point_b, self.point_c)
    
    def __eq__(self, other):
        if self.point_b.x == other.point_b.x and self.point_b.y == other.point_b.y:
            if self.point_a.x == other.point_a.x and self.point_a.y == other.point_a.y:
                if self.point_c.x == other.point_c.x and self.point_c.y == other.point_c.y:
                    return True
            elif self.point_a.x == other.point_c.x and self.point_a.y == other.point_c.y:
                if self.point_c.x == other.point_a.x and self.point_c.y == other.point_a.y:
                    return True
        return False

    
A1 = Point('P1', -30, 20)
A2 = Point('P2', -10, -10)
A3 = Point('P3', -20, -30)
A4 = Point('P4', 20, -30)
A5 = Point('P5', 30, 20)
A6 = Point('P6', 10, 10)
A7 = Point('P7', 30, 30)

cm_a = CheckMark(A1, A2, A3)
cm_b = CheckMark(A3, A2, A4)
cm_c = CheckMark(A3, A2, A7)
cm_d = CheckMark(A4, A2, A3)
cm_e = CheckMark(A2, A6, A7)
cm_f = CheckMark(A7, A5, A6)
cm_g = CheckMark(A1, A1, A6)
cm_h = CheckMark(A4, A5, A4)
cm_i = CheckMark(A3, A3, A3)

print(bool(cm_a))
print(bool(cm_b))
print(bool(cm_c))
print(bool(cm_d))
print(bool(cm_e))
print(bool(cm_f))
print(bool(cm_g))
print(bool(cm_h))
print(bool(cm_i))
