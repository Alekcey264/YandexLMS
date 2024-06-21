num = int(input())
nums = [int("1" * (i + 1)) for i in range(len(str(num)))]
print(*[item ** 2 for item in nums if item < num], sep=", ")

