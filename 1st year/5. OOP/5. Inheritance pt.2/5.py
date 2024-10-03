class Cucumber:
    def crunch(self):
        return "crunch"
    
    def refresh(self):
        return "Cucumber refresh."
    

class Tomato:
    def melt(self):
        return "melt in the mouth"
    
    def refresh(self):
        return "Tomato refresh."
    

class Salad(Tomato, Cucumber):
    pass


class Smoothie(Cucumber, Tomato):
    pass


sal = Salad()
sm = Smoothie()
print(sal.refresh())
print(sm.refresh())