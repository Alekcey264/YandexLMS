try:
    new_n = input().strip().replace(' ', '')
    number = '+'
    our = False
    if new_n[0] == "+" or new_n[0] == '8' or new_n[:4] == "+359" or new_n[:3] == "+55" or new_n[:2] == "+1":
        if (new_n[0] == '8' or new_n[:2] == '+7'):
            our = True
            if new_n[0] == '8':    
                new_n = '7' + new_n[1:]
            elif new_n[:2] == "+7":
                new_n = new_n[1:]
            for letter in new_n:
                if letter in [')', '(', '+', '-', ' ', '	'] or letter.isnumeric():
                    number += letter
                else:
                    raise ValueError
        elif new_n[:4] == "+359" or new_n[:3] == "+55" or new_n[:2] == "+1":
            new_n = new_n[1:]
            for letter in new_n:
                if letter in [')', '(', '+', '-', ' ', '	'] or letter.isnumeric():
                    number += letter
                else:
                    raise ValueError
        else:
            raise NameError
    count = 0
    skobs = [list(), 0]
    if number.count(')') != number.count('(') or '--' in number or number[-1] == '-':
        raise ValueError
    if (number[0] == '8' or number[:2] == '+7' or number[:4] == "+359" or number[:3] == "+55" or number[:2] == "+1"):
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
    number = '+' + ''.join([item if item.isnumeric() else '' for item in number])
    opers = [range(910, 920), range(980, 990), range(920, 940),
             range(920, 940), range(902, 907), range(960, 970)]
    if count == 11:
        if our:
            for item in opers:
                if int(number[2:5]) in item:
                    print(number)
                    exit()
            else:
                raise TabError
        else:
            print(number)
    else:
        raise TypeError
except ValueError:
    print('неверный формат')
except TypeError:
    print('неверное количество цифр')
except TabError:
    print('не определяется оператор сотовой связи')
except NameError:
    print('не определяется код страны')