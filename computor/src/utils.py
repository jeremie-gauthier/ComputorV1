from concurrent.futures import ThreadPoolExecutor
from typing import List, Any, Callable


class Parallelize:
    def __init__(self):
        self.executor = ThreadPoolExecutor(max_workers=4)
        self.running_tasks = []

    def execute(self, tasks: List[Callable]) -> None:
        for task in tasks:
            self.running_tasks.append(self.executor.submit(task))

    def get_results(self) -> List[Any]:
        return [task.result() for task in self.running_tasks]


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def is_neg(x: float) -> bool:
    return x < 0
