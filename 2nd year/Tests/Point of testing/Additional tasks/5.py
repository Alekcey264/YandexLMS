import sys


def is_correct_mobile_phone_ru():
    s = list(map(str.strip, sys.stdin))[0]
    if s.startswith('8'):
        s = s[1:]
    elif s.startswith('+7'):
        s = s[2:]
    else:
        print('NO')
        return
    scobs = []
    if '(' in s and s.count('(') + s.count(')') != 2:
        print('NO')
        return
    for letter in s:
        if letter == '(':
            scobs.append(letter)
        elif letter == ')':
            if scobs and scobs[-1] == '(':
                scobs.pop()
            else:
                print('NO')
                return
    if scobs:
        print('NO')
        return
    s = s.replace('-', '').replace(' ', '').replace(')', '').replace('(', '')
    if s.isnumeric():
        print('YES')
    else:
        print('NO')
    return


is_correct_mobile_phone_ru()