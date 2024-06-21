flags = [input() for _ in range(int(input()))]
count = int(input())
for i in range(count):
	print(flags[i % len(flags)])    