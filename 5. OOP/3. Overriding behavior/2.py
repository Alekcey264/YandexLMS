class ChairLeg:
    def __init__(self, length):
        self.length = length

    def __mul__(self, other):
        self.length *= other

    def __rmul__(self, other):
        self.length = other * self.length

    def __truediv__(self, other):
        self.length /= other

    def __mod__(self, other):
        return self.length % other

chl = ChairLeg(15)
chl * 3
print(chl.length)
2 * chl
print(chl.length)
print(chl % 7)