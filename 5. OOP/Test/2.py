class HumptyDumpty:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __iadd__(self, number):
        part = (2 * number) // 3
        return HumptyDumpty(self.length + part, self.width + number - part)
    
    def __isub__(self, number):
        part = (2 * number) // 3
        self.length = self.length - part
        self.width = self.width - number + part
        if self.length < 1:
            self.length = 1
        if self.width < 1:
            self.width = 1
        return HumptyDumpty(self.length, self.width)
        
    def __add__(self, other):
        return HumptyDumpty(self.length + other.length, self.width + other.width)
    
    def __truediv__(self, number):
        return [HumptyDumpty(self.length // number, self.width // number) for _ in range(number)]

    def __str__(self):
        return f"Humpty Dumpty has sizes: {self.length}, {self.width}"
    
    def __repr__(self):
        return f"HumptyDumpty({self.length}, {self.width})"
    
hd = HumptyDumpty(5, 3)
hd += 7
print(hd)
hd -= 10
print(hd)
hd1 = hd + HumptyDumpty(1, 4)
print()
print(hd1, hd, sep='\n')