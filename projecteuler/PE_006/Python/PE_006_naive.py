#!/usr/bin/env python


def PE_006_naive(n):
    square_sum = sum(i**2 for i in xrange(n + 1))
    natural_sum = sum(i for i in xrange(n + 1))
    return natural_sum**2 - square_sum
