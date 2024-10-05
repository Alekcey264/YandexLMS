PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]


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
    

class LoudNote(Note):
    def __init__(self, name, is_long=False):
        super().__init__(name, is_long)
        self.name = self.name.upper()


class DefaultNote(Note):
    def __init__(self, name="до", is_long=False):
        super().__init__(name, is_long)

    
class NoteWithOctave(Note):
    def __init__(self, name, octave, is_long=False):
        super().__init__(name, is_long)
        self.octave = octave

    def __str__(self):
        return f"{self.name} ({self.octave})"

print(Note("соль"))

print(LoudNote(PITCHES[4]))
print(LoudNote("си", is_long=True))

print(DefaultNote("ми"))
print(DefaultNote())
print(DefaultNote(is_long=True))

print(NoteWithOctave("ре", "первая октава"))
print(NoteWithOctave("ля", "малая октава", is_long=True))