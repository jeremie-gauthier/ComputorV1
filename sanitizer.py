import re


def sanitize_entry(entry: str) -> str:
    sanitized_entry = entry.strip()

    real = r"\d+(\.\d+)?"
    power = r"[Xx](\^\d+)?"
    nb = fr"{real}((\s*\*\s*)?{power})?"
    sign = r"[\+\-]"
    next_nb = fr"(\s*{sign}\s*{nb})"
    eq = r"\s*\=\s*"
    pattern = fr"^(-?{nb}){next_nb}*{eq}-?{nb}{next_nb}*$"

    if re.match(pattern, sanitized_entry) is None:
        raise Exception("Bad Formatting")

    replacements = [
        (r"(?<=\d)[Xx]", " * X"),
        (r"[Xx](?!\^)", "X^1"),
        (r"(?<=(?<!\^)\d)(?!([Xx])|(\s*\*))", " * X^0"),
        (fr"([\+\-]\s*)?0(\.0+)?\s*\*\s*{power}", ""),
        (r"^\s*\+\s*", ""),
    ]
    for old, new in replacements:
        sanitized_entry = re.sub(old, new, sanitized_entry)
    return sanitized_entry
