text = input()
for i in range(1, len(text) // 2 + 1):
    num = text.count(text[:i])
    if num > 1:
        print(f"{text[:i]}: {num}")
