from random import randint, choice


def generate_fandom(n, names: list):
    temp_names = names
    new = list()
    for _ in range(n):
        city_num = randint(0, len(temp_names) - 1)
        city = temp_names[city_num]
        temp_names.pop(city_num)
        size = randint(10, 20)
        people = choice(range(10000, 1000000, 10000))
        place = randint(100, 500)
        while place in list(map(lambda x: x[3], new)):
            place = randint(100, 500)
        new.append((city, size, people, place))
    return new


names = ['Ankh-Morpork', 'Silent Hill', 'New Vasuki', 'Mordor', 'Twin Peaks', 'Springfield', 'Zurbagan', 'Arkanar', 'Zion', 'Atlantis', 'Castle Rock', 'Kitezh', 'Shambala']
for item in generate_fandom(5, names):
    print(*item)