class Giant:
    def __init__(self, name, **kwargs):
        self.name = name
        if kwargs:
            self.kwargs = kwargs

    def __getitem__(self, key):
        return self.kwargs[key]
    
    def __setitem__(self, key, value):
        self.kwargs[key] = value

    def __iter__(self):
        return iter(self.kwargs)
    
    def __str__(self):
        return f"{self.__class__.__name__} {self.name} with the number of properties {len(self.kwargs)}."

class UsualMan(Giant):
    def __init__(self, name, *kwargs):
        super().__init__(name, **{item: 1 for item in kwargs})
        
    def __len__(self):
        return len(self.kwargs)
    
    def __call__(self, value):
        self.kwargs[value] = self.kwargs.get(value, 0) + 1


prop = {"height": 2, "step": 5, "loud": 8}
gt = Giant("Jack", **prop)
print(gt)
for item in gt:
    print(f"{item}: {gt[item]}")
print()
items = ["cool", "friendly", "jolly"]
um = UsualMan("Jib", *items)
print(len(um))
um("jolly")
um["cool"] = 3
for item in um:
    print(f"{item}: {um[item]}")