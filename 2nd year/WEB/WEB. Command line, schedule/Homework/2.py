import sys


arguments = sys.argv[1:]
strings = []
is_sorted = False
if "--sort" in arguments:
    is_sorted = True
    arguments.remove("--sort")
for item in arguments:
    item = item.split("=")
    strings.append((item[0], item[1]))
if is_sorted:
    strings.sort(key=lambda x: x[0])
for item in strings:
    print(f"Key: {item[0]} Value: {item[1]}")