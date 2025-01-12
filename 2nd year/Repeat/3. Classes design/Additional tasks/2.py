class Bell:
    def __init__(self, *args, **kwargs):
        self.args = list(args)
        self.kwargs = dict(sorted(kwargs.items()))

    def print_info(self):
        if self.kwargs or self.args:
            temp_string = '' 
            if self.kwargs:
                temp_string += ', '.join([f"{key}: {value}" for key, value in self.kwargs.items()])
                if self.args:
                    temp_string += "; "
            if self.args:
                temp_string += ', '.join([value for value in self.args])
            print(temp_string)
        else:
            print('-')


class LittleBell(Bell):
    def sound(self):
        print("ding")


class BigBell(Bell):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.flag = True
    
    def sound(self):
        if self.flag:
            print("ding")
            self.flag = False
        else:
            print("dong")
            self.flag = True


class BellTower:
    def __init__(self, *args):
        self.bells = list(args)

    def sound(self):
        for bell in self.bells:
            bell.sound()
        print("...")

    def print_info(self):
        for i in range(len(self.bells)):
            print(f"{i + 1} {self.bells[i].__class__.__name__}")
            self.bells[i].print_info()
        print()

    def append(self, item):
        self.bells.append(item)


class SizedBellTower(BellTower):
    def __init__(self, *args, size=10):
        self.size = size
        super().__init__(*args)
        while len(self.bells) > self.size:
            self.bells = self.bells[1:]

    def append(self, item):
        super().append(item)
        if len(self.bells) > self.size:
            self.bells = self.bells[1:]


class TypedBellTower(BellTower):
    def __init__(self, *args, bell_type=LittleBell):
        self.bell_type = bell_type
        super().__init__(*[item for item in args if isinstance(item, self.bell_type)])

    def append(self, item):
        if isinstance(item, self.bell_type):
            super().append(item)


b_bt = TypedBellTower(BigBell("бронзовый"),
                      LittleBell("медный", нота="ля"),
                      BigBell(название="Корноухий", вес="1275 пудов"),
                      bell_type=BigBell)
l_bt = TypedBellTower(BigBell("бронзовый"),
                      LittleBell("медный", нота="ля"),
                      BigBell(название="Корноухий", вес="1275 пудов"))
b_bt.print_info()
l_bt.print_info()

bb = BigBell("самый звонкий")
lb = LittleBell("самый маленький")

b_bt.print_info()
l_bt.print_info()