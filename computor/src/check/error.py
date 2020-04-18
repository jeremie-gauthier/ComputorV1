import re
from typing import Pattern
from computor.src.utils import Parallelize


class Error:
    def __init__(self, entry: str):
        self.err = []
        self.entry = entry

    def formatting(self) -> None:
        Parallelize().execute(
            [
                self._count_equal_signs,
                self._forbidden_chars,
                self._coefficients,
                self._operators,
            ]
        )

    def _wave_all(self) -> str:
        return "^" * len(self.entry)

    def _wave_at(self, stop: int, wave_len: int = 1) -> str:
        return " " * stop + "^" * wave_len

    def _search_pattern(self, pattern: Pattern, err_msg: str) -> bool:
        where = re.search(pattern, self.entry)
        if where:
            start = where.start()
            len_err = where.end() - start
            self.err.append(
                "\n".join(
                    [
                        self.entry,
                        self._wave_at(start, wave_len=len_err),
                        f"[-] {err_msg}",
                    ]
                )
            )

    def _count_equal_signs(self) -> bool:
        nb_eq = self.entry.count("=")
        if nb_eq > 1:
            self._search_pattern(r"=", "There are two or much equal sign")
        elif nb_eq == 0:
            self.err.append(
                "\n".join([self.entry, self._wave_all(), "[-] Equal sign is missing"])
            )

    def _operators(self) -> None:
        eq_neg_op = r"\=\s*\-\s+[\dxX]"
        self._search_pattern(eq_neg_op, "Stick the operand to the coefficient")

        double_op = r"[\+\-\*]\s*[\+\-\*\=]|\=\s*[\+\*]"
        self._search_pattern(double_op, "Operators conflict")

        trailing_op = r"[\-\+\=\*]$"
        self._search_pattern(trailing_op, "Please remove trailing operator")

        heading_op = r"^[\+\=\*]"
        self._search_pattern(heading_op, "Please remove heading operator")

    def _forbidden_chars(self) -> bool:
        forbid_chars = r"[^\+\-\=\*\d\sxX\^\.]"
        self._search_pattern(forbid_chars, "Forbidden char")

    def _coefficients(self) -> bool:
        floats = r"[^\d]\.\d|\d\.[^\d]|\d*\.\d+\.\d*"
        self._search_pattern(floats, "Float malformed")
