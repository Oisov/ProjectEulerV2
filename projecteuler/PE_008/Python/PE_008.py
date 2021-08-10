#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Project Euler 8: Largest product in a series

The four adjacent digits in the 1000-digit number that have the greatest product
are 9 × 9 × 8 × 9 = 5832.

    73167176531330624919225119674426574742355349194934
    96983520312774506326239578318016984801869478851843
    85861560789112949495459501737958331952853208805511
    12540698747158523863050715693290963295227443043557
    66896648950445244523161731856403098711121722383113
    62229893423380308135336276614282806444486645238749
    30358907296290491560440772390713810515859307960866
    70172427121883998797908792274921901699720888093776
    65727333001053367881220235421809751254540594752243
    52584907711670556013604839586446706324415722155397
    53697817977846174064955149290862569321978468622482
    83972241375657056057490261407972968652414535100474
    82166370484403199890008895243450658541227588666881
    16427171479924442928230863465674813919123162824586
    17866458359124566529476545682848912883142607690042
    24219022671055626321111109370544217506941658960408
    07198403850962455444362981230987879927244284909188
    84580156166097919133875499200524063689912560717606
    05886116467109405077541002256983155200055935729725
    71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
'''

import math
import timeit
from functools import reduce


def naive_str_search(string, length):
    string_length = len(string)
    product_max = 1
    for k in range(string_length - length + 1):
        product = 1
        for i in range(length):
            product *= int(string[k + i])
        if product > product_max:
            product_max = product
    return product_max


def improved_str_search(num_list, length):
    product_max = 0
    zero_lst = []
    for i, num in enumerate(num_list):
        if num == 0: zero_lst.append(i)
    zero_lst.append(len(num_list))

    stop = 0
    for i in range(len(zero_lst)-1):
        start, stop = stop + 1, zero_lst[i]
        if stop - start >= length:
            product = product_bitshift(num_list[start:stop], stop - start, length)
            # product = product_whole(num_list[start:stop], stop - start, length)
            if product > product_max:
                product_max = product
    return product_max


def product_bitshift(sub_list, len_sub_list, length):
    max_product = product = prod(sub_list[:length])
    for i in range(length, len_sub_list):
        product *= sub_list[i] / float(sub_list[i - length])
        if product > max_product:
            max_product = product
    return int(max_product)


def product_whole(sub_list, len_sub_list, length):
    max_product = product = prod(sub_list[0:length])
    for i in range(length, len_sub_list):
        product = prod(sub_list[i - length + 1:i + 1])
        if product > max_product:
            max_product = product
    return int(max_product)


def prod(lst):
    return reduce(lambda x, y: int(x) * int(y), lst)


if __name__ == "__main__":

    n = ("73167176531330624919225119674426574742355349194934"
         "96983520312774506326239578318016984801869478851843"
         "85861560789112949495459501737958331952853208805511"
         "12540698747158523863050715693290963295227443043557"
         "66896648950445244523161731856403098711121722383113"
         "62229893423380308135336276614282806444486645238749"
         "31358997296292491567442772392713814515859357968866"
         "70172427121883998797908792274921901699720888093776"
         "65727333001053367881220235421809751254540594752243"
         "52584907711670556013604839586446706324415722155397"
         "53697817977846174064955149290862569321978468622482"
         "83972241375657056057490261407972968652414535100474"
         "82166370484403199890008895243450658541227588666881"
         "16427171479924442928230863465674813919123162824586"
         "17866458359124566529476545682848912883142607690042"
         "24219022671055626321111109370544217506941658960408"
         "07198403850962455444362981230987879927244284909188"
         "84580156166097919133875499200524063689912560717606"
         "05886116467109405077541002256983155200055935729725"
         "71636269561882670428252483600823257530420752963450")

    num_list = [int(i) for i in n]

    # comment these lines to solve the original problem
    f = open('1MillionDigits.txt', 'r')
    num_list = map(int, f.read())

    length = 5
    print improved_str_search(num_list, length)
    # print naive_str_search(num_list, length)

    n = 10
    # print 1000*timeit.timeit(lambda: naive_str_search(num_list, length),
    # number = n)/float(n) , 'ms'
    print timeit.timeit(lambda: improved_str_search(num_list, length), number=n) / float(n), 'ms'
