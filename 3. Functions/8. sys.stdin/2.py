import sys

o = ['20010', '1000002', '2000001', '1002', '12', '21', '201', '102']

print(min(sys.stdin, key=lambda x: (sum(list(map(int, list(x.strip())))), -len(x.strip()), int(x.strip()))))