class Interaction:
    def __init__(self):
        self.carrier = ''
        self.const = 0

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.carrier}', {self.const})"


class Gravitational(Interaction):
    def __init__(self):
        self.carrier = "graviton"
        self.const = 1e-39


class ForceOfUniversalGravity(Gravitational):
    def __init__(self):
        self.G = 6.67e-11
        super().__init__()

    def __call__(self, m1, m2, r):
        return self.G * m1 * m2 / (r ** 2)


class Electromagnetic(Interaction):
    def __init__(self):
        self.carrier = "photon"
        self.const = 1 / 137


class CoulombPower(Electromagnetic):
    def __init__(self):
        self.k = 9e9
        super().__init__()

    def __call__(self, q1, q2, r):
        return self.k * q1 * q2 / (r ** 2)


class FrictionForce(Electromagnetic):
    def __init__(self, mu):
        self.mu = mu
        super().__init__()

    def __call__(self, N):
        return self.mu * N


class Strong(Interaction):
    def __init__(self):
        self.carrier = "gluon"
        self.const = 1


class Weak(Interaction):
    def __init__(self):
        self.carrier = "boson"
        self.const = 1e-15


em = Electromagnetic()
print(em, f"Interaction carrier of electromagnetic field is {em.carrier}.", sep='\n')
print()
ff = FrictionForce(0.15)
print(ff, f"Friction is an {ff.__class__.__bases__[0].__name__} force.", sep='\n')
print()
print(Strong(), Weak(), sep='\n')