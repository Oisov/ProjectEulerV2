#!/usr/bin/env python
# -*- coding: utf-8 -*-

from primefac import isprime


def is_palindrome(number):
    string = str(number)
    return string == string[::-1]


def cheat_even(num):
    nine = '9' * (num / 2)
    num1 = nine + nine
    num2 = nine + '0' * (-1 + num / 2) + '1'
    product = nine + '0' * (num) + nine
    return (int(num1), int(num2))


def generate_palindromes(n, increase=False):
    """
    Generates palindromes of length 2n.
    Changing increase to True causes the function to yield the smallest numbers first.
    """
    en = 10**n
    en1 = 10**(n - 1)
    range_ = xrange(en1, en) if increase else xrange(en - 1, en1 - 1, -1)
    for i in range_:
        i = str(i)
        yield int(i + i[::-1])


def PE_004(n=3):
    if n == 1:
        return 0
    elif n % 2 == 0:
        fac_1, fac_2 = cheat_even(n)
        palindrome = fac_1*fac_2
        if is_palindrome(palindrome):
            return palindrome

    en = 10**n
    en1 = 10**(n - 1)
    for p in generate_palindromes(n):
        p //= 11
        if isprime(p):
            continue
        # Generate numbers such that 11*i has length n
        for i in xrange(en // 11, max(p // en, en1 // 11), -1):
            if p % i == 0:
                return p * 11
                # return (i * 11, p // i), p * 11
