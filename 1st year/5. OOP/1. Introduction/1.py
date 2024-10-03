class Controller:
    def __init__(self):
        self.channel = 1

    def click(self):
        if self.channel == 5:
            self.channel = 1
        else:
            self.channel += 1

c = Controller()
c.click()
c.click()
print(c.channel)
c.click()
c.click()
print(c.channel)