import sys
import re
from parse_expr import *
from solver import *


def main(arg):
    try:
        numbers = parser(arg)()
        result = solver(numbers)
        return 0
    except Exception as e:
        print(f"[-] {e}", file=sys.stderr)
        return -1


if __name__ == "__main__":
    argc = len(sys.argv)
    if argc == 2:
        if main(sys.argv[1]) < 0:
            sys.exit("[*] Exit")
    else:
        print("[-] Arguments error", file=sys.stderr)
        sys.exit("[*] Exit")
