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


class BellTower:
    def __init__(self, *args):
        self.bells = list(args)

    def sound(self):
        for bell in self.bells:
            bell.sound()
        print("...")

    def append(self, item):
        self.bells.append(item)


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


bell = BigBell()
bell_p1 = BigBell("звонкий")
bell_p1.print_info()
bell_p4 = BigBell("серебряный", "на верёвочке", "с ленточкой", "хорошо смотрится на новогодней ёлке")
bell.print_info()
bell_p4.print_info()
bell_p1.print_info()
for _ in range(2):
    bell.sound()
    bell_p1.sound()
    bell_p4.sound()