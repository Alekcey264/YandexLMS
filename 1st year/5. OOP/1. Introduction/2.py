class Avalanche:
    def __init__(self):
        self.string = "O"
    
    def go(self):
        print(self.string)
        if self.string == "O":
            self.string = self.string.replace("O", "ooOoo")
        else:
            self.string = self.string.translate(str.maketrans({"O": "ooOoo", "o": "oOo"}))

ava = Avalanche()
ava.go()
ava.go()
ava.go()