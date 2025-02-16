from yandex_testing_lesson import is_correct_mobile_phone_number_ru


def is_correct_mobile_phone_number_ru_test():
    data = (
        ('+7(900)1234567', True),
        # ('', False),
        # ('+7-922-599-104', True),
        # ('+7(922)599104', True),
        # ('+7(922)59-91-04', True),
        # ('8 922 259 91 04', True),
        # ('+89222599104', False),
        # ('79222599104', False),
        ('6фывячсячсйasdzxczxc', False),
        ('+7)900(1234567', False)
    )
    for input_val, correct_output in data:
        if is_correct_mobile_phone_number_ru(input_val) != correct_output:
            print('NO')
            return
    print('YES')


is_correct_mobile_phone_number_ru_test()