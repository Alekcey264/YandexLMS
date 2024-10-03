class Talking:
    def __init__(self, name):
        self.name = name
        self.yes = 0
        self.no = 0
        self.counter = 0

    def to_answer(self):
        self.counter += 1
        if self.counter % 2:
            self.yes += 1
            return "moore-moore"
        else:
            self.no += 1
            return "meow-meow"

    def number_yes(self):
        return self.yes

    def number_no(self):
        return self.no

tk = Talking('Pussy')
tk1 = Talking('Barsik')
print(tk.to_answer())
print(tk1.to_answer())
print(tk1.to_answer())
print(tk1.to_answer())
print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')
print(f'{tk1.name} says "yes" {tk1.number_yes()} times, "no" {tk1.number_no()} times')