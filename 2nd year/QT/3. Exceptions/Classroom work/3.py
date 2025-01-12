try:
    new_number = input().strip().replace(' ', '')
    number = '+'
    if (new_number[0] == '8' or new_number[:2] == '+7'):
        if new_number[0] == '8':    
            new_number = '7' + new_number[1:]
        elif new_number[:2] == "+7":
            new_number = new_number[1:]
        for letter in new_number:
            if letter in [')', '(', '+', '-', ' ', '	'] or letter.isnumeric():
                number += letter
            else:
                raise ValueError
    else:
        raise ValueError
    count = 0
    skobs = [list(), 0]
    if number.count(')') != number.count('(') or '--' in number or number[-1] == '-':
        raise ValueError
    if (number[0] == '8' or number[:2] == '+7'):
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
    else:
        raise ValueError
    if count == 11:
        print('+' + ''.join([item if item.isnumeric() else '' for item in number]))
    else:
        raise TypeError
except ValueError:
    print('неверный формат')
except TypeError:
    print('неверное количество цифр')
