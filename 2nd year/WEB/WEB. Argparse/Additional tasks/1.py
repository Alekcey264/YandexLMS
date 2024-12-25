import argparse


def print_error(message: str):
    print(f"ERROR: {message}!!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("message")
    args = parser.parse_args()
    print("Welcome to my program")
    print_error(args.message)