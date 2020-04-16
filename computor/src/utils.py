def pgcd(a: int, b: int) -> int:
    if a == b:
        return a
    else:
        if a > b:
            return pgcd(a - b, b)
        else:
            return pgcd(a, b - a)


def is_neg(x: float):
    return x < 0
