from concurrent.futures import ThreadPoolExecutor
from typing import List, Any, Callable
from .type_hints import TypeNumber
from functools import partial


class Parallelize:
    def __init__(self, max_workers=None):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self.running_tasks = []

    def execute(self, tasks: List[Callable]) -> None:
        self.running_tasks = [self.executor.submit(task) for task in tasks]

    def get_results(self) -> List[Any]:
        return [task.result() for task in self.running_tasks]


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def is_neg(x: float) -> bool:
    return x < 0


def elegant_number(x: TypeNumber) -> TypeNumber:
    if int(x) == x:
        return int(x)
    return x


six_rounded = partial(round, ndigits=6)
