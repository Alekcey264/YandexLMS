data = []

num = int(input())
while num != 0:
    divisors = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            if i == int(num / i):
                divisors += 1
            else:
                divisors += 2
    data.append((num, divisors))
    num = int(input())
print(sorted(data, key=lambda x: (x[1], x[0])))