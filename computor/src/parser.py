from typing import List
import re


def get_degree(dict_coefs: dict) -> int:
    return max(dict_coefs) if len(dict_coefs) else 0


def split_equality(equation: str) -> List[str]:
    return re.split(r"\s*=\s*", equation)


def parser(equation: str) -> List[float]:
    def find_nb(elem: str) -> float:
        nb = float(re.search(r"\d+(\.\d+)?", elem).group())
        return -nb if elem[0] == "-" else nb

    def find_pow(elem: str) -> int:
        power = re.search(r"(?<=[Xx]\^)\d*", elem).group()
        return int(power)

    def extract_coefs():
        pattern_coef = r"(-\s*)?\d+(\.\d+)?\s*\*\s*[Xx]\^\d+"
        matches = re.finditer(pattern_coef, equation)
        return map(lambda m: m.group(), matches)

    raw_coefs = extract_coefs()
    coefs = {}
    for rc in raw_coefs:
        power = find_pow(rc)
        if power in coefs:
            coefs[power] += find_nb(rc)
        else:
            coefs[power] = find_nb(rc)
    return coefs
