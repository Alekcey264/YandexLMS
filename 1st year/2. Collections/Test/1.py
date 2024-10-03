n = int(input())
strings = set()
for _ in range(n):
    s = input()
    m = int(input())
    k = int(input())
    strings.add(s[:m:k])
print(*strings, sep="\n")