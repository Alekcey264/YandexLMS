class Robot:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.places = [(self.x, self.y)]

    def fix_values(self):
        if self.x > 100:
            self.x = 100
        elif self.x < 0:
            self.x = 0
        if self.y > 100:
            self.y = 100
        elif self.y < 0:
            self.y = 0

    def move(self, moves):
        self.places = [self.places[-1]]
        for letter in moves:
            if letter == "N":
                self.y += 1
            elif letter == "S":
                self.y -= 1
            elif letter == "E":
                self.x += 1
            elif letter == "W":
                self.x -= 1
            self.fix_values()
            self.places.append((self.x, self.y))
        return self.places[-1]

    def path(self):
        return self.places

r = Robot((0, 0))
print(r.move('NENWEE'))
print(*r.path())
print()
print(r.move('ENWEWSNN'))
print(*r.path())
print()
print(r.move('NNNNNNNSSWENWEWSNN'))
print(*r.path())