def gcd(a: int, b: int) -> int:
    if a == b:
        return a
    else:
        if a > b:
            return gcd(a - b, b)
        else:
            return gcd(a, b - a)


def is_neg(x: float):
    return x < 0
