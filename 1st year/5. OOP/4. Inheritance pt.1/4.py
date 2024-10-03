C_SVET = 1


class ClassicalMechanics:
    def __init__(self, v):
        self.v = v

    def __str__(self):
        return f"Object {self.__class__.__name__}, velocity {self.v} c"

    def __call__(self, value):
        return self.v + value

class SpecialTheoryRelativity(ClassicalMechanics):
    def __call__(self, value):
        if self.v < 0.1 and value < 0.1:
            return super().__call__(value)
        else:
            return (self.v + value) / (1 + self.v * value)

cm = ClassicalMechanics(0.05)
st = SpecialTheoryRelativity(0.05)
print(cm(0.05))
print(st(0.05))
print(cm, st, sep='\n')