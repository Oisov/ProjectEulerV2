import timeit
from math import log

" 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26."
" What is the sum of the digits of the number 2^1000? "

def digit_sum_wikipedia(x, base):
    total = 1
    for n in xrange(int(log(x, base))):
        pow_base = base**n
        digit = (x % (base*pow_base) - (x % pow_base))
        total += digit/pow_base
    return total

def digit_sum(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

def digit_sum_fast(num):
    return sum(map(int, str(num)))

def naive_digitsum(num):
    return sum(int(i) for i in str(num))

if __name__ == '__main__':

    print digit_sum_wikipedia(2**1000, 10)
    sum(map(int, str(2**(10**3))))
    num = 2**(10**4)
    n = 100
    print timeit.timeit(lambda: digit_sum_fast(num), number = n)/float(n)
    print timeit.timeit(lambda: naive_digitsum(num), number = n)/float(n)
    #print timeit.timeit(lambda: digit_sum_wikipedia(num, 10), number = n)/float(n)
    #print digit_sum_fast(num)
    
