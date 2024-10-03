divisors = dict()


def number_of_divisors(num):
    if num not in divisors.keys():
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                if i == int(num / i):
                    divisors[num] = divisors.get(num, 0) + 1
                else:
                    divisors[num] = divisors.get(num, 0) + 2
    return divisors[num]

print(number_of_divisors(36))

print(divisors)