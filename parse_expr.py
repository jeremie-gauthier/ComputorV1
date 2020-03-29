import re
from sanitizer import *


def get_polynomial_degree(func):
    def max_degree(equation):
        pattern_pow = r"(?<=X\^)\d*"
        pows = re.findall(pattern_pow, equation)
        degree = int(max(pows, key=lambda p: int(p)))
        print(f"Polynomial degree: {degree}")
        if degree > 2:
            raise Exception(
                "The polynomial degree is stricly greater than 2, I can't solve."
            )
        return func(equation, degree)

    return max_degree


@sanitizer
@get_polynomial_degree
def parser(equation, degree):
    def get_part():
        parts = re.split(r"\s*=\s*", equation)
        for part in parts:
            yield part
        yield None

    def find_nb(elem):
        nb = float(re.search(r"\d*\.?\d+", elem).group())
        return -nb if elem[0] == "-" else nb

    def find_pow(elem):
        power = re.search(r"(?<=X\^)\d*", elem).group()
        return int(power)

    def get_numbers():
        pattern_nb = r"\d+(\.\d+)?\s*\*\s*[Xx]\^\d+"
        pattern_numbers = fr"(-\s*)?{pattern_nb}"
        parts = get_part()
        part = next(parts)
        numbers = ()
        while part:
            matches = re.finditer(pattern_numbers, part)
            matched_values = [match.group() for _, match in enumerate(matches, start=1)]
            part_numbers = [0.0 for p in range(degree + 1)]
            for nb in matched_values:
                part_numbers[find_pow(nb)] += find_nb(nb)
            numbers = (*numbers, part_numbers)
            part = next(parts)
        return numbers

    return get_numbers
