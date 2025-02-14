from yandex_testing_lesson import is_palindrome # type: ignore


def is_palindrome_test():
    data = (
        # ('', False),
        ('aba', True),
        ('a', True),
        ('abc', False)
    )
    flag = True
    for input_val, correct_output_val in data:
        try:
            output_val = is_palindrome(input_val)
        except Exception:
            flag = False
        else:
            if output_val != correct_output_val:
                flag = False
    if flag:
        print('YES')
    else:
        print('NO')