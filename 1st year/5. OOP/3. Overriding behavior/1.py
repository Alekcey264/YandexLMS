class ModifiedString:
    def __init__(self, first):
        self.first = first

    def __add__(self, other):
        return ModifiedString(self.first + other)
    
    def __radd__(self, other):
        return ModifiedString(other + self.first)
    
    def __sub__(self, other):
        return ModifiedString(''.join([letter for letter in self.first 
                                       if letter.lower() not in other.lower()]))
    
    def __rsub__(self, other):
        return ModifiedString(''.join([letter for letter in other 
                                       if letter.lower() not in self.first.lower()]))
    
    def __str__(self):
        return self.first


ms_1 = ModifiedString('My heart in the Highland')
ms_2 = 'my heart is not here'
ms_3 = ms_1 + ms_2
ms_4 = ms_2 + ms_1
ms_5 = ms_1 - ms_2
ms_6 = ms_2 - ms_1
print(isinstance(ms_3, ModifiedString))
print(isinstance(ms_4, ModifiedString))
print(isinstance(ms_5, ModifiedString))
print(isinstance(ms_6, ModifiedString))
print(ms_1)