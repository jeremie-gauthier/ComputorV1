import sys
from computor.src import parser, sanitizer, solver, verbose, reducer


def run(arg: str) -> int:
    try:
        equation = sanitizer.sanitize_entry(arg)

        # Organize expr to ease computations
        split_eq = parser.split_equality(equation)
        coefs = map(lambda eq: parser.parser(eq), split_eq)

        # Start equation resolution
        reduced_form = reducer.expression(coefs)
        degree = parser.get_degree(reduced_form)
        print("\n".join([verbose.reduced_form(reduced_form), verbose.degree(degree)]))
        delta, result = solver.solver(reduced_form, degree).values()
        print("\n".join([verbose.delta(delta), verbose.result(delta, result)]))
        return {"status": "Success", "solutions": result[1]}

    except Exception as e:
        print(f"[-] {e}", file=sys.stderr)
        return {"status": "Error"}
