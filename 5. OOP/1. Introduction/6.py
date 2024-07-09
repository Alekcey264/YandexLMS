class TigerLily:
    def __init__(self, themes):
        self.themes = themes
    
    def add_theme(self, value):
        self.themes = self.themes + (value,)

    def shift_one(self):
        self.themes = (self.themes[-1], *self.themes[:-1])

    def reverse_order(self):
        self.themes = self.themes[::-1]

    def get_themes(self):
        return self.themes

    def get_first(self):
        return self.themes[0]

tl = TigerLily(('weather', 'rain'))
tl.add_theme('warm')
print(tl.get_themes())
tl.shift_one()
print(tl.get_first())