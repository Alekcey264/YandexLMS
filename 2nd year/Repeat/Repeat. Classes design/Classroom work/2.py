N = 7  
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]  
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]  
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]


class Note:
    def __init__(self, name, is_long=False):
        if is_long:
            self.name = LONG_PITCHES[PITCHES.index(name)]
        else:
            self.name = name

    def __str__(self):
        return self.name
       
    def __lchange(self, times, type: list):
        temp = self.name
        for _ in range(times):
            if temp == type[0]:
                temp = type[-1]
            else:
                temp = type[type.index(temp) - 1]
        return Note(temp)

    def __lshift__(self, times):
        if self.name in PITCHES:
            return self.__lchange(times, PITCHES)
        else:
            return self.__lchange(times, LONG_PITCHES)
    
    def __rchange(self, times, type: list):
        temp = self.name
        for _ in range(times):
            if temp == type[-1]:
                temp = type[0]
            else:
                temp = type[type.index(temp) + 1]
        return Note(temp)

    def __rshift__(self, times):
        if self.name in PITCHES:
            return self.__rchange(times, PITCHES)
        else:
            return self.__rchange(times, LONG_PITCHES)

    def __gt__(self, other):
        if self.name in PITCHES:
            num = PITCHES.index(self.name)
        else:
            num = LONG_PITCHES.index(self.name)
        if other.name in PITCHES:
            other_num = PITCHES.index(other.name)
        else:
            other_num = LONG_PITCHES.index(other.name)
        return num > other_num
    
    def __lt__(self, other):
        if self.name in PITCHES:
            num = PITCHES.index(self.name)
        else:
            num = LONG_PITCHES.index(self.name)
        if other.name in PITCHES:
            other_num = PITCHES.index(other.name)
        else:
            other_num = LONG_PITCHES.index(other.name)
        return num < other_num

    def __ge__(self, other):
        if self.name in PITCHES:
            num = PITCHES.index(self.name)
        else:
            num = LONG_PITCHES.index(self.name)
        if other.name in PITCHES:
            other_num = PITCHES.index(other.name)
        else:
            other_num = LONG_PITCHES.index(other.name)
        return num >= other_num

    def __le__(self, other):
        if self.name in PITCHES:
            num = PITCHES.index(self.name)
        else:
            num = LONG_PITCHES.index(self.name)
        if other.name in PITCHES:
            other_num = PITCHES.index(other.name)
        else:
            other_num = LONG_PITCHES.index(other.name)
        return num <= other_num

    def __eq__(self, other):
        if self.name in PITCHES:
            num = PITCHES.index(self.name)
        else:
            num = LONG_PITCHES.index(self.name)
        if other.name in PITCHES:
            other_num = PITCHES.index(other.name)
        else:
            other_num = LONG_PITCHES.index(other.name)
        return num == other_num

    def __ne__(self, other):
        if self.name in PITCHES:
            num = PITCHES.index(self.name)
        else:
            num = LONG_PITCHES.index(self.name)
        if other.name in PITCHES:
            other_num = PITCHES.index(other.name)
        else:
            other_num = LONG_PITCHES.index(other.name)
        return num != other_num
    
    def get_interval(self, other):
        if self.name in PITCHES:
            num = PITCHES.index(self.name)
        else:
            num = LONG_PITCHES.index(self.name)
        if other.name in PITCHES:
            other_num = PITCHES.index(other.name)
        else:
            other_num = LONG_PITCHES.index(other.name)
        return INTERVALS[abs(other_num - num)]


class Melody:
    def __init__(self, *args):
        if args:
            self.melody = args[0]  
        else:
            self.melody = list()

    def __str__(self):
        return ', '.join([item.name for item in self.melody]).capitalize()
    
    def append(self, new):
        self.melody.append(new)

    def replace_last(self, new):
        self.melody[-1] = new

    def remove_last(self):
        self.melody.pop()

    def clear(self):
        self.melody.clear()

    def __len__(self):
        return len(self.melody)
    
    def __lshift__(self, times):
        temp_melody = self.melody
        for _ in range(times):
            temp_list = [item.name for item in temp_melody]
            if "до" not in temp_list and "до-о" not in temp_list:
                temp_melody = [item << 1 for item in temp_melody]
            else: 
                break
        else:
            return Melody(temp_melody)
        return ', '.join([item.name for item in self.melody]).capitalize()

    def __rshift__(self, times):
        temp_melody = self.melody
        for _ in range(times):
            temp_list = [item.name for item in temp_melody]
            if "си" not in temp_list and "си-и" not in temp_list:
                temp_melody = [item >> 1 for item in temp_melody]
            else: 
                break
        else:
            return Melody(temp_melody)
        return ', '.join([item.name for item in self.melody]).capitalize()

    
melody = Melody([Note('ля'), Note('соль'), Note('ми'),  Note('до', True)])
print(melody)
print(Melody() >> 2)
melody_up = melody >> 1
melody_down = melody << 1
melody.replace_last(Note('соль'))
print('>> 1:', melody_up)
print('<< 1:', melody_down)
print(melody)