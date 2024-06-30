import string
import random


def name(lenght):
    first_part_lenght = random.randint(2, lenght - 2)
    second_part_lenght = lenght - first_part_lenght - 1
    first_part = ''
    first_part += random.choice(string.ascii_letters)
    first_part += random.choice(string.digits)
    for _ in range(2, first_part_lenght):
        letter = random.choice(string.ascii_letters + string.digits)
        while letter.lower() in first_part.lower():
            letter = random.choice(string.ascii_letters + string.digits)
        first_part += letter
    first_part = first_part[0] + ''.join(random.sample(list(first_part[1:]), len(list(first_part[1:]))))
    second_part = ''
    letter = random.choice(string.ascii_uppercase[:13])
    while letter.lower() in first_part.lower():
        letter = random.choice(string.ascii_uppercase[:13])
    second_part += letter
    for _ in range(1, second_part_lenght):
        letter = random.choice(string.ascii_lowercase)
        while letter.lower() in second_part.lower() or letter.lower() in first_part.lower():
            letter = random.choice(string.ascii_lowercase)
        second_part += letter
    return first_part + ' ' + second_part

for i in range(5, 30):
    k = name(i)
    if len(set(k)) == len(k):
        print('True')
    else:
        print(k)
        break