class BellTower:
    def __init__(self, *args):
        self.bells = list(args)

    def sound(self):
        for bell in self.bells:
            bell.sound()
        print("...")

    def append(self, item):
        self.bells.append(item)


class LittleBell:
    def sound(self):
        print("ding")


class BigBell():
    def __init__(self):
        self.flag = True
    
    def sound(self):
        if self.flag:
            print("ding")
            self.flag = False
        else:
            print("dong")
            self.flag = True