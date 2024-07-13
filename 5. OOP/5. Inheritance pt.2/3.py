class AbstractCat:
    def __init__(self):
        self.zapas = 0
        self.weight = 0

    def eat(self, value):
        self.zapas += value
        while self.zapas >= 10:
            if self.weight < 100:
                self.weight += 1
            self.zapas -= 10

    def __str__(self):
        return f"{self.__class__.__name__} ({self.weight})"
    

class Kitten(AbstractCat):
    def __init__(self, weight):
        super().__init__()
        self.weight = weight

    def meow(self):
        return "meow..."
    
    def sleep(self):
        return ''.join(["Snore" for _ in range(self.weight // 5)])
    

class Cat(Kitten):
    def __init__(self, weight, name):
        super().__init__(weight)
        self.weight = weight
        self.name = name

    def meow(self):
        return "MEOW..."
    
    def get_name(self):
        return self.name
    
    def catch_mice(self):
        return "Got it!"
    
abscat = AbstractCat()
abscat.eat(125)
abscat.eat(17)
print(abscat)
kit = Kitten(21)
print(kit.sleep())
cat = Cat(83, 'Molly')
print(cat.meow())
print(cat.get_name())