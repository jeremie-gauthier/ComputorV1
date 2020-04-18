import re
from typing import Pattern
from computor.src.utils import Parallelize


class Error:
    def __init__(self, entry: str):
        self.err = []
        self.entry = entry
        self.len_entry = len(entry)

    def formatting(self) -> None:
        if not self.entry.strip():
            self.err.append("[-] Empty string")
            return
        Parallelize().execute(
            [
                self._count_equal_signs,
                self._forbidden_chars,
                self._coefficients,
                self._operators,
                self._powers,
            ]
        )
        if not self.err:
            self.err.append(
                "\n".join([self.entry, self._wave_all(), "[-] Bad Formatting"])
            )

    def _wave_all(self) -> str:
        return "^" * self.len_entry

    def _wave_at(self, stop: int, wave_len: int = 1) -> str:
        return " " * stop + "^" * wave_len

    def _search_pattern(self, pattern: Pattern, err_msg: str) -> bool:
        err_indicator = [" "] * self.len_entry
        where = re.search(pattern, self.entry)
        last_end = 0
        while where:
            start, end = where.start(), where.end()
            for i in range(end - start):
                err_indicator[last_end + start + i] = "^"
            last_end += end
            where = re.search(pattern, self.entry[last_end:])
        if last_end > 0:
            self.err.append(
                "\n".join([self.entry, "".join(err_indicator), f"[-] {err_msg}"])
            )

    def _count_equal_signs(self) -> None:
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
        self._search_pattern(trailing_op, "Remove trailing operator")

        heading_op = r"^[\+\=\*]"
        self._search_pattern(heading_op, "Remove heading operator")

        missing_op = r"[\dxX]\s+[\dxX]"
        self._search_pattern(missing_op, "Missing operator ?")

    def _forbidden_chars(self) -> None:
        forbid_chars = r"[^\+\-\=\*\d\sxX\^\.]"
        self._search_pattern(forbid_chars, "Forbidden char")

    def _coefficients(self) -> None:
        floats = r"[^\d]\.\d|\d?\.[^\d]|\d*\.\d+\.\d*"
        self._search_pattern(floats, "Float malformed")

    def _powers(self) -> None:
        missing_symbol = r"[xX]\d"
        self._search_pattern(missing_symbol, "Power symbol is missing")
