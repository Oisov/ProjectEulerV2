#!/usr/bin/env python
from projecteuler.utilities import sum_integers, sum_integers_squared


def PE_006(n=100):
    """
    The sum of the first natural numbers are

        S_1(n) = 1 + 2 + 3 ... n = n*(n+1)/2

    The sum of the first square numbers are

        S_2(n) = 1^2 + 2^3 + ... n^2 = n*(n+1)*(2*n+1)/6

    By computing the difference of these two numbers one gets

        S[1](n)^2 - S[2](n) = n (n - 1) (3n + 2) (n + 1) / 12
    """
    return n * (n - 1) * (3 * n + 2) * (n + 1) / 12


print(sum_integers_squared(100) - sum_integers(100))
