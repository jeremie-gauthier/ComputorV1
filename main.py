import sys
import re


def sanitize_entry(arg):
    proper_arg = arg.strip()
    check_pattern = r"((\d*\.?\d*\s*\*\s*[Xx]\^[0-2])(\s*([\-\+\*\/]|\=)\s*)?)"
    if re.match(check_pattern, proper_arg) is None:
        return None
    if proper_arg.count("=") != 1:
        return None
    return proper_arg


def parse_equation(equation):
    pattern_numbers = r"\d*\.?\d*\s*\*\s*[Xx]\^[0-2]"
    left = re.findall(pattern_numbers, equation[0])
    right = re.findall(pattern_numbers, equation[1])
    pattern_number = r"\d*\.?\d"
    return {
        "left": [float(re.search(pattern_number, nb).group()) for nb in left],
        "right": [float(re.search(pattern_number, nb).group()) for nb in right],
    }


def solve_equation(numbers):
    def put_terms_to_left():
        for i in range(len(numbers["right"])):
            numbers["left"][i] -= numbers["right"][i]
        numbers["right"] = []

    # b^2 - 4ac
    def get_delta():
        left = numbers["left"]
        return (left[1] ** 2) - (4 * left[2] * left[0])

    put_terms_to_left()
    delta = get_delta()
    print(delta)
    # No solution
    if delta < 0:
        return None
    # -b/2a
    elif delta == 0:
        return -numbers["left"][1] / 2 * numbers["left"][2]
    # (-b - sqrt(delta)) / 2a AND (-b + sqrt(delta)) / 2a
    else:
        pass


def main(arg):
    proper_arg = sanitize_entry(arg)
    if proper_arg is None:
        print("[-] Format error\nExit", file=sys.stderr)
        sys.exit(-1)
    equation = re.split(r"\s*=\s*", proper_arg)
    numbers = parse_equation(equation)
    solve_equation(numbers)


if __name__ == "__main__":
    argc = len(sys.argv)
    if argc == 2:
        main(sys.argv[1])
    else:
        print("[-] Arguments error\nExit", file=sys.stderr)
        sys.exit(-1)

# Regex for "n * X^p"
# \d*\.?\d*\s*\*\s*[Xx]\^[0-2]

# Regex for integrity - combine with a count of '=' (must have only one)
# ((\d*\.?\d*\s*\*\s*[Xx]\^[0-2])(\s*([\-\+\*\/]|\=)\s*)?)
# 1. split le '='
# 2. strim whitespaces
