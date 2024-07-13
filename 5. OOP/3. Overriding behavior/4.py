class FlowingRectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.s = self.a * self.b / 2
        self.otn = self.a / self.b

    def __add__(self, other):
        self.s += other.s
        self.a = (2 * self.s * self.otn) ** 0.5
        self.b = (2 * self.s / self.otn) ** 0.5

    def __sub__(self, other):
        if self.s < other.s:
            self.a, self.b, self.s = 0, 0, 0
        else:
            self.s -= other.s
            self.a = (2 * self.s * self.otn) ** 0.5
            self.b = (2 * self.s / self.otn) ** 0.5
            
    def get_width(self):
        return round(self.a, 2)
    
    def get_height(self):
        return round(self.b, 2)
    
fr_1 = FlowingRectangle(12, 5)
fr_2 = FlowingRectangle(60, 1)
fr_1 + fr_2
print(fr_1.get_width(), fr_1.get_height())
fr_1 - fr_2
print(fr_1.get_width(), fr_1.get_height())