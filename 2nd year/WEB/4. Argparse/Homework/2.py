import argparse
import sys


class ArgumentParserError(Exception): pass

class ThrowingArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise ArgumentParserError(message)


try:
    parser = ThrowingArgumentParser()
    parser.add_argument("int_values", type=int, nargs='*')
    values = parser.parse_args().int_values
except Exception as e:
    print(e.__class__.__name__)

if len(values) == 2:
    print(sum(values))
elif len(values) == 0:
    print("NO PARAMS")
elif len(values) == 1:
    print("TOO FEW PARAMS")
else:
    print("TOO MANY PARAMS")