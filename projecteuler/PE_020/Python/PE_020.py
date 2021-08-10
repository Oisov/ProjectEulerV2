#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Project Euler: Factorial digit sum

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

from math import factorial
import timeit

def digit_sum_fast(num):
    return sum(map(int, str(num)))

if __name__ == '__main__':

	# One liner
	num = 100
	# print timeit.timeit(lambda: sum(int(digit) for digit in str(factorial(num))), number = 10000)
	# print timeit.timeit(lambda: digit_sum_fast(factorial(num)), number = 10000)
	print digit_sum_fast(factorial(num))
