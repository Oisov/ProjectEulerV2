#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Project Euler: Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
'''

import time


def lattice_rec(x, y):
    """
    Recursive solution to grid problem. Input is a list of x,y moves remaining.
    """
    # base case, no moves left
    if x == 0 and y == 0:
        return 1
    # recursive calls
    paths = 0
    # move left when possible
    if y > 0:
        paths += lattice_rec(x, y - 1)
    # move down when possible
    if x > 0:
        paths += lattice_rec(x - 1, y)
    return paths


def lattice_partial(n, m):
    lattice_dic = dict()

    for i in range(n+1):
        lattice_dic[(i, 0)] = 1
    for j in range(1, m+1):
        lattice_dic[(0, j)] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            lattice_dic[(i, j)] = lattice_dic[(i-1, j)] + lattice_dic[(i, j-1)]

    return lattice_dic[(n, m)]


def recPath_fast(n):
    ret = 1
    for j in range(1, n+1):
        ret *= n + j
        ret //= j
    return ret

if __name__ == '__main__':

    n, m = 100, 100
    print recPath_fast(n)
    print lattice_partial(n, m)
