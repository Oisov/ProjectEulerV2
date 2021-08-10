import functools
import itertools


@functools.cache
def nth_fibonacci(n):
    if n in [0, 1]:
        return n
    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)


def fibonacci():
    n = 0
    while True:
        yield nth_fibonacci(n)
        n += 1


def takewhile(
    iterable=None,
    function=None,
    predicate=None,
    break_condition=None,
    start=0,
    end=None,
):
    if function is not None and iterable is not None:
        raise ValueError("Only one iterator allowed, choose iterable, or functionction")
    elif function is not None:
        iterable = (
            _takewhile_fun(function, start)
            if end is None
            else _takewhile_fun_range(function, start, end)
        )

    if iterable is None:
        iterable = (
            itertools.count(start=start, step=1) if end is None else range(start, end)
        )

    if predicate is None:
        predicate = lambda index, value: True

    if break_condition is None:
        break_condition = lambda index, value: False

    return _takewhile(iterable, predicate, break_condition)


def _takewhile_fun(function, start):
    i = start
    while True:
        yield function(i)
        i += 1


def _takewhile_fun_range(function, start, end):
    for i in range(start, end):
        yield function(i)


def _takewhile(iterable, predicate, break_condition):
    for index, value in enumerate(iterable):
        if break_condition(index, value):
            break
        if predicate(index, value):
            yield value


def PE_002_recursive_v2(limit=4 * 10 ** 6):
    is_even = lambda i, val: val % 2 == 0
    is_over_limit = lambda i, val: val >= limit
    even_fibs_under_limit = _takewhile(
        iterable=fibonacci(), predicate=is_even, break_condition=is_over_limit
    )
    return sum(even_fibs_under_limit)


def PE_002_recursive(limit=4 * 10 ** 6):
    total = 0
    for fib in fibonacci():
        if fib > limit:
            break
        if fib % 2 == 0:
            total += fib
    return total


if __name__ == "__main__":

    print(PE_002_recursive_v2())
