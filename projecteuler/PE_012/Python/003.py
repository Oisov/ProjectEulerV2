#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from faktorisering import primesbelow, isprime
from primefac import primefac
from primesieve import Iterator, generate_primes, generate_n_primes
from fractions import gcd
from random import randint
from math import sqrt


def brent(N):
    if N%2==0:
        return 2
    y, c, m = randint(1, N-1), randint(1, N-1), randint(1, N-1)
    g, r, q = 1, 1, 1
    while g == 1:
        x = y
        for i in range(r):
            y = ((y*y)%N+c)%N
        k = 0
        while k<r and g == 1:
            ys = y
            for i in range(min(m,r-k)):
                y = ((y*y)%N+c)%N
                q = q*(abs(x-y))%N
                g = gcd(q,N)
                k = k + m
        r = r*2
    if g == N:
        while True:
            ys = ((ys*ys)%N+c)%N
            g = gcd(abs(x-ys),N)
            if g > 1:
                break
    return g


def bernt_largest_primefactor(N):
    while not isprime(N) and N > 1:
        N //= brent(N)
    return N


def largest_primefactor_naive(num):
    i = 2
    while i < num:
        while num % i == 0:
            num //= i
        i += 1
    return num


def largest_primefactor_improved_1(num):
    i = 2
    while i <= int(sqrt(num)):
        while num % i == 0:
            num //= i
        i += 1
    return num


def largest_primefactor_improved_2(num):
    while num % 2 == 0:
        num //= 2

    i = 3
    limit = num**0.5
    while i < limit:
        while num % i == 0:
            num //= i
            limit = num**0.5
        i += 2
    return num


def largest_primefactor_improved_3(num):
    for k in [2, 3, 5]:
        while num % k == 0:
            num //= k
        if num == 1: return k

    multiple = 6
    limit = num**0.5
    while multiple <= limit:
        for step in [1, 5]:
            factor = multiple + step
            if num % factor == 0:
                num //= factor
                while num % factor == 0:
                    num //= factor
                if num == 1: return factor
                limit = num**0.5
        multiple += 6
    return num

def largest_primefactor_improved_4(num):
    for k in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        while num % k == 0:
            num //= k
        if num == 1: return k

    multiple = 30
    limit = num**0.5
    while multiple <= limit:
        for step in [1, 7, 11, 13, 17, 19, 23, 29]:
            factor = multiple + step
            if num % factor == 0:
                num //= factor
                while num % factor == 0:
                    num //= factor
                if num == 1: return factor
                limit = num**0.5
        multiple += 30
    return num



def largest_factor(num, number_of_spokes = 3):

    spokes = generate_n_primes(n)
    wheel = reduce(lambda x, y: x * y, spokes)
    composites = []
    for i in range(1, wheel):
        if all( i % k != 0 for k in spokes):
            composites.append(i)

    for factor in spokes:
        if num % factor == 0 and n > factor:
            num //= factor
            while num % factor == 0:
                num //= factor
            if num == 1:
                return factor

    multiple = 0
    limit = num**0.5
    while factor < limit:
        for step in composites:
            factor = multiple + step
            if num % factor == 0 and factor > 1:
                num //= factor
                while num % factor == 0:
                    num //= factor
                if num == 1: return factor
                limit = num**0.5
        multiple += wheel
    return num


def prime_gen(num):
    if isprime(num): return num
    it = Iterator()
    prime = it.next_prime()
    limit = num**0.5
    while prime < limit:
        if num % prime == 0:
            num //= prime
            while num % prime == 0: num //= prime
            if num == 1: return prime
            if isprime(num): return num
            limit = num**0.5
        prime = it.next_prime()
    return num


if __name__ == "__main__":
    import timeit
    num = 6008514751436008

    print largest_primefactor_improved_3(3*5*7**10)
    print prime_gen(6008514751436008)
    print
    # print largest_primefactor_improved_4(600851475143600851475143)

    # print largest_primefactor_naive(600851475143)
    # print
    # print bernt_largest_primefactor(600851475143)
    # print
    # print largest_primefactor_improved_3(600851475143)


    times = 1000
    t01 = timeit.timeit(
       "prime_gen(6008514751436008)", number=times, setup="from __main__ import prime_gen")
    print 1000*t01/float(times)


    # t1 = timeit.timeit(
    #    "largest_primefactor_improved_4(600851475143600851475141)", number=times, setup="from __main__ import largest_primefactor_improved_4")
    # print 1000*t1/float(times)

    # times = 1000
    # t01 = timeit.timeit(
    #    "bernt_largest_primefactor(600851475143)", number=times, setup="from __main__ import bernt_largest_primefactor")
    # print 1000*t01/float(times), 'ms'

    # times = 1000
    # t0 = timeit.timeit(
    #    "largest_primefactor_improved(600851475143)", number=times, setup="from __main__ import largest_primefactor_improved")
    # print 1000*t0/float(times), 'ms'


    # times = 1000
    # t0 = timeit.timeit(
    #    "largest_primefactor_improved_2(600851475143)", number=times, setup="from __main__ import largest_primefactor_improved_2")
    # print 1000*t0/float(times), 'ms'


    # times = 1000
    # t0 = timeit.timeit(
    #    "largest_primefactor_improved_2(600851475143)", number=times, setup="from __main__ import largest_primefactor_improved_2")
    # print 1000*t0/float(times), 'ms'


    # times = 100
    # t1 = timeit.timeit(
    #    "list(primefac(600851475143543))[-1]", number=times, setup="from __main__ import primefac")
    # print 1000*t1/float(times), 'ms', 'primefac'

    # t2 = timeit.timeit(
    #    "largest_factor_2(600851475143543)", number=times, setup="from __main__ import largest_factor_2")
    # print 1000*t2/float(times), 'ms'

    # t3 = timeit.timeit(
    #    "largest_factor(600851475143543, [2, 3, 5])", number=times, setup="from __main__ import largest_factor")
    # print 1000*t3/float(times), 'ms'
