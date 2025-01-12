import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--sort", action="store_true")
parser.add_argument("items", nargs="*")
args = parser.parse_args()
values = dict()
for item in args.items:
    item = item.split("=")
    values[item[0]] = item[1]
values = list(values.items())
if args.sort:
    values.sort(key=lambda x: x[0])
[print(f"Key: {item[0]}\tValue: {item[1]}") for item in values]