import sys


params = sys.argv[1:]
if params:
    sum = 0
    mult = 1
    for item in params:
        try:
            sum = sum + mult * int
else:
    print("NO PARAMS")