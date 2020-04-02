import sys
import re
from parse_expr import *
from solver import *
from verbose import *


def main(arg: str) -> int:
    try:
        equation = sanitize_entry(arg)
        # approximation of the degree, based on parsing
        tmp_degree = get_approx_degree(equation)
        split_eq = split_equality(equation)
        coefs = map(lambda eq: parser(eq, tmp_degree), split_eq)
        reduced_form = expr_reducer(coefs)
        # real degree, based on calculations
        degree = get_real_degree(reduced_form)
        delta, result = solver(reduced_form, degree).values()
        print(
            "\n".join(
                (
                    vb_reduced_form(reduced_form),
                    vb_degree(degree),
                    vb_result(delta, result),
                )
            )
        )
        return {"status": "Success", "solutions": result}
    except Exception as e:
        print(f"[-] {e}", file=sys.stderr)
        return {"status": "Error"}


if __name__ == "__main__":
    argc = len(sys.argv)
    if argc == 2:
        if main(sys.argv[1])["status"] == "Error":
            sys.exit("[*] Exit")
    else:
        print("[-] Arguments error", file=sys.stderr)
        sys.exit("[*] Exit")
