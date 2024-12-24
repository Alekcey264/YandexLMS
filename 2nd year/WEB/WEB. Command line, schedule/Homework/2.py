import sys

arguments = sys.argv[1:].split()
strings = []
is_sorted = False
if arguments[0] == "--sort":
    is_sorted = True
    arguments.pop(0)
for item in arguments:
    item = item.split("=")
    strings.append(f"{item[0]}: {item[1]}")

