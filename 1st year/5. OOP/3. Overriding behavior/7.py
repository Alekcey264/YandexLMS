class Train:
    def __init__(self, number, wagons=list()):
        self.number = number
        self.wagons = wagons
    
    def get_number(self):
        return self.number
    
    def get_wagons(self):
        return self.wagons
    
    def append(self, other):
        self.wagons.append(other)

    def __len__(self):
        return len(self.wagons)

    def __str__(self):
        return f"Train {self.number} has {len(self.wagons)} wagons"

    def __getitem__(self, other):
        return self.wagons[other]
    
    def __setitem__(self, other, value):
        self.wagons[other] = value

    def __delitem__(self, other):
        if other == len(self.wagons) - 1:
            del self.wagons[other]

    def __iter__(self):
        return iter(self.wagons)


class Wagon:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"№{self.number}"
    
    def get_number(self):
        return self.number
    
tr = Train(206, [Wagon(1), Wagon(2), Wagon(3)])
print(tr)
print(', '.join([str(item.get_number()) for item in tr]))
print(f"This train has number {tr.get_number()}.")
for i in range(4, 10):
    tr.append(Wagon(i))
print(*tr.get_wagons())