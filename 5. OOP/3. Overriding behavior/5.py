class PearsBasket:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return str(self.a)

    def __repr__(self):
        return f"PearsBasket({self.a})"
    
    def __floordiv__(self, other):
        if self.a % other:
            return [*[PearsBasket(self.a // other) for _ in range(other)], PearsBasket(self.a % other)]
        else:
            return [PearsBasket(self.a // other) for _ in range(other)]
    
    def __mod__(self, other):
        return self.a % other

    def __add__(self, other):
        return PearsBasket(self.a + other.a)
    
    def __sub__(self, other):
        if other > self.a:
            self.a = 0
        else:
            self.a -= other

pb_1 = PearsBasket(71)
array = pb_1 // 3
print(*array)
print(pb_1)
pb_2 = PearsBasket(132)
print(pb_2 % 19)
pb_3 = pb_1 + pb_2
print([pb_3])
print(pb_3 % 7)
pb_1 - 172
print(pb_2 // 3)