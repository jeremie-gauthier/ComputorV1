import re
from typing import Any


def vb_degree(degree):
    return f"Polynomial degree: {degree}"


def vb_reduced_form(reduced: list) -> str:
    string_reduced = " + ".join(
        ["X^".join((val, str(idx))) for idx, val in enumerate(map(str, reduced))]
    )

    # Reduce even more
    replacements = [
        (r"\+ -", "- "),
        (r"\.0 ", " "),
        (r"\.0X", "X"),
        (r"\^1|X\^0", ""),
    ]
    for old, new in replacements:
        string_reduced = re.sub(old, new, string_reduced)

    return f"Reduced form: {string_reduced} = 0"


def vb_result(delta: float, result: Any) -> str:
    if delta < 0:
        return "Discriminant is strictly negative, there is no solution"
    elif delta == 0:
        return f"Discriminant is equal to zero, the only solution is:\n{result}"
    else:
        return f"Discriminant is strictly positive, the two solutions are:\n\
                \rS1 = {result[0]: .6f}\nS2 = {result[1]: .6f}"
