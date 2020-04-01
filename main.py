import sys
import re
from parse_expr import *
from solver import *


@sanitizer
def main(equation: str):
    try:
        degree = get_polynomial_degree(equation)
        split_eq = split_equality(equation)
        coefs = map(lambda eq: parser(eq)(degree["value"]), split_eq)
        result = solver(coefs)

        print("\n".join((degree["message"], result["reduced_form"], result["message"])))

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
