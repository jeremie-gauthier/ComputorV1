from typing import List
import re


def is_neg(x: float):
    return x < 0


def second_degree(coefs: List[float]) -> dict:
    def get_delta(a: float, b: float, c: float) -> float:
        return b ** 2 - 4 * a * c

    def positive_delta():
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
        ]
        return result

    def nullish_delta():
        result = [
            (f"{-b if is_neg(b) else f'-{b}'} / ( 2 * {a} )", None),
            (-b / (2 * a), None),
        ]
        return result

    def negative_delta():
        pre_s1 = f"( {-b if is_neg(b) else f'-{b}'} - √({delta}) ) / ( 2 * {a} )"
        pre_s2 = f"( {-b if is_neg(b) else f'-{b}'} + √({delta}) ) / ( 2 * {a} )"
        s1 = (-b - delta ** 0.5) / (2 * a)
        s2 = (-b + delta ** 0.5) / (2 * a)
        result = [(pre_s1, pre_s2), (s1, s2)]
        return result

    c, b, a = [coefs.get(c, 0) for c in range(3)]
    delta = get_delta(a, b, c)
    if delta < 0:
        result = positive_delta()
    elif delta == 0:
        result = nullish_delta()
    else:
        result = negative_delta()
    return {"delta": delta, "result": result}


def first_degree(coefs: List[float]) -> dict:
    b, a = [coefs.get(c, 0) for c in range(2)]
    formula = f"{-b if is_neg(b) else f'-{b}'} / {a}"
    result = (-b / a, None)
    return {"delta": None, "result": [formula, result]}


def zero_degree(coefs: List[float]) -> dict:
    n = coefs.get(0, 0)
    observation = f"{n} = 0"
    if n == 0:
        result = f"All reals are possible solutions"
    else:
        result = f"There is no solution"
    return {"delta": None, "result": [observation, (result, None)]}


def solver(coefs: List[float], degree: int) -> dict:
    try:
        return [zero_degree, first_degree, second_degree][degree](coefs)
    except IndexError:
        raise Exception("Can't solve polynomials greater than 2nd degree.")
