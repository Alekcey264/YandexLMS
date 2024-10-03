numbers = set()
for num in range(10):
    numbers.add(str(num))
text = set(input())
print(*(numbers - text))
