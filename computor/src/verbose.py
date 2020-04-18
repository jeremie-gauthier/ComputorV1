import re
from .type_hints import TypeResult, TypeRetFraction, TypeCoefs


def irreducible_fraction(a: TypeRetFraction, b: TypeRetFraction) -> str:
    if a and b:
        if type(a) == tuple and type(b) == tuple:
            return f"""Irreducible fraction:
                \r\tS1 = {a[0]} / {a[1]}
                \r\tS2 = {b[0]} / {b[1]}\n"""
        else:
            return f"Irreducible fraction:\n\t{a} / {b}\n"
    return ""


def mid_steps_reducer(left: TypeCoefs, right: TypeCoefs):
    left_string = natural_form(reduce_form(left)) if left else "0"
    right_string = natural_form(reduce_form(right)) if right else "0"
    return f"Reduced form: {left_string} = {right_string}"


def degree(degree: int) -> str:
    return f"Polynomial degree: {degree}"


def natural_form(reduced: str) -> str:
    replacements = [
        (r"\.0 ", " "),
        (r"\.0X", "X"),
        (r"\^1(?!\d)|X\^0", ""),
        (r"(?<=\s)1(?=X)", ""),
        (r"^1(?=X)", ""),
    ]
    for old, new in replacements:
        reduced = re.sub(old, new, reduced)
    return reduced


def reduce_form(reduced: TypeCoefs) -> str:
    len_reduced = len(reduced)
    items = sorted(reduced.items(), reverse=True)
    string_reduced = " + ".join(
        [
            "X^".join((str(coef), str(power)))
            for power, coef in items
            if (coef != 0.0 and len_reduced > 1) or len_reduced == 1
        ]
    ).replace("+ -", "- ")
    return string_reduced


def reduced(reduced: TypeCoefs) -> str:
    string_reduced = natural_form(reduce_form(reduced))
    return f"Reduced form: {string_reduced} = 0"


def delta(delta: float) -> str:
    if delta is None:
        return "Δ = No delta found"
    else:
        return f"Δ = {delta}"


def result(delta: float, result: TypeResult) -> str:
    if delta is None:
        return f"""The solution is:
                \r\t{result[0]}
                \rSo:
                \r\t{result[1][0]}"""
    else:
        if delta < 0:
            return f"""Discriminant is strictly negative, there is no real root.
                    \rHowever, it exists two complex solutions:
                    \r\tS1 = {result[0][0]}\n\tS2 = {result[0][1]}
                    \rSo:
                    \r\tS1 = {result[1][0]}\n\tS2 = {result[1][1]}"""
        elif delta == 0:
            return f"""Discriminant is equal to zero, the only solution is:
                    \r\t{result[0][0]}
                    \rSo:
                    \r\t{result[1][0]}"""
        else:
            return f"""Discriminant is strictly positive, the two solutions are:
                    \r\tS1 = {result[0][0]}\n\tS2 = {result[0][1]}
                    \rSo:
                    \r\tS1 = {result[1][0]: .6f}\n\tS2 = {result[1][1]: .6f}"""
