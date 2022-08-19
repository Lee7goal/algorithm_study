from functools import lru_cache
from typing import Dict, Generator

memo: Dict[int, int] = {0: 0, 1: 1}


def fib(n: int) -> int:
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]


@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:
        return n
    return fib4(n - 1) + fib4(n - 2)


def fib5(n: int) -> int:
    if n == 0: return 0
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next


def fib6(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    yield next


if __name__ == '__main__':
    # 0 1 1 2 3 5
    # print(fib(100))
    # print(fib4(100))
    # print(fib5(100))
    for i in fib6(50):
        print(i)
