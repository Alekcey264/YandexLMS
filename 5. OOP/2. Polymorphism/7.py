from string import ascii_uppercase


class LettersRhombus:
    def __init__(self, letter, separator=" "):
        self.letter = letter
        self.lenght = len(ascii_uppercase[:ascii_uppercase.index(letter)])
        self.letters = ascii_uppercase[:ascii_uppercase.index(letter)]
        self.separator = separator

    def rows(self):
        background = self.separator
        template = [[background for _ in range(self.lenght * 2 + 1)] for _ in range(self.lenght + 1)]
        template[0][self.lenght] = 'A'
        for index in range(1, len(template)):
            template[index][self.lenght - index] = ascii_uppercase[index]
            template[index][-(self.lenght - index) - 1] = ascii_uppercase[index]
        template.extend(list(reversed(template))[1:])
        template = [''.join(item) for item in template]
        return template
    
    def cols(self):
        background = self.separator
        template = [[background for _ in range(self.lenght * 2 + 1)] for _ in range(self.lenght + 1)] 
        template[0][self.lenght] = self.letter
        for index in range(1, len(template)):
            template[index][self.lenght - index] = self.letters[-index]
            template[index][-(self.lenght - index) - 1] = self.letters[-index]
        template.extend(list(reversed(template))[1:])
        template = [''.join(item) for item in template]
        return template





lines = LettersRhombus("D", "-")
print(*lines.rows(), sep="\n")

lines = LettersRhombus("E")
print(*lines.cols(), sep="\n")