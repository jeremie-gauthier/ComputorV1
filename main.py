import sys
import re


def sanitize_entry(arg):
    proper_arg = arg.strip()
    check_pattern = r"((\d*\.?\d+\s*\*\s*[Xx]\^[0-2])(\s*([\-\+\*\/]|\=)\s*)?)"
    if re.match(check_pattern, proper_arg) is None:
        return None
    if proper_arg.count("=") != 1:
        return None
    return proper_arg


def parse_equation(equation):
    def find_nb(elem):
        nb = float(re.search(pattern_number, elem).group())
        return -nb if elem[0] == "-" else nb

    pattern_numbers = (
        r"(-\s)?-\s*\d*\.?\d+\s*\*\s*[Xx]\^[0-2]|\d*\.?\d+\s*\*\s*[Xx]\^[0-2]"
    )
    left_matches = re.finditer(pattern_numbers, equation[0])
    left = [match.group() for _, match in enumerate(left_matches, start=1)]
    right_matches = re.finditer(pattern_numbers, equation[1])
    right = [match.group() for _, match in enumerate(right_matches, start=1)]
    pattern_number = r"\d*\.?\d+"
    return {
        "left": [find_nb(elem) for elem in left],
        "right": [find_nb(elem) for elem in right],
    }


def solve_equation(numbers):
    def put_terms_to_left():
        for i in range(len(numbers["right"])):
            numbers["left"][i] -= numbers["right"][i]
        numbers["right"] = []

    # b^2 - 4ac
    def get_delta():
        return b ** 2 - 4 * a * c

    put_terms_to_left()
    a, b, c = numbers["left"][::-1]
    delta = get_delta()
    if delta < 0:
        print("Discriminant is strictly negative, there is no solution")
        return None
    elif delta == 0:
        s = -b / 2 * a
        print("Discriminant is equal to zero, the only solution is:")
        print(s)
        return s
    else:
        s1, s2 = ((-b - delta ** 0.5) / (2 * a), (-b + delta ** 0.5) / (2 * a))
        print("Discriminant is strictly positive, the two solutions are:")
        print(f"S1 = {s1: .6f}\nS2 = {s2: .6f}")
        return (s1, s2)


def main(arg):
    proper_arg = sanitize_entry(arg)
    if proper_arg is None:
        print("[-] Format error\nExit", file=sys.stderr)
        sys.exit(-1)
    equation = re.split(r"\s*=\s*", proper_arg)
    numbers = parse_equation(equation)
    result = solve_equation(numbers)


if __name__ == "__main__":
    argc = len(sys.argv)
    if argc == 2:
        main(sys.argv[1])
    else:
        print("[-] Arguments error\nExit", file=sys.stderr)
        sys.exit(-1)
