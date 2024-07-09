class BlackCat():
    def __init__(self, name):
        self.name = name
        self.plays = {
            "wool": 0,
            "tail": 0
        }

    def play(self, kind, n):
        if kind in self.plays.keys():
            self.plays[kind] = self.plays.get(kind, 0) + n
        else:
            for key in self.plays.keys():
                self.plays[key] = 0

    def get_play(self):
        return (self.plays["wool"], self.plays["tail"])

bc = BlackCat('Kitty')
bc.play('wool', 5)
bc.play('wool', 3)
bc.play('tail', 2)
bc.play('wool', 1)
print(bc.get_play())
bc.play('hand', 8)
print(bc.get_play())