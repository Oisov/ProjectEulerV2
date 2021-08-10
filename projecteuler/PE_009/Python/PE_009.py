#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Project Euler 9: Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

from fractions import gcd

def exact_triple_fast(limit):
    if limit % 2 != 0:
        return (0, 0, 0)
    num2 = limit/2
    mlimit = int(1+num2**0.5) - 1
    for m in range(2, mlimit):
        if num2 % m == 0:
            sm = num2/m
            while sm % 2 == 0 and sm > 1:
                sm //= 2
            if m % 2 == 1: k = m + 2
            else: k = m + 1
            while k < 2*m and k < sm:
                if sm % k == 0 and gcd(k, m) == 1:
                    d = num2 / (k*m)
                    n = k - m
                    a = d*(m*m - n*n)
                    b = 2*d*m*n
                    c = d*(m*m + n*n)
                    return (a, b, c)
                k += 2


def exact_triple(number):
    if number % 2 != 0:
        return (0, 0, 0)

    sqr_c = int(1 + (0.25*number**0.5))
    for m in xrange(1, sqr_c):
        d = 1 + m%2
        for n in xrange(d, m, d):
            pyt_sum = 2*m*(m+n)
            if number % pyt_sum == 0:
                f = number/pyt_sum
                a, b, c = m**2 - n**2, 2*m*n, m**2 + n**2
                return (f*a,f*b,f*c)
    return (0, 0, 0)


if __name__ == "__main__":

    limit = 10**4
    print exact_triple(limit)
    print exact_triple_fast(limit)
