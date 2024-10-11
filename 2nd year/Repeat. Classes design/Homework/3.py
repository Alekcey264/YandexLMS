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

    def __get_status(self, point_a, point_b, point_c):
        return False

    def __str__(self):
        return self.point_a.name + self.point_b.name + self.point_c.name

    def __bool__(self):
        return self.__get_status(self.point_a, self.point_b, self.point_c)
    
    def __eq__(self, other):
        return (self.point_a, self.point_b, self.point_c) == (other.point_a, other.point_b, other.point_c) or (self.point_a, self.point_b, self.point_c) == (other.point_c, other.point_b, other.point_a)
        
    

p_A = Point('A', 1, 2)
p_B = Point('B', 0, 1)
p_C = Point('C', -1, 2)
p_D = Point('D', 2, 2)
p_E = Point('E', 2, 0)
p_F = Point('F', 2, -1)
cm_ABC = CheckMark(p_A, p_B, p_C)
cm_DEF = CheckMark(p_D, p_E, p_F)
cm_ABB = CheckMark(p_A, p_B, p_B)
print(cm_ABC, bool(cm_ABC))
print(cm_DEF, bool(cm_DEF))
print(cm_ABB, bool(cm_ABB))    