import regex
from .error import Error


def check_entry(entry: str) -> str:
    sanitized = entry.strip()

    real = r"\d+(\.\d+)?"
    power = r"[Xx](\^\d+)?"
    nb = fr"({real}|{power}|({real}\s*\*?\s*{power}))"
    sign = r"[\+\-]"
    next_nb = fr"(\s*{sign}\s*{nb})"
    eq = r"\s*\=\s*"
    pattern = fr"^(-?{nb}){next_nb}*{eq}-?{nb}{next_nb}*$"

    if regex.match(pattern, sanitized) is None:
        err_cls = Error(entry)
        err_cls.formatting()
        raise Exception(err_cls.err)

    replacements = [
        (r"(?<=\d)[Xx]", " * X"),
        (r"[Xx](?!\^)", "X^1"),
        (r"(?<=\=\s*)[xX]", "1 * X"),
        (r"^[xX]", "1 * X"),
        (r"\+(?=\s*[xX])", "+ 1 *"),
        (r"\-(?=\s*[xX])", "- 1 *"),
        (r"(?<=(?<!\^(\d+)?)\d)(?!\d|\.|\s*\*|\s*[xX])", " * X^0"),
        (fr"([\+\-]\s*)?(?<!\d|\.)0(\.0+)?\s*\*\s*{power}", ""),
        (r"^\s*\+\s*", ""),
    ]
    for old, new in replacements:
        sanitized = regex.sub(old, new, sanitized)
    return sanitized
