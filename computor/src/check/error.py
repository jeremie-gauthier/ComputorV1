import re
from typing import Pattern


class Error:
    def __init__(self, entry: str):
        self.err = ""
        self.entry = entry

    def formatting(self) -> None:
        if any(
            [
                self._count_equal_signs(),
                self._operators(),
                self._forbidden_chars(),
                self._coefficients(),
            ]
        ):
            self.err = "\n".join([self.entry, self.err])
        else:
            self.err = "\n".join([self.entry, "[-] Bad Formatting"])

    def _wave_all(self) -> str:
        return "^" * len(self.entry)

    def _wave_at(self, stop: int, wave_len: int = 1) -> str:
        return " " * stop + "^" * wave_len

    def _search_pattern(self, pattern: Pattern, err_msg: str) -> bool:
        where = re.search(pattern, self.entry)
        if where:
            start = where.start()
            len_err = where.end() - start
            self.err = "\n".join(
                [self._wave_at(start, wave_len=len_err), f"[-] {err_msg}"]
            )
            return True
        return False

    def _count_equal_signs(self) -> bool:
        nb_eq = self.entry.count("=")
        if nb_eq > 1:
            idx = self.entry.rindex("=")
            self.err = "\n".join(
                [self._wave_at(idx), "There are two or much equal sign"]
            )
            return True
        elif nb_eq == 0:
            self.err = "\n".join([self._wave_all(), "Equal sign is missing"])
            return True
        return False

    def _operators(self) -> bool:
        eq_neg_op = r"\=\s*\-\s+[\dxX]"
        if self._search_pattern(eq_neg_op, "Stick the operand to the coefficient"):
            return True

        double_op = r"[\+\-\*]\s*[\+\-\*\=]|\=\s*[\+\*]"
        if self._search_pattern(double_op, "Operators conflict"):
            return True

        trailing_op = r"[\-\+\=\*]$"
        if self._search_pattern(trailing_op, "Please remove trailing operator"):
            return True

        heading_op = r"^[\+\=\*]"
        if self._search_pattern(heading_op, "Please remove heading operator"):
            return True

        return False

    def _forbidden_chars(self) -> bool:
        forbid_chars = r"[^\+\-\=\*\d\sxX\^\.]"
        if self._search_pattern(forbid_chars, "Forbidden char"):
            return True
        return False

    def _coefficients(self) -> bool:
        floats = r"[^\d]\.\d|\d\.[^\d]"
        if self._search_pattern(floats, "Float malformed"):
            return True
        return False
