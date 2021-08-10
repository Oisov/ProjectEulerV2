from PE_002_naive import PE_002_naive
from math import log

PHI = (1 + 5**0.5) / float(2)
LOG_5 = log(5, PHI) / float(6)


def largest_even_fib_under_n(limit):
    return int(LOG_5 + log(limit, PHI) / float(3))


def PE_002_math(limit=4 * 10**6):
    if limit > 10**15:
        return PE_002_naive(limit)
    fib_max_index = largest_even_fib_under_n(limit)
    phi = ((1 + 5**0.5) / float(2))

    def sum_phi(k, positive=True):
        if positive:
            i = 1
        else:
            if k > 10:
                return (5**0.5 - 1) / float(4)
            i = -1
        phi_3 = phi**(3 * i)
        return phi_3 * (1 - (i * phi_3)**k) / float(1 - phi_3)

    total = sum_phi(fib_max_index) + sum_phi(fib_max_index, False)
    return int(total / float(5**0.5))


if __name__ == "__main__":

    print(PE_002_math(10**(16)))
