class Wardrobe:
    def __init__(self, *values):
        self.values = values

    def __str__(self):
        return ' '.join(self.values)
    
    def __lt__(self, other):
        if self.__class__.__name__ == 'JustWardrobe' and other.__class__.__name__ == 'MagicWardrobe':
            return True
        elif self.__class__.__name__ == other.__class__.__name__:
            if len(self.values) < len(other.values):
                return True
        return False

    def __gt__(self, other):
        if self.__class__.__name__ == 'MagicWardrobe' and other.__class__.__name__ == 'JustWardrobe':
            return True
        elif self.__class__.__name__ == other.__class__.__name__:
            if len(self.values) > len(other.values):
                return True
        return False
    
    def __eq__(self, other):
        if self.__class__.__name__ == other.__class__.__name__:
            if len(self.values) == len(other.values):
                return True
        return False
    
    def __le__(self, other):
        if ((self.__class__.__name__ == 'JustWardrobe' and other.__class__.__name__ == 'MagicWardrobe') 
                or (self.__class__.__name__ == other.__class__.__name__)):
            if len(self.values) <= len(other.values):
                return True
        return False
    
    def __ne__(self, other):
        if self.__class__.__name__ != other.__class__.__name__:
            return True
        else:
            if len(self.values) != len(other.values):
                return True
        return False
    
    def __ge__(self, other):
        if ((self.__class__.__name__ == 'MagicWardrobe' and other.__class__.__name__ == 'JustWardrobe') 
                or (self.__class__.__name__ == other.__class__.__name__)):
            if len(self.values) >= len(other.values):
                return True
        return False


class JustWardrobe(Wardrobe):
    def __str__(self):
        return ', '.join(self.values).capitalize() + '.'


class MagicWardrobe(Wardrobe):
    def __str__(self):
        return ', '.join(sorted(self.values)).title() + '.'


jw1 = JustWardrobe("socks", "jacket", "hat")
jw2 = JustWardrobe("trousers", "blouse")
mw1 = MagicWardrobe("Narnia", "Wonderland", "Dreamland")
mw2 = MagicWardrobe("Kingdom", "Mordor", "Middle Earth")
print(jw1 > jw2)
print(jw1 == mw1)
print(jw2 <= mw2)
print(mw1 != mw2)