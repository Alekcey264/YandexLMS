import string
import random


def name(lenght):
    first_part_lenght = random.randint(2, lenght - 2)
    second_part_lenght = lenght - first_part_lenght - 1
    first_part = ''
    first_part += random.choice(string.ascii_letters)
    first_part += random.choice(string.digits)
    for _ in range(2, first_part_lenght):
        first_part += random.choice(string.ascii_letters + string.digits)
    first_part = first_part[0] + ''.join(random.sample(list(first_part[1:]), len(list(first_part[1:]))))
    second_part = ''
    second_part += random.choice(string.ascii_uppercase[:13])
    for _ in range(1, second_part_lenght):
        second_part += random.choice(string.ascii_lowercase)
    return first_part + ' ' + second_part

print(len(name(12)))