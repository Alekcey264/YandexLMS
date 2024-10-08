PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]  
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]  
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]

class Note:
    def __init__(self, name, is_long=False):
        self.long = {"до": "до-о", "ре": "ре-э", "ми": "ми-и", "фа": "фа-а", "си": "си-и",
                     "соль": "со-оль", "ля": "ля-а"}
        if is_long:
            self.name = self.long[name]
        else:
            self.name = name

    def __str__(self):
        return self.name
    
    def __lchange(self, times, type: list):
        for _ in range(times):
            if self.name == type[0]:
                self.name = type[-1]
            else:
                self.name = type[type.index(self.name) - 1]

    def __lshift__(self, times):
        if self.name in PITCHES:
            self.__lchange(times, PITCHES)
        else:
            self.__lchange(times, LONG_PITCHES)
        return self.name
    
    def __rchange(self, times, type: list):
        for _ in range(times):
            if self.name == type[-1]:
                self.name = type[0]
            else:
                self.name = type[type.index(self.name) + 1]

    def __rshift__(self, times):
        if self.name in PITCHES:
            self.__rchange(times, PITCHES)
        else:
            self.__rchange(times, LONG_PITCHES)
        return self.name
    
fa2 = Note("до")
print(fa2 >> 3)

