try:
    password = input()
    small = False
    big = False
    letter = False
    num = False
    forbitten_strings = {'qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ', 
                         'фывапролджэё', 'ячсмитьбю', '1234567890'}
    assert len(password) > 8
    for item in password:
        if small and big and letter and num:
            break
        else:
            if item.islower() and not small:
                small = True
            if item.isupper() and not big:
                big = True
            if item.isalpha() and not letter:
                letter = True
            if item.isnumeric() and not num:
                num = True
    assert small and big and letter and num
    password = password.lower()
    for i in range(len(password) - 2):
        for item in forbitten_strings:
            assert password[i:i + 3] not in item
    print('ok')
except AssertionError:
    print('error')
except Exception:
    print('error')