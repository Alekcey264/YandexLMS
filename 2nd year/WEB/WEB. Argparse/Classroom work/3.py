import argparse


def count_lines(file_path: str):
    try:
        with open(file_path, "r") as file:
            print(len(file.readlines()))
    except Exception:
        print(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", metavar="--file")
    args = parser.parse_args()
    print(count_lines(args.file))