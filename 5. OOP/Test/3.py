class Talking:
    def __init__(self, name, time, theme=list()):
        self.name = name
        self.time = time
        self.theme = theme

    def add_theme(self, value):
        self.theme.append(value)

    def change_theme(self):
        self.theme = self.theme[1:] + self.theme[:1]

    def change_time(self, number):
        self.time += number

    def __str__(self):
        return f"{self.name}'s Conversation, main theme is {self.theme[0]} for {self.time} minutes"

    def __eq__(self, other):
        return (self.time, len(self.theme), self.name) == (other.time, len(other.theme), other.name)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return (self.time, len(self.theme), self.name) < (other.time, len(other.theme), other.name)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return (self.time, len(self.theme), self.name) > (other.time, len(other.theme), other.name)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)


    

tk = Talking('Alice', 5)
tk1 = Talking('Hatter', 5)
print(tk < tk1)
tk.add_theme('cricket')
tk1.add_theme('teatime')
print(tk == tk1)
tk.change_time(1)
print(tk >= tk1)