"""
This code solves Project Euler Problem 2:

    Each new term in the Fibonacci sequence is generated by adding the previous
    two terms. By starting with 1 and 2, the first 10 terms will be:
    
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    
    By considering the terms in the Fibonacci sequence whose values do not
    exceed four million, find the sum of the even-valued terms.

See https://projecteuler.net/index.php?section=problems&id=2 for details
"""
import typing
import bisect

EvenFibSum = typing.NewType("EvenFibSum", int)
Limit = typing.NewType("Limit", int)

PE_002_LIMIT = 4 * 10 ** 6

# fmt: off
EVEN_FIBS = [
    0, 2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578,
    14930352, 63245986, 267914296, 1134903170, 4807526976, 20365011074,
    86267571272, 365435296162, 1548008755920, 6557470319842, 27777890035288,
    117669030460994, 498454011879264, 2111485077978050, 8944394323791464,
    37889062373143906, 160500643816367088, 679891637638612258,
    2880067194370816120, 12200160415121876738
]
# fmt: on

EVEN_FIBS_SET = set(EVEN_FIBS)

# fmt: off
EVEN_FIBS_CUMSUM = [
    0, 2, 10, 44, 188, 798, 3382, 14328, 60696, 257114, 1089154, 4613732,
    19544084, 82790070, 350704366, 1485607536, 6293134512, 26658145586,
    112925716858, 478361013020, 2026369768940, 8583840088782, 36361730124070,
    154030760585064, 652484772464328, 2763969850442378, 11708364174233842,
    49597426547377748, 210098070363744836, 889989708002357094,
    3770056902373173214, 15970217317495049952
]
# fmt: on


def linear_reccurence(constants: list[int], initials: list[int]) -> int:
    """Returns a generator for a linear recucurence relation

    A linear recurrence relation is of the form

        A(n) = c0 * A(n-1) + c0 * A(n-2) + ... + ck * A(n - k);
        A(0) = I0, A(1) = I1, ..., A(k) = Ik

    and would correspond to ``constants = [ck ..., c1, c0]`` and ``initials =
    [Ik, ..., I1, I0]``.  Note that the values here are stored in ascending order

    Args:
        constants: Defines the constants in the recucurence relation.
        initials: The initial values for the recurrence relation.

    Yields:
        The next value in the recucurence relation.

    Examples:
        Returns the Fibonacci numbers ``F(n) = F(n-1) + F(n-2)`` with ``F(0)=0``, ``F(1)=1``.

        >>> fibonacci = linear_reccurence([1, 1], [0, 1])
        >>> print([next(fibonacci) for _ in range(10)])
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

        Returns the Lucas numbers ``L(n) = L(n-1) + L(n-2)`` with ``L(0)=1``, ``L(1)=3``.

        >>> lucas = linear_reccurence([1, 1], [1, 3])
        >>> print([next(lucas) for _ in range(10)])
        [1, 3, 4, 7, 11, 18, 29, 47, 76, 123]
    """

    values = initials.copy()
    for value in values:
        yield value
    while True:
        last = sum(const * value for const, value in zip(constants, values))
        values[:-1], values[-1] = values[1:], last
        yield last


def PE_002(limit: Limit = PE_002_LIMIT) -> EvenFibSum:
    """Sums all even fibonacci numbers under some limit

    Args:
        limit: Sums all even fibonacci numbers less than this limit

    Returns:
        The sum of all even fibonacci numbers less than some limit

    Examples:
        >>> limits = [0, 2, 8, 10, 10**8]
        >>> print([PE_002(lim) for lim in limits])
        [0, 2, 10, 10, 82790070]

        >>> print(PE_002(2**65-1))
        15970217317495049952
    """

    def _even_fib_sum_large(limit: Limit) -> EvenFibSum:
        total = EVEN_FIBS_CUMSUM[-1] - EVEN_FIBS[-2] - EVEN_FIBS[-1]
        # The linear recurrence relation for the even fibonacci numbers is
        #   E(n) = 4 * E(n - 1) + 1 * E(n - 2); E(0) = 0, E(1) = 2
        # See https://math.stackexchange.com/questions/94359/need-help-deriving-recurrence-relation-for-even-valued-fibonacci-numbers
        even_fibonacci = linear_reccurence([1, 4], [EVEN_FIBS[-2], EVEN_FIBS[-1]])
        while (even_fib := next(even_fibonacci)) < limit:
            total += even_fib
        return total

    def _even_fib_sum_small(limit: Limit) -> EvenFibSum:
        # The code performs a lookup to find the largest index such that EVEN_FIBS[index] <= limit.
        # The lookup is done in O(log n) using a basic bisection algorithm.
        # The offset is added because bisection performs < and we need <=
        offset = 0 if limit in EVEN_FIBS_ else 1
        index = bisect.bisect_left(EVEN_FIBS, limit)
        return EVEN_FIBS_CUMSUM[index - offset]

    if limit > EVEN_FIBS[-1]:
        return _even_fib_sum_large(limit)
    return _even_fib_sum_small(limit)


if __name__ == "__main__":
    import doctest
    import argparse

    doctest.testmod()

    parser = argparse.ArgumentParser(
        description="Solves Project Euler 2; Sums all even fibonacci numbers less than limit"
    )
    parser.add_argument(
        dest="limit",
        nargs="?",
        type=int,
        default=PE_002_LIMIT,
        help="Sums all even fibonacci numbers less than this number",
    )
    args = parser.parse_args()

    print(PE_002(args.limit))
