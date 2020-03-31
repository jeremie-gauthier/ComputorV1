import re
from sanitizer import *


def get_polynomial_degree(equation):
    pattern_pow = r"(?<=X\^)\d*"
    pows = re.findall(pattern_pow, equation)
    degree = int(max(pows, key=lambda p: int(p)))
    if degree > 2:
        raise Exception("Can't solve polynomials greater than 2nd degree.")
    elif degree == 0:
        raise Exception("This is not a polynomial, just an equality.")
    return degree


def split_equality(equation):
    return re.split(r"\s*=\s*", equation)


def parser(equation):
    def find_nb(elem):
        nb = float(re.search(r"\d*\.?\d+", elem).group())
        return -nb if elem[0] == "-" else nb

    def find_pow(elem):
        power = re.search(r"(?<=X\^)\d*", elem).group()
        return int(power)

    def list_of_zeros(degree):
        return [0.0] * (degree + 1)

    def extract_coef(degree):
        pattern_coef = r"(-\s*)?\d+(\.\d+)?\s*\*\s*[Xx]\^\d+"
        matches = re.finditer(pattern_coef, equation)
        values = map(lambda m: m.group(), matches)
        coefs = list_of_zeros(degree)
        for nb in values:
            coefs[find_pow(nb)] += find_nb(nb)
        return coefs

    return extract_coef
