import sys
import re
from parse_expr import *
from solver import *


def main(arg):
    try:
        numbers = parser(arg)()
        print("numbers =>", numbers)
        result = solver(numbers)
        return 0

    except Exception as e:
        print(f"[-] {e}", file=sys.stderr)
        print(f"[*] Exit", file=sys.stderr)
        return -1


if __name__ == "__main__":
    argc = len(sys.argv)
    if argc == 2:
        main(sys.argv[1])
    else:
        print("[-] Arguments error", file=sys.stderr)
        print("[*] Exit", file=sys.stderr)
        sys.exit(-1)
