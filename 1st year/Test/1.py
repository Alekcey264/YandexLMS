a, b = int(input()), int(input())
n = int(input())
for _ in range(n):
    temp_arr = list()
    nums = list(map(int, input().split()))
    for item in nums:
        if item in range(a, b + 1):
            temp_arr.append(item * 13)
    print(*temp_arr, sep="> ")
