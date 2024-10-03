class Hyperbole:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"y = {self.a} + {self.b}/x"
    
    def __repr__(self):
        return f"Hyp({self.a}, {self.b})"
    
    def __call__(self, h):
        if h == 0:
            return None
        else:
            return round(self.a + (self.b) / h, 6)
        
hyp = Hyperbole(2.5, 3)
print(hyp(2))
print(hyp.__repr__())
print(hyp)