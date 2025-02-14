# from yandex_testing_lesson import is_prime  # type: ignore

def is_prime(n): 
    for divisor in range(2, int(n ** 0.5)):
        if n % divisor == 0: 
            return False 
    return True


def is_prime_test():
    data = (
        (2, True),
        (4, False),
        (5, True)
    )
    for input_val, correct_output_val in data:
        if is_prime(input_val) != correct_output_val:
            print('NO')
            return
    print('YES')


is_prime_test()