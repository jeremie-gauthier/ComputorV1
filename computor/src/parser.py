from typing import List
import re


def get_approx_degree(equation: str) -> int:
    pows = re.findall(r"(?<=[Xx]\^)\d*", equation)
    if pows:
        degree = int(max(pows, key=lambda p: int(p)))
    else:
        degree = 0
    return degree


def get_real_degree(coefs: List[float]) -> int:
    degree = len(coefs) - 1
    if degree == -1:
        return 0
    return degree


def split_equality(equation: str) -> List[str]:
    return re.split(r"\s*=\s*", equation)


def parser(equation: str, degree: int) -> List[float]:
    def find_nb(elem: str) -> float:
        nb = float(re.search(r"\d+(\.\d+)?", elem).group())
        return -nb if elem[0] == "-" else nb

    def find_pow(elem: str) -> int:
        power = re.search(r"(?<=[Xx]\^)\d*", elem).group()
        return int(power)

    def list_of_zeros() -> List[float]:
        return [0.0] * (degree + 1)

    def extract_coefs():
        pattern_coef = r"(-\s*)?\d+(\.\d+)?\s*\*\s*[Xx]\^\d+"
        matches = re.finditer(pattern_coef, equation)
        return map(lambda m: m.group(), matches)

    raw_coefs = extract_coefs()
    coefs = list_of_zeros()
    for rc in raw_coefs:
        coefs[find_pow(rc)] += find_nb(rc)
    return coefs
