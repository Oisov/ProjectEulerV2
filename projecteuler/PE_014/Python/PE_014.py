#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Longest Collatz sequence
The following iterative sequence is defined for the set of positive integers:

	n  ->  n/2 (n is even)
	n  ->  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

	13  ->  40  ->  20  ->  10  ->  5  ->  16  ->  8  ->  4  ->  2  ->  1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

from collections import defaultdict

LIMIT = 10**6
collatz_dict = defaultdict(int)


def collatz_step(num):
	return num // 2 if num%2 == 0 else 3*num + 1


def collatz_sequence_length(num):
	length = 1
	lst_collatz = [num]
	while num != 1:
		num = collatz_step(num)
		lst_collatz.append(num)
		length += 1
		if collatz_dict[num] != 0:
			length += -1 + collatz_dict[num]
			break
	for i, item in enumerate(lst_collatz):
		collatz_dict[item] = length - i
	return length


def collatz_longest_sequence(limit=LIMIT):
	longest_sequence = 1
	start_num = 1
	for num in xrange(limit-1, limit/2, -2):
		if collatz_dict[num] != 0:
			continue
		length_sequence = collatz_sequence_length(num)
		if length_sequence > longest_sequence:
			longest_sequence = length_sequence
			start_num = num
	return (start_num, longest_sequence)


if __name__ == '__main__':

	import timeit
	print collatz_longest_sequence()
	times = 10
	t1 = timeit.timeit("collatz_longest_sequence()", setup="from __main__ import collatz_longest_sequence", number = times)
	print "{} ms".format(t1/float(times))
	# print PE()
