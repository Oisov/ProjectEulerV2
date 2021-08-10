def fibonacci(limit=float("Inf")):
    fib, fib_next = 0, 1
    while fib < limit:
        yield fib
        fib, fib_next = fib_next, fib + fib_next


def PE_002_naive(limit=4 * 10 ** 6):
    total = 0
    for fib in fibonacci(limit):
        if fib % 2 == 0:
            total += fib
    return total


def _PE_002_naive_functional(limit=4 * 10 ** 6):
    return sum(fib for fib in fibonacci(limit) if fib % 2 == 0)


if __name__ == "__main__":

    print(PE_002_naive())
