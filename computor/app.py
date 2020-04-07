import sys
from computor.src import parser, sanitizer, solver, verbose


def run(arg: str) -> int:
    try:
        equation = sanitizer.sanitize_entry(arg)

        # Organize expr to ease computations
        tmp_degree = parser.get_approx_degree(equation)
        split_eq = parser.split_equality(equation)
        coefs = map(lambda eq: parser.parser(eq, tmp_degree), split_eq)

        # Start equation resolution
        reduced_form = solver.expr_reducer(coefs)
        degree = parser.get_real_degree(reduced_form)
        print("\n".join([verbose.reduced_form(reduced_form), verbose.degree(degree)]))
        if degree > 2:
            raise Exception("Can't solve polynomials greater than 2nd degree.")
        elif degree == 0:
            raise Exception("This is not a polynomial, just an equality.")

        delta, result = solver.solver(reduced_form, degree).values()
        print(verbose.result(delta, result))
        return {"status": "Success", "solutions": result}

    except Exception as e:
        print(f"[-] {e}", file=sys.stderr)
        return {"status": "Error"}
