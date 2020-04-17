import sys
from computor.src import parser, sanitizer, solver, verbose, reducer


def run(entry: str, opt_verbose: bool = False) -> int:
    try:
        equation = sanitizer.sanitize_entry(entry)

        # Organize expr to ease computations
        split_eq = parser.split_equality(equation)
        coefs = map(lambda eq: parser.parser(eq), split_eq)

        # Start equation resolution
        reduced_form, mid_steps = reducer.expression(coefs, opt_verbose)
        if opt_verbose:
            print("\n".join(mid_steps))
        degree = parser.get_degree(reduced_form)
        print("\n".join([verbose.reduced_form(reduced_form), verbose.degree(degree)]))
        delta, result, mid_steps = solver.solver(reduced_form, degree).values()
        if opt_verbose and mid_steps is not None:
            print("\n".join(mid_steps))
        print("\n".join([verbose.delta(delta), verbose.result(delta, result)]))
        if opt_verbose:
            irr_form = verbose.irreducible_fraction(*result[2])
            if irr_form:
                print(irr_form)
        return {"status": "Success", "solutions": result[1]}

    except Exception as e:
        print(f"[-] {e}", file=sys.stderr)
        return {"status": "Error"}
