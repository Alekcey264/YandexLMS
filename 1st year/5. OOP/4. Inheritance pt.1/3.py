class Holiday:
    def __init__(self, name, day):
        self.name = name
        self.day = day

    def __str__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.day}')"
    
    def get_season(self):
        seasons = {
            "Winter": ("December", "January", "February"), 
            "Spring": ("March", "April", "May"),
            "Summer": ("June", "July", "August"),
            "Autumn": ("September", "October", "November")}
        for key, value in seasons.items():
            if self.day.split()[-1] in value:
                return key
            

class NewYear(Holiday):
    def __init__(self, name, day, peoples: list):
        self.peoples = peoples[:]
        super().__init__(name, day)
    
    def congratulate(self, human):
        if human in self.peoples:
            return f"Dear {human}! Happy New Year!"
        else:
            self.peoples.append(human)
            return f"Dear new friend {human}! Have fun this New Year!"
    
    def get_greet(self):
        return self.peoples
    

class MuseumDay(Holiday):
    def __init__(self, name, day, museums):
        self.museums = museums
        super().__init__(name, day)

    def get_museums(self):
        return self.museums

hl = Holiday('183rd Year Day', '2 July')
print(hl, hl.get_season(), sep='\n')
people = ['Sonya', 'Kate', 'Andrey']
ny = NewYear("Someones' New Year", '17 April', people)
print(ny.get_season())
print(ny, ny.congratulate('Kate'), ny.congratulate('Lilly'), sep='\n')
print(people)
print(ny.get_greet())
museums = ['New Acropolis', 'Louvre', 'British Museum']
md = MuseumDay('Ones more Museum Day', '29 September', museums)
print(md)
print(', '.join(sorted(md.get_museums())))
print(md.get_season())