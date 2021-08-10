from collections.abc import Iterable, Callable
from typing import Any

from gmpy2 import mpz
import numpy as np

import functools
import itertools

def sum_powers(power, start: int, stop: int = 0):
    start, stop = min(start, stop), max(start, stop)
    if power == 1:
        return sum_integers(stop, start)
    elif power == 2:
        return sum_squared(stop, start)
    elif power == 3:
        return sum_cubes(stop, start)
    return sum(i ** power for i in range(start, stop + 1))


def sum_integers(start: int, stop: int = 0) -> int:
    """Sums all integers in range in constant time

    Equivalent to

        sum(i for i in range(start, stop + 1))

    but in constant time. Exploits the fact that

        1 + 2 + 3 + ... + n = n (n + 1) / 2

    see https://brilliant.org/wiki/sum-of-n-n2-or-n3/ for more details

    >>> [sum_integers(0, k) for k in range(5)]
    [0, 1, 3, 6, 10]

    >>> sum_integers(4, 4)
    4

    >>> pairs = [(0, 5), (0, -5), (5, 0), (-5, 0)]
    >>> [sum_integers(*pair) for pair in pairs]
    [15, -15, 15, -15]

    >>> pairs = [(5, 10), (5, -10), (-5, -10), (-5, 10)]
    >>> [sum_integers(*pair) for pair in pairs]
    [45, -40, -45, 40]
    """
    integer_sum = lambda n: n * (n + 1) // 2
    start, stop = min(start, stop), max(start, stop)
    return integer_sum(stop) - integer_sum(start - 1)


def sum_integers_squared(start: int, stop: int = 0) -> int:
    """sums the square of all integers in range in constant time

    equivalent to

        list(i**2 for i in range(start, stop + 1))

    but in constant time. exploits the fact that

        1^2 + 2^2 + 3^2 + ... + n = n (n + 1) (2n + 1) / 6

    see https://brilliant.org/wiki/sum-of-n-n2-or-n3/ for more details

    >>> [sum_integers_squared(0, i) for i in range(5)]
    [0, 1, 5, 14, 30]

    >>> sum_integers_squared(4, 4)
    16

    """
    squared = lambda n: n * (n + 1) * (2 * n + 1) // 6
    start, stop = min(start, stop), max(start, stop)
    return squared(stop) - squared(start - 1)


def sum_integers_cubed(stop: int, start: int = 0) -> int:
    """sums the cube of all integers in range in constant time

    equivalent to

        list(i**2 for i in range(start, stop + 1))

    but in constant time. exploits the fact that

        1^3 + 2^3 + 3^3 + ... + n = [ n (n + 1) / 2]^2

    see https://brilliant.org/wiki/sum-of-n-n2-or-n3/ for more details

    >>> [sum_integers_cubed(0, i) for i in range(5)]
    [0, 1, 9, 36, 100]

    >>> sum_integers_cubed(4, 4)
    64

    """
    cubed = lambda n: n ** 2 * (n + 1) ** 2 // 4
    start, stop = min(start, stop), max(start, stop)
    return cubed(stop) - cubed(start - 1)


def nth_fibonacci(n):
    """Returns the nth fibonacci number in O(log n)

    Exploits the following Lucas number relations

        L(2n)     = L(n)^2    - 2 (-1)^n
        L(2n + 1) = L(2n + 2) - L(2n)
        L(2n + 2) = L(n+1)^2  + 2 (-1)^n

    To calculate

        F(n) = [ 2 L(n+1) - L(n) ] / 2

    The following squaring relations are then used

        F(2n)   = F(n) * L(n)
        F(2n+1) = F(n) L(n+1) + (-1)^n

    To quickly calculate ``2n`` and ``2n+1`` from ``n`` and ``n+2``.
    see https://stackoverflow.com/a/48171368/1048781 for more details.

    Args:
        n (int): The index of the nth fibonacci number (F[n])

    Returns:
        The nth fibonacci number

    Example:
        The first ten fibonacci numbers
        >>> [nth_fibonacci(i) for i in range(10)]
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

        The 103rd fibonacci number
        >>> nth_fibonacci(103)
        1500520536206896083277

    """

    def fib_inner(n):
        """Returns L[n] and L[n+1]"""
        if n == 0:
            return mpz(2), mpz(1)
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
        return int(v * f - q)
    return int(u * f)


def linear_reccurence(coefficients: list[int], initials: list[int]) -> int:
    """Returns a generator for a linear recucurence relation

    A linear recurrence relation is of the form

        A(n) = c0 * A(n-1) + c0 * A(n-2) + ... + ck * A(n - k);
        A(0) = I0, A(1) = I1, ..., A(k) = Ik

    and would correspond to ``coefficients = [ck ..., c1, c0]`` and ``initials =
    [Ik, ..., I1, I0]``.  Note that the values here are stored in ascending order

    Args:
        coefficients: Defines the coefficients in the recucurence relation.
        initials: The initial values for the recurrence relation.

    Yields:
        The next value in the recucurence relation.

    Examples:
        >>> powers_of_2 = linear_reccurence([2], [1])
        >>> print([next(powers_of_2) for _ in range(10)])
        [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

        >>> fibonacci = linear_reccurence([1, 1], [0, 1])
        >>> print([next(fibonacci) for _ in range(10)])
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

        Returns the Lucas numbers ``L(n) = L(n-1) + L(n-2)`` with ``L(0)=1``, ``L(1)=3``.

        >>> lucas = linear_reccurence([1, 1], [1, 3])
        >>> print([next(lucas) for _ in range(10)])
        [1, 3, 4, 7, 11, 18, 29, 47, 76, 123]
    """

    sequence = initials.copy()
    yield from sequence
    while True:
        # If sequence = [a, b, c] then one loop changes this to [b, c, next_value]
        # where next_value is the dotproduct between coefficients and sequence
        next_value = sum(i * j for i, j in zip(coefficients, sequence))
        sequence[:-1], sequence[-1] = sequence[1:], next_value
        yield next_value


# fmt: off
_SMALL_FIBS = [
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
    4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811,
    514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352,
    24157817, 39088169, 63245986, 102334155, 165580141, 267914296,
    433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976,
    7778742049, 12586269025, 20365011074, 32951280099, 53316291173,
    86267571272, 139583862445, 225851433717, 365435296162, 591286729879,
    956722026041, 1548008755920, 2504730781961, 4052739537881,
    6557470319842, 10610209857723, 17167680177565, 27777890035288,
    44945570212853, 72723460248141, 117669030460994, 190392490709135,
    308061521170129, 498454011879264, 806515533049393, 1304969544928657,
    2111485077978050, 3416454622906707, 5527939700884757, 8944394323791464,
    14472334024676221, 23416728348467685, 37889062373143906,
    61305790721611591, 99194853094755497, 160500643816367088,
    259695496911122585, 420196140727489673, 679891637638612258,
    1100087778366101931, 1779979416004714189, 2880067194370816120,
    4660046610375530309, 7540113804746346429, 12200160415121876738
]
# fmt: on
_BIG_FIB_1 = 19740274219868223167
_BIG_FIB_2 = 31940434634990099905
_FIBS_LEN = len(_SMALL_FIBS)  # Consider changing this to 94
_SMALL_FIBS_ = set(_SMALL_FIBS)


def fibonacci(stop: int = None, start: int = 0) -> int:
    """Returns the n first fibonacci numbers

    If no input is provided this returns an infinite generator,
    otherwise it returns a generator of fibonacci numbers starting
    with index start and ending with index stop.

    Uses that the fibonacci sequence is a linear recurrence

        F(n) = 1 * F(n-1) + 1 * F(n - 2)

    with initial values ``F(0) = 0`` and ``F(1) = 1``

    >>> next(fibonacci(start=5, stop=5))
    5

    >>> print(list(fibonacci(5)))
    [0, 1, 1, 2, 3]

    >>> print(list(fibonacci(0, 5)))
    [0, 1, 1, 2, 3]

    >>> print(list(fibonacci(5, 10)))
    [5, 8, 13, 21, 34]

    >>> fib1 = fibonacci()
    >>> print([next(fib1) for _ in range(10)])
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    >>> fib2 = fibonacci(start=94-1)
    >>> print([next(fib2) for _ in range(4)])
    [12200160415121876738, 19740274219868223167, 31940434634990099905, 51680708854858323072]

    >>> [x for x in fibonacci(93, 96)]
    [12200160415121876738, 19740274219868223167, 31940434634990099905, 51680708854858323072]

    >>> print(list(fibonacci(103, 103)))
    [1500520536206896083277]

    >>> print(list(fibonacci(103, 104)))
    [1500520536206896083277, 2427893228399975082453]
    """

    def fibonacci_(first, second):
        f0, f1 = first, second
        yield f0
        while True:
            yield f1
            f1, f0 = f1 + f0, f1

    if stop is None:
        if start < _FIBS_LEN:
            yield from _SMALL_FIBS[start:]
            first, second = _BIG_FIB_1, _BIG_FIB_2
        else:
            first, second = nth_fibonacci(start), nth_fibonacci(start + 1)
        yield from fibonacci_(first, second)
        return
    start_, stop_ = min(start, stop), max(start, stop)
    if start_ == stop_:
        if stop_ < _FIBS_LEN:
            yield _SMALL_FIBS[stop_]
        else:
            yield nth_fibonacci(stop_)
        return

    if stop_ < _FIBS_LEN:
        yield from _SMALL_FIBS[start_:stop_]
        return

    if start_ < _FIBS_LEN:
        yield from _SMALL_FIBS[start_:]
        first, second, start_ = _BIG_FIB_1, _BIG_FIB_2, _FIBS_LEN
    else:
        first, second = nth_fibonacci(start_), nth_fibonacci(start_ + 1)
    fibonacci = fibonacci_(first, second)
    for _ in range(stop_ - start_ + 1):
        yield next(fibonacci)
    return


def takewhile(
    iterable: Iterable[Any],
    predicate: Callable[[Any], bool],
    break_condition: Callable[[Any], bool],
):
    for index, value in enumerate(iterable):
        if break_condition(index, value):
            break
        if predicate(index, value):
            yield value

@functools.cache
def reduce_w_cache(function, sequence):
    """Reduces the sequence to a single number by left folding function over it

    Example:

        The easiest way to understand how reduce works is applying a tuple to it
        >>> sequence = tuple([1, 3, 5, 6, 2])
        >>> make_tuple = lambda x, y: tuple([x, y])
        >>> reduce_w_cache(make_tuple, sequence)
        ((((1, 3), 5), 6), 2)

        Similarly a right fold would look like ``(1, (3, (5, (6, 2))))``

        >>> add = lambda x, y: x + y
        >>> sum_reduce = lambda x: reduce_w_cache(add, x)
        >>> reduce_w_cache(add, sequence)
        17

        Understanding how this works is as easy as replacing , with + in the
        example above

            reduce_w_cache(add, sequence) = ((((1 + 3) + 5) + 6) + 2) = 17

        >>> prod = lambda x, y: x * y
        >>> reduce_w_cache(prod, sequence)
        180

        By replacing ``,`` with ``*`` we have

            reduce_w_cache(add, sequence) = ((((1 * 3) * 5) * 6) * 2) = 17

        Lastly we can find the max / min just as easilly
        >>> maximum = lambda x, y: x if y < x else y
        >>> reduce_w_cache(maximum, sequence)
        6

        >>> reduce_w_cache(min, sequence)
        1

        Let us test if the caching works. We first save how many misses we
        have, where a miss corresponds to a value being added to the cache. We
        will then perform some lookups and study how many values were cached.

        >>> repeat_reduce = lambda fun, seqs: [reduce_w_cache(fun, tuple(s)) for s in seqs]
        >>> def values_cached(function, sequences):
        ...     initial = reduce_w_cache.cache_info().misses
        ...     repeat_reduce(function, sequences)
        ...     total = reduce_w_cache.cache_info().misses
        ...     return total - initial

        >>> test_function = lambda x, y: [x, y]
        >>> sequences = [[103], [103, 105], [103, 105, 107], [103, 105, 107, 109], [103, 105, 107, 109, 111]]

        We are going to run ``reduce_w_cache`` with ``test_function`` over
        each element in ``sequences`` With no caching we would expect ``len - 1``
        function calls with a minimal of ``1`` for each sequence in sequences. Totaling to
        `1 + 1 + 2 + 3 + 4 = 11` function calls.

        However with cached values this is greatly lowered. For instance ``(103, 105,
        107)`` folds to ``(103, (105, 107))`` and the value of ``(105, 107)``
        is already stored in the cache.
        >>> values_cached(test_function, sequences)
        5

        No new values should be added if we lookup the same values again
        >>> values_cached(test_function, sequences)
        0

        As a sanity check let us test how many values are cached when
        we can not use previously stored values
        >>> sequences = [[112], [113, 114], [115, 116, 117], [118, 119, 120, 121], [118, 119, 120, 121, 122]]
        >>> values_cached(test_function, sequences)
        11

        Let us double check that the number of calls really is 11. For each
        function call we wrap two elements in ``[]`` so simply counting the number
        of either ``[`` or ``]`` returns the number of function calls.
        >>> str(repeat_reduce(test_function, sequences)).count('[')
        11
    """
    *remaining, last = sequence
    if not remaining:
        return last
    return function(reduce_w_cache(function, tuple(remaining)), last)


def powerset(iterable, emptyset=False, flatten=True):
    """Returns the powerset of some list, grouped by length

    Examples:
        >>> list(powerset([1,2,3]))
        [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]

        >>> list(powerset([1,2,3], emptyset=True))
        [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]

        >>> list(list(i) for i in powerset([1,2,3], flatten=False))
        [[(1,), (2,), (3,)], [(1, 2), (1, 3), (2, 3)], [(1, 2, 3)]]

        >>> list(list(i) for i in powerset([1,2,3], emptyset=True, flatten=False))
        [[()], [(1,), (2,), (3,)], [(1, 2), (1, 3), (2, 3)], [(1, 2, 3)]]
    """

    try:
        iterator = iter(iterable)
        s = list(iterable)
    except TypeError:
        if not isinstance(iterable, list):
            raise TypeError("Input must be list or iterable")
        s = iterable
    start = 0 if emptyset else 1
    powerset_ = (itertools.combinations(s, r) for r in range(start, len(s) + 1))
    return itertools.chain.from_iterable(powerset_) if flatten else powerset_


if __name__ == "__main__":
    import doctest
    import timeit

    doctest.testmod()
