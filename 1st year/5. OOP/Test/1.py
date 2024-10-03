class BeeElephant:
    def __init__(self, bee_part, elph_part):
        self.bee_part = bee_part
        self.elph_part = elph_part

    def fly(self):
        return self.bee_part >= self.elph_part

    def trumpet(self):
        if self.elph_part >= self.bee_part:
            return "tu-tu-doo-doo!"
        else:
            return "wzzzzz"

    def eat(self, meal, value):
        if meal == "nectar":
            self.elph_part -= value
            self.bee_part += value
        elif meal == "grass":
            self.bee_part -= value
            self.elph_part += value

        if self.elph_part > 100:
            self.elph_part += (100 - self.elph_part)
        elif self.elph_part < 0:
            self.elph_part -= (0 + self.elph_part)

        if self.bee_part > 100:
            self.bee_part += (100 - self.bee_part)
        elif self.bee_part < 0:
            self.bee_part -= (0 + self.bee_part)

    def get_parts(self):
        return (self.bee_part, self.elph_part)