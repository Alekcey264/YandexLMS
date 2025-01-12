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
    
    def __hash__(self):
        return hash((self.name, self.x, self.y))
    

points = [Point("A", 0, 3), Point("A", 0, 3),
          Point("A", 3, 0), Point("A", 3, 0),
          Point("B", 0, 3), Point("A", 0, 3)]
points_dir = {}
for i, point in enumerate(points):
    points_dir[point] = i
print(["{}: {}".format(k, v) for k, v in sorted(points_dir.items())])
['A(0, 3): 5', 'A(3, 0): 3', 'B(0, 3): 4']