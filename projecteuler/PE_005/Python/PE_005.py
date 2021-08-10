#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Project Euler 5: Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


from primesieve import generate_primes
from math import log


def smallest_multiple_2(number):
    old_1_to_n = [k for k in range(2, number+1)]
    len_1_to_n = number - 1
    new_1_to_n = []

    prod = 1
    while len_1_to_n:
        divisor = old_1_to_n[0]
        len_1_to_n -= 1
        prod *= divisor
        for j in range(1, len_1_to_n+1):
            next_value = old_1_to_n[j]
            if next_value % divisor != 0:
                new_1_to_n.append(next_value)
            else:
                next_value_divided = next_value/divisor
                if next_value_divided > 1:
                    new_1_to_n.append(next_value_divided)
        old_1_to_n = list(new_1_to_n)
        len_1_to_n = len(old_1_to_n)
        new_1_to_n = []
    return prod


def smallest_multiple(number):
    prod = 1
    lst = [i for i in range(2, number+1)]
    lst_len = number - 1
    for i, divisor in enumerate(lst):
        if divisor > 1:
            prod *= divisor
            for k in range(i, lst_len):
                if (lst[k] % divisor) == 0:
                    lst[k] /= divisor
    return prod


def smallest_multiple_fast(n):
    prod = 1
    for prime in generate_primes(n):
        prod *= prime**int(log(n, prime))
    return prod


def smallest_multiple_fastest(n):
    prod = 1
    for prime in generate_primes(int(n**0.5)):
        prod *= prime**int(log(n, prime))
    for prime in generate_primes(int(1+n**0.5), n):
        prod *= prime
    return prod

if __name__ == "__main__":
    print smallest_multiple_2(20)
    print smallest_multiple(20)
    print smallest_multiple_fast(20)
    print smallest_multiple_fastest(20)

    import timeit
    times = 10
    t1 = timeit.timeit("smallest_multiple(20)",
                       setup="from __main__ import smallest_multiple", number=times)/float(times)
    print "Naive: ", t1*1000, 'ms'
    times = 20
    t2 = timeit.timeit("smallest_multiple_fast(20)",
                       setup="from __main__ import smallest_multiple_fast", number=times)/float(times)
    print "Optimized: ", t2*1000, 'ms'
    t3 = timeit.timeit("smallest_multiple_fastest(20)",
                       setup="from __main__ import smallest_multiple_fastest", number=times)/float(times)
    print "Most optimized: ", t3*1000, 'ms'
    print '''
The optimized code was {} times faster than the naive
the most optimized code was {} times faster than the naive
    '''.format(t1/float(t2), format(t1/float(t3)))
