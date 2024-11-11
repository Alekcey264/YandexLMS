from random import choice


with open('lines.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    if lines:   
        print(choice(lines).strip())