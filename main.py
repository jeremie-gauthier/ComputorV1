import sys
import re
from parse_expr import *
from solver import *
from verbose import *


def main(arg: str) -> int:
    try:
        equation = sanitize_entry(arg)

        # Organize expr to ease computations
        tmp_degree = get_approx_degree(equation)
        split_eq = split_equality(equation)
        coefs = map(lambda eq: parser(eq, tmp_degree), split_eq)

        # Start equation resolution
        reduced_form = expr_reducer(coefs)
        degree = get_real_degree(reduced_form)
        print("\n".join([vb_reduced_form(reduced_form), vb_degree(degree)]))
        if degree > 2:
            raise Exception("Can't solve polynomials greater than 2nd degree.")
        elif degree == 0:
            raise Exception("This is not a polynomial, just an equality.")

        delta, result = solver(reduced_form, degree).values()
        print(vb_result(delta, result))
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
