#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Project Euler: Power digit sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

def below_twenty(n):
	numbers = [ '', 'one', 'two', 'three', 'four', 'five',
				'six', 'seven', 'eight', 'nine', 'ten',
				'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
				'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty'
			]
	return numbers[n]


def ten_place_name(n):
	numbers = [ '', '', 'twenty', 'thirty', 'forty', 'fifty',
				'sixty', 'seventy', 'eighty', 'ninety'
			]
	return numbers[n]

# concentrate_num(12345999) = [12,345,999]
def concentrate_num(num):
	temp_num_lst = [int(i) for i in str(num)]
	temp_len = len(temp_num_lst)
	num_lst = []
	while temp_len > 2: #While we have three elements
		num_lst.append(   10**0*temp_num_lst.pop() #Pop the last three elements
						+ 10**1*temp_num_lst.pop()
						+ 10**2*temp_num_lst.pop()
						)
		temp_len = len(temp_num_lst)
	# If there are any elements left add them (eg 12)
	if temp_len>0:
		num_lst.append(sum(10**(temp_len-i-1)*item for i,item in enumerate(temp_num_lst)))
	return num_lst[::-1]


def suffix(place):
	if place == 1:
		sffx = 'hundred'
	elif place == 2:
		sffx = 'thousand'
	elif place == 3:
		sffx = 'million'
	elif place == 4:
		sffx = 'billion'
	elif place == 5:
		sffx = 'trillion'
	elif place == 6:
		sffx = 'quadrillion'
	elif place == 7:
		sffx = 'quintillion'
	elif place == 8:
		sffx = 'sextillion'
	elif place == 9:
		sffx = 'septillion'
	else:
		sffx = ''
	return sffx


def below_hundred(num):

	word = ""
	str_num = str(num)
	num_lst_len = len(str_num)
	if num_lst_len == 1:
		num_a = int(str_num[0])
		word += below_twenty(num_a)
	elif num_lst_len == 2:
		num_a = int(str_num[0])
		num_b = int(str_num[1])
		if num_a + num_b > 0:
			word += "and "
			if 10*num_a + num_b < 20:
				word += below_twenty(10*num_a + num_b)
			else:
				word += ten_place_name(num_a)
				if num_b > 0:
					word += "-" + below_twenty(num_b)
	elif num_lst_len == 3:
		word += below_twenty(int(str_num[0])) + " " + suffix(1)
		num_a = int(str_num[1])
		num_b = int(str_num[2])
		if num_a + num_b > 0:
			word += " and "
			if 10*num_a + num_b < 20:
				word += below_twenty(10*num_a + num_b)
			else:
				word += ten_place_name(num_a)
				if num_b > 0:
					word += "-" + below_twenty(num_b)
	return word

def print_word(num):
	word = ''
	num_lst = concentrate_num(num)
	num_lst_len = len(num_lst)
	if num == 0:
		return 'zero'
	if num_lst_len == 1:
		word += below_hundred(num_lst[0])
	else:
		for index,item in enumerate(num_lst):
			power = num_lst_len - index
			word += below_hundred(item) + " "
			if index < num_lst_len-1:
				word += suffix(power) + " "

	if str(word[0:3]) == "and":
		return word[4:]
	return word


def sum_sentence(sentence):
	sentence = sentence.replace(" ", "")
	sentence = sentence.replace("-", "")
	print sentence
	return len(sentence)


def sum_all_word2num(limit):
	total = 0
	for num in range(1,limit+1):
		word = print_word(num)
		total += sum_sentence(word)
	return total


if __name__ == '__main__':

	print sum_all_word2num(1000)
