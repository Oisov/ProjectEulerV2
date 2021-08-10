import math

import timeit
import numpy as np

SQRT5 = math.sqrt(5)
GOLDEN_RATIO = (1 + SQRT5) / 2
LOG_5 = math.log(5, GOLDEN_RATIO) / 6


def largest_even_fib_index(limit):
    "Finds the biggest n such that fibonacci(n) < limit"
    return int(LOG_5 + math.log(limit, GOLDEN_RATIO) / 3)


def fibonacci(n):
    """Returns the nth fibonacci number in sublinear time

    See https://stackoverflow.com/a/48171368/1048781 for details"""

    def fib_inner(n):
        """Returns L[n] and L[n+1]"""
        if n == 0:
            return 2, 1
        m = n >> 1
        u, v = fib_inner(m)
        q = (2, -2)[m & 1]
        u = u * u - q
        v = v * v + q
        if n & 1:
            return v - u, v
        return u, v - u

    m = n >> 1
    u, v = fib_inner(m)
    # F[m]
    f = (2 * v - u) // 5
    if n & 1:
        q = (n & 2) - 1
        return v * f - q
    return u * f


def PE_002(limit=4 * 10 ** 6):
    if limit < 10 ** 25:
        a, b = 0, 2
        while b < limit:
            a, b = b, 4 * b + a
        even_fib_sum = (a + b - 2) // 4
    else:
        n = largest_even_fib_index(limit)
        even_fib_sum = (fibonacci(3 * n + 2) - 1) // 2
    return even_fib_sum


def sum_even_fib_sublinear(limit=4 * 10 ** 6):
    n = largest_even_fib_index(limit)
    return (fibonacci(3 * n + 2) - 1) // 2


def sum_even_fib_fast(limit):
    a, b = 0, 2
    while b < limit:
        a, b = b, 4 * b + a
    return (a + b - 2) // 4


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def sum_even_fib_naive(limit):
    a, b, total = 0, 1, 0
    while a <= limit:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total


if __name__ == "__main__":

    for lim in range(1, 10 ** 6):
        fsum = sum_even_fib_naive(lim)
        fsum_fast = sum_even_fib_sublinear(lim)
        if fsum != fsum_fast:
            print(lim, fsum, fsum_fast, LOG_5 + math.log(lim, GOLDEN_RATIO) / 3)

#     num = 10 ** 3
#     rep = 100
#     print(f" Power    Naive      Fast    Sublinear")
#     for power in range(0, 50, 5):
#         limit = 4 * 10 ** power
#
#         reps1 = timeit.repeat(
#             repeat=rep,
#             number=num,
#             stmt=f"sum_even_fib_naive({limit})",
#             setup="from __main__ import sum_even_fib_naive",
#         )
#
#         reps2 = timeit.repeat(
#             repeat=rep,
#             number=100,
#             stmt=f"sum_even_fib_fast({limit})",
#             setup="from __main__ import sum_even_fib_fast",
#         )
#
#         reps3 = timeit.repeat(
#             repeat=rep,
#             number=100,
#             stmt=f"sum_even_fib_sublinear({limit})",
#             setup="from __main__ import sum_even_fib_sublinear",
#         )
#
#         reps4 = timeit.repeat(
#             repeat=rep,
#             number=100,
#             stmt=f"PE_002({limit})",
#             setup="from __main__ import PE_002",
#         )
#
#         # taking the median might be better, since I suspect the distribution of times will
#         # be heavily skewed
#         naive, fast, sublinear, euler002 = [
#             np.mean(reps) for reps in [reps1, reps2, reps3, reps4]
#         ]
#         print(
#             f" {power:>3}    {naive:>.2e}     {int(naive/fast):>3}       {int(naive/sublinear):>3}       {int(naive/euler002):>3}    "
#         )
#     # if fast > sublinear:
#     #     break
