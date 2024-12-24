import sys


params = sys.argv[1:]
if params:
    sum = 0
    mult = 1
    try:
        for item in params:
            if item.isnumeric():
                sum = sum + mult * int(item)
                mult *= -1
            else:
                raise ValueError
        print(sum)
    except ValueError as e:
        print("ValueError")
else:
    print("NO PARAMS")