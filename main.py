import sys
import re
from parse_expr import *
from solver import *
from verbose import *


def main(arg: str):
    try:
        equation = sanitize_entry(arg)
        degree = get_polynomial_degree(equation)
        split_eq = split_equality(equation)
        coefs = map(lambda eq: parser(eq, degree), split_eq)
        reduced_form = expr_reducer(coefs)

        delta, result = solver(reduced_form).values()

        print(
            "\n".join(
                (
                    vb_degree(degree),
                    vb_reduced_form(reduced_form),
                    vb_result(delta, result),
                )
            )
        )

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
