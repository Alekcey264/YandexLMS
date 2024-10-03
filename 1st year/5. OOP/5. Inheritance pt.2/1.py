class Seat:
    def __init__(self, size, color, *args):
        self.size = size
        self.color = color
        self.args = ', '.join(list(map(str, args)))

    def __str__(self):
        if self.args:
            return f"{self.__class__.__name__}({self.size}, {self.color}, {self.args})"
        else:
            return f"{self.__class__.__name__}({self.size}, {self.color})"
    

class Chair(Seat):
    def __init__(self, size, color, *args):
        self.lenght = args[0]
        self.count = args[1]
        super().__init__(size, color, *args)


class ArmChair(Seat):
    def __init__(self, size, color, *args):
        self.lenght = args[0]
        self.material = args[1]
        super().__init__(size, color, *args)


class Stool(Seat):
    def __init__(self, size, color, *args):
        self.count = args[0]
        super().__init__(size, color, *args)


class BagChair(Seat):
    def __init__(self, size, color, *args):
        self.material = args[0]
        super().__init__(size, color, *args)


se = Seat(35, "beige")
ch = Chair(40, "pink", 80, 3)
ach = ArmChair(70, "black", 85, "leather")
st = Stool(48, "white", 3)
bc = BagChair(75, "orange", "matting")
for item in se, ch, ach, st, bc:
    print(item)