import sys


if len(sys.argv) == 3 and sys.argv[1].isnumeric() and sys.argv[2].isnumeric():
    print(int(sys.argv[1]) + int(sys.argv[2]))
else:
    print(0)