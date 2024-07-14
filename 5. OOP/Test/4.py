class Trial:
    def __init__(self, text):
        self.text = sorted(text.split(" "))

    def get_trials(self):
        return " ".join(self.text)
    
    def __repr__(self):
        return f"Trial('{self.text[0]}')"


class GhostRescue(Trial): 
    def __init__(self, text, name):
        super().__init__(text)
        self.name = name

    def add(self, value):
        self.text.append(value)
        self.text = sorted(self.text)

    def pop(self, key):
        self.text.remove(key)
        return key
    
    def __len__(self):
        return len(self.text)
    
    def __contains__(self, item):
        return item in self.text
    
    def __repr__(self):
        return f"GhostRescue('{self.text[0]}', '{self.name}')"
    
    def __iter__(self):
        return iter(self.text)
    

tr = Trial("come see win")
print(tr)
print(tr.get_trials())
gr = GhostRescue("visions horror whispers", "Centerville")
print(len(gr))
print(gr.pop("horror"))
print(gr.get_trials())
print(gr)
gr = GhostRescue("pursue harass", "Outiss")
gr.add("harm")
for item in gr:
   print(item)
print(gr)
print(gr.get_trials())
print(issubclass(GhostRescue, Trial))