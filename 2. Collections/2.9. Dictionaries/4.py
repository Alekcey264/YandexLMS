nums = list(map(int, input().split()))
chars = list()
for num in nums:
    num = bin(num)[2:]
    chars.append({'digits': len(num), 'units': num.count('1'), 'zeros': num.count('0')})
print(chars)