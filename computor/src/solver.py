from typing import List
import re
from .utils import is_neg
from .reducer import fraction


def second_degree(coefs: List[float]) -> dict:
    def get_delta(a: float, b: float, c: float) -> float:
        mid_steps = map(
            lambda s: "Δ = " + s, (f"{b}^2 - 4 * {a} * {c}", f"{b**2} - {4 * a * c}"),
        )
        result = b ** 2 - 4 * a * c
        return (result, mid_steps)

    def negative_delta():
        # Complex solutions
        imaginary = ((delta * -1) ** 0.5) / (2 * a)
        real = -b / (2 * a)
        result = [
            (
                f"( {-b if is_neg(b) else f'-{b}'} + i√({-delta}) ) / {2 * a}",
                f"( {-b if is_neg(b) else f'-{b}'} - i√({-delta}) ) / {2 * a}",
            ),
            (
                f"{real} + {imaginary} * i".replace("+ -", "- "),
                f"{real} - {imaginary} * i".replace("- -", "+ "),
            ),
            None,  # irreducible
        ]
        return result

    def nullish_delta():
        irreducible = fraction(-b, 2 * a)
        result = [
            (f"{-b if is_neg(b) else f'-{b}'} / ( 2 * {a} )", None),
            (-b / (2 * a), None),
            irreducible,
        ]
        return result

    def positive_delta():
        pre_s1 = f"( {-b if is_neg(b) else f'-{b}'} - √({delta}) ) / ( 2 * {a} )"
        pre_s2 = f"( {-b if is_neg(b) else f'-{b}'} + √({delta}) ) / ( 2 * {a} )"
        s1 = (-b - delta ** 0.5) / (2 * a)
        irr_s1 = fraction((-b - delta ** 0.5), (2 * a))
        s2 = (-b + delta ** 0.5) / (2 * a)
        irr_s2 = fraction((-b + delta ** 0.5), (2 * a))
        result = [(pre_s1, pre_s2), (s1, s2), (irr_s1, irr_s2)]
        return result

    c, b, a = [coefs.get(c, 0) for c in range(3)]
    delta, mid_steps = get_delta(a, b, c)
    if delta > 0:
        result = positive_delta()
    elif delta == 0:
        result = nullish_delta()
    else:
        result = negative_delta()
    return {"delta": delta, "result": result, "steps_to_delta": mid_steps}


def first_degree(coefs: List[float]) -> dict:
    b, a = [coefs.get(c, 0) for c in range(2)]
    formula = f"{-b if is_neg(b) else f'-{b}'} / {a}"
    result = (-b / a, None)
    irreducible = fraction(-b, a)
    return {
        "delta": None,
        "result": [formula, result, irreducible],
        "steps_to_delta": None,
    }


def zero_degree(coefs: List[float]) -> dict:
    n = coefs.get(0, 0)
    observation = f"{n} = 0"
    if n == 0:
        result = f"All reals are possible solutions"
    else:
        result = f"There is no solution"
    return {
        "delta": None,
        "result": [observation, (result, None), (None, None)],
        "steps_to_delta": None,
    }


def solver(coefs: List[float], degree: int) -> dict:
    try:
        return [zero_degree, first_degree, second_degree][degree](coefs)
    except IndexError:
        raise Exception("Can't solve polynomials greater than 2nd degree.")
