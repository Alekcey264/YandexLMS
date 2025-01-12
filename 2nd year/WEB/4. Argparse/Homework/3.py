import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("--count", action="store_true")
parser.add_argument("--num", action="store_true")
parser.add_argument("--sort", action="store_true")
parser.add_argument("file_name", default=None)
args = parser.parse_args()
if args.file_name and os.path.isfile(args.file_name):
    with open(args.file_name, 'r') as file:
        lines = file.read().split("\n")
    if args.sort:
        lines.sort()
    if args.num:
        lines = [f"{i} {lines[i]}" for i in range(len(lines))]
    if args.count:
        lines.append(f"rows count: {len(lines)}")
    print(*lines, sep="\n")
else:
    print("ERROR")