from typing import List
import re
from sanitizer import *


def get_polynomial_degree(equation: str) -> dict:
    pattern_pow = r"(?<=X\^)\d*"
    pows = re.findall(pattern_pow, equation)
    degree = int(max(pows, key=lambda p: int(p)))
    if degree > 2:
        raise Exception("Can't solve polynomials greater than 2nd degree.")
    elif degree == 0:
        raise Exception("This is not a polynomial, just an equality.")
    return {"value": degree, "message": f"Polynomial degree: {degree}"}


def split_equality(equation: str) -> List[str]:
    return re.split(r"\s*=\s*", equation)


def parser(equation: str):
    def find_nb(elem: str) -> float:
        nb = float(re.search(r"\d*\.?\d+", elem).group())
        return -nb if elem[0] == "-" else nb

    def find_pow(elem: str) -> int:
        power = re.search(r"(?<=X\^)\d*", elem).group()
        return int(power)

    def list_of_zeros(degree: int) -> List[float]:
        return [0.0] * (degree + 1)

    def extract_coef(degree: str) -> List[float]:
        pattern_coef = r"(-\s*)?\d+(\.\d+)?\s*\*\s*[Xx]\^\d+"
        matches = re.finditer(pattern_coef, equation)
        values = map(lambda m: m.group(), matches)
        coefs = list_of_zeros(degree)
        for nb in values:
            coefs[find_pow(nb)] += find_nb(nb)
        return coefs

    return extract_coef
