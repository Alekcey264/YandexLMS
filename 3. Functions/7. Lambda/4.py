min_mass = int(input())
count = int(input())
mass = 0
for _ in range(count):
    for item in filter(lambda x: x >= min_mass, list(map(int, input().split()))):
        mass += item
print(mass)