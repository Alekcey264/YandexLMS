import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--barbie", metavar="--barbie", type=int, default=50)
parser.add_argument("--cars", metavar="--cars", type=int, default=50)
parser.add_argument("--movie", metavar="--movie", type=str, default="other")
movies = {"melodrama": 0, "other": 50, "football": 100}
args = parser.parse_args()
if args.cars not in range(0, 101):
    args.cars = 50
if args.barbie not in range(0, 101):
    args.barbie = 50
boy_value = int((100 - args.barbie + args.cars + movies[args.movie]) / 3)
girl_value = 100 - boy_value
print(f"boy: {boy_value}")
print(f"girl: {girl_value}")