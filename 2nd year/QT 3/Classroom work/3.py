number = input().strip().replace(' ', '')
count = 0
skobs = [list(), 0]
try:
    if (number[0] == '8' or number[:2] == '+7') and '--' not in number and number[-1] != '-':
        for letter in number:
            if skobs[1] > 2:
                raise ValueError
            else:
                if letter == '(':
                    skobs[0].append(letter)
                    skobs[1] += 1
                    continue
                elif letter == ')':
                    if len(skobs[0]) == 0:
                        raise ValueError
                    skobs[0].pop()
                    skobs[1] += 1
                    continue
            if letter.isnumeric():
                count += 1
    if count == 11 and len(skobs[0]) == 0:
        if number[0] == '8':
            number = '7' + number[1:]
        print('+' + ''.join([item if item.isnumeric() else '' for item in number]))
    else:
        raise TypeError
except ValueError:
    print('неверный формат')
except TypeError:
    print('неверное количество цифр')
