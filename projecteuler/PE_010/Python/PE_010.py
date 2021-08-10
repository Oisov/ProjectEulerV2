#!/usr/bin/env python
# -*- coding: utf-8 -*-


from faktorisering import primesbelow
from primesieve import generate_primes, Iterator

'''
Project Euler 10: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

if __name__ == '__main__':

    print len([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103])
    print list(primesbelow(108))

    # print generate_primes(2*10**6)
    import timeit
    limit = 2*10**6
    print sum(primesbelow(limit))
    print sum(generate_primes(limit))


    times = 10**4
    t1 = timeit.timeit("primesbelow(2*10**6)", setup="from __main__ import primesbelow", number = times)/float(times)
    t2 = timeit.timeit("generate_primes(2*10**6)", setup="from __main__ import generate_primes", number = times)/float(times)

    print "primesbelow", t1*1000, 'ms'
    print "generate_primes", t2*1000, 'ms'

    print "My solution used: ", 1000*t1, "ms"
    print "The C++ solution used:  ", 1000*t2, "ms"
