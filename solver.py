from typing import List
from operator import sub
import re


def expr_reducer(coefs: map) -> List[float]:
    return list(map(lambda c: sub(*c), zip(*coefs)))


def solver(coefs: List[float]) -> dict:
    def get_delta(a, b, c):
        return b ** 2 - 4 * a * c

    def second_degree():
        c, b, a = coefs
        delta = get_delta(a, b, c)
        if delta < 0:
            result = None
        elif delta == 0:
            result = -b / 2 * a
        else:
            s1 = (-b - delta ** 0.5) / (2 * a)
            s2 = (-b + delta ** 0.5) / (2 * a)
            result = (s1, s2)
        return {"delta": delta, "result": result}

    return second_degree()
