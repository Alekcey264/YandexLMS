import sys
import os


arguments = sys.argv[1:]
is_count = False
is_num = False
is_sort = False
if "--count" in arguments:
    is_count = True
    arguments.remove("--count")
if "--num" in arguments:
    is_num = True
    arguments.remove("--num")
if "--sort" in arguments:
    is_sort = True
    arguments.remove("--sort")
if arguments:
    file_name = arguments[0]
    if os.path.isfile(file_name):
        with open(file_name, "r") as file:
            strings = file.read().split("\n")
    else:
        print("ERROR")
else:
    print("ERROR")
if is_sort:
    strings.sort()
if is_num:
    for i in range(len(strings)):
        strings[i] = str(i) + " " + strings[i]
if is_count:
    strings.append(f"rows count: {len(strings)}")
[print(item) for item in strings]
