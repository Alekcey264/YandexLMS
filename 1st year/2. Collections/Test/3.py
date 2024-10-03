n = int(input())
for _ in range(n):
    first_string = set(input().split())
    second_string = set(input().split())
    unit = list(first_string & second_string)
    unit = [item for item in unit if int(item) in range(10, 100)]
    unit.sort(reverse=True)
    print(*unit, sep=": ")