class EpicHero:
    def __init__(self, name, wins, weapons: list):
        self.name = name
        self.wins = wins
        self.weapons = weapons
    
    def __str__(self):
        return f"Epic Hero {self.name}, {self.wins}"
    
    def __repr__(self):
        return f"EpicHero('{self.name}', {self.wins}, {sorted(self.weapons)})"

    def add_win(self):
        self.wins += 1

    def add_weapon(self, item):
        self.weapons.append(item)

    def del_weapon(self, item):
        if item in self.weapons:
            self.weapons.remove(item)

    def __lt__(self, other):
        return ((self.wins < other.wins) and (len(self.weapons) < len(other.weapons)) 
                and (len(self.name) < len(other.name)) and (self.name.lower() < other.name.lower()))
    
    def __le__(self, other):
        return ((self.wins <= other.wins) or (len(self.weapons) <= len(other.weapons)) 
                or (len(self.name) <= len(other.name)) or (self.name.lower() <= other.name.lower()))

    def __eq__(self, other):
        return ((self.wins == other.wins) or (len(self.weapons) == len(other.weapons)) 
                or (len(self.name) == len(other.name)) or (self.name.lower() == other.name.lower()))

    def __ne__(self, other):
        return ((self.wins != other.wins) or (len(self.weapons) != len(other.weapons)) 
                or (len(self.name) != len(other.name)) or (self.name.lower() != other.name.lower()))
        
    def __gt__(self, other):
        return ((self.wins > other.wins) and (len(self.weapons) > len(other.weapons)) 
                and (len(self.name) > len(other.name)) and (self.name.lower() > other.name.lower()))

    def __ge__(self, other):
        return ((self.wins >= other.wins) or (len(self.weapons) >= len(other.weapons)) 
                or (len(self.name) >= len(other.name)) or (self.name.lower() >= other.name.lower()))
            


eh_1 = EpicHero('Ilya', 2, ['mace', 'bow'])
eh_2 = EpicHero('Dobrynya', 2, ['knife'])
print(eh_1, eh_2, sep='\n')
print([eh_1, eh_2])
eh_2.add_weapon('sword')
print(eh_1 >= eh_2)