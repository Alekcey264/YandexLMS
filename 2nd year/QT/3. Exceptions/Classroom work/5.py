class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


def check_password(password: str):
    small = False
    big = False
    num = False
    letter = False
    forbitten_strings = {'qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ', 
                         'фывапролджэё', 'ячсмитьбю', '1234567890'}
    if len(password) <= 8:
        raise LengthError
    for item in password:
        if small and big and num:
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
    if ((small and not big) or (big and not small)) or not letter:
        raise LetterError
    if not num:
        raise DigitError
    password = password.lower()
    for i in range(len(password) - 2):
        for item in forbitten_strings:
            if password[i:i + 3] in item:
                raise SequenceError
    return 'ok'


try:
    print(check_password("0392040454"))
except Exception as error:
    print(error.__class__.__name__)