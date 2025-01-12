import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--upper", action="store_true")
parser.add_argument("--lines", metavar="--lines", type=int)
parser.add_argument("source")
parser.add_argument("destination")
args = parser.parse_args()
with open(args.source, "r") as file:
    file_lines = file.readlines()
if not args.lines or args.lines > len(file_lines):
    args.lines = len(file_lines)
if args.upper:
    for i in range(args.lines):
        file_lines[i] = file_lines[i].upper()
with open(args.destination, "w") as file:
    for item in file_lines[:args.lines]:
        file.write(item)
