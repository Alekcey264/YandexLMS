def pass_check(password: str):
    small = False
    big = False
    letter = False
    num = False
    forbitten_strings = {'qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ', 
                         'фывапролджэё', 'ячсмитьбю', '1234567890'}
    if len(password) <= 8:
        return 'error'
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
    if not (small and big and letter and num):
        return 'error'
    password = password.lower()
    for i in range(len(password) - 2):
        for item in forbitten_strings:
            if password[i:i + 3] in item:
                return 'error'
    return 'ok'


print(pass_check(input()))
