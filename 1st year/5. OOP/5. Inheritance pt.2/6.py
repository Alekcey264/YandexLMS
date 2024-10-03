class Mosquito:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        if self.__class__.__name__ == "MaleMosquito":
            return f"MaleMosquito, {self.age} days"
        elif self.__class__.__name__ == "FemaleMosquito":
            return f"FemaleMosquito, {self.age} days"
        elif self.__class__.__name__ == "MosquitoLarva":
            return f"MosquitoLarva, {self.age} days"
        else:
            return f"Mosquito, {self.age} days"
    

class MaleMosquito(Mosquito):
    def __init__(self, age):
        self.feed = "nectar"
        self.lives = "on land"
        super().__init__(age)

    def hearing(self):
        return f"I hear and see everything {self.lives}"


class FemaleMosquito(Mosquito):
    def __init__(self, age):
        self.feed = "blood"
        self.lives = "on land"
        super().__init__(age)

    def squeak(self):
        return f"The thin squeak of a mosquito after eating {self.feed}"


class MosquitoLarva(MaleMosquito, FemaleMosquito):
    def __init__(self, age):
        super().__init__(age)
        self.feed = "algae"
        self.lives = "in water"


mm = MaleMosquito(19)
fm = FemaleMosquito(42)
ml = MosquitoLarva(3)
for item in (mm, fm, ml):
    print(f'{item}, I feed {item.feed}, I lives {item.lives}')
m = Mosquito(13)
print(m)