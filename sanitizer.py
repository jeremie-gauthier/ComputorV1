from typing import Callable, Any
import re


def sanitizer(func: Callable[..., Any]):
    def sanitize_entry(entry: str) -> Any:
        sanitized_entry = entry.strip()

        real = r"\d+(\.\d+)?"
        power = r"[Xx]\^\d+"
        nb = fr"{real}\s*\*\s*{power}"
        sign = r"[\+\-\*\/]"
        next_nb = fr"(\s*{sign}\s*{nb})"
        eq = r"\s*\=\s*"
        pattern = fr"^(-?{nb}){next_nb}*{eq}-?{nb}{next_nb}*$"

        if re.match(pattern, sanitized_entry) is None:
            raise Exception("Bad Formatting")
        return func(sanitized_entry)

    return sanitize_entry
