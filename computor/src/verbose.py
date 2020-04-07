import re
from typing import Union, Tuple

TypeResult = Union[None, Tuple[float, ...]]


def degree(degree):
    return f"Polynomial degree: {degree}"


def reduced_form(reduced: list) -> str:
    string_reduced = " + ".join(
        ["X^".join((val, str(idx))) for idx, val in enumerate(map(str, reduced))]
    )

    # Reduce even more
    replacements = [
        (r"\+ -", "- "),
        (r"\.0 ", " "),
        (r"\.0X", "X"),
        (r"\^1(?!\d)|X\^0", ""),
    ]
    for old, new in replacements:
        string_reduced = re.sub(old, new, string_reduced)

    return f"Reduced form: {string_reduced} = 0"


def delta(delta: float) -> str:
    return f"Δ = {delta}"


def result(delta: float, result: TypeResult) -> str:
    if delta is None:
        return f"The solution is: {result}"
    else:
        if delta < 0:
            return f"""Discriminant is strictly negative, there is no real root.
            \rHowever, it exists two complex solutions:
            \rS1 = {result[0]}\nS2 = {result[1]}"""
        elif delta == 0:
            return f"Discriminant is equal to zero, the only solution is:\n{result[0]}"
        else:
            return f"Discriminant is strictly positive, the two solutions are:\n\
                    \rS1 = {result[0]: .6f}\nS2 = {result[1]: .6f}"
