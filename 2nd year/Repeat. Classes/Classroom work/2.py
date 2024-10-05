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