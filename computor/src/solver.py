from typing import List
import re


# To keep the expr as reduced as possible,
# we remove all consecutive biggest coefs that are = 0
def expr_reducer(coefs: map) -> List[float]:
    sub = lambda x, y: x - y
    reduced = list(map(lambda c: sub(*c), zip(*coefs)))
    while len(reduced) > 1 and reduced[-1] == 0:
        reduced = reduced[:-1]
    return reduced


def solver(coefs: List[float], degree: int) -> dict:
    is_neg = lambda x: x < 0

    def get_delta(a: float, b: float, c: float) -> float:
        return b ** 2 - 4 * a * c

    def second_degree() -> dict:
        c, b, a = coefs
        delta = get_delta(a, b, c)
        if delta < 0:
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
        elif delta == 0:
            result = [
                (f"{-b if is_neg(b) else f'-{b}'} / ( 2 * {a} )", None),
                (-b / (2 * a), None),
            ]
        else:
            pre_s1 = f"( {-b if is_neg(b) else f'-{b}'} - √({delta}) ) / ( 2 * {a})"
            pre_s2 = f"( {-b if is_neg(b) else f'-{b}'} + √({delta}) ) / ( 2 * {a})"
            s1 = (-b - delta ** 0.5) / (2 * a)
            s2 = (-b + delta ** 0.5) / (2 * a)
            result = [(pre_s1, pre_s2), (s1, s2)]
        return {"delta": delta, "result": result}

    def first_degree() -> dict:
        b, a = coefs
        result = [f"{-b if is_neg(b) else f'-{b}'} / {a}", -b / a]
        return {"delta": None, "result": result}

    def equality_case() -> dict:
        (n,) = coefs
        observation = f"{n} = 0"
        if n > 0:
            result = f"This is an inequality\n\t{n} > 0"
        elif n < 0:
            result = f"This is an inequality\n\t{n} < 0"
        else:
            result = f"This is an equality\n\tAll reals are possible solutions"
        return {"delta": None, "result": [observation, (result, None)]}

    if degree == 0:
        return equality_case()
    elif degree == 1:
        return first_degree()
    elif degree == 2:
        return second_degree()
