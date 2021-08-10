def PE_002_fast(limit=4 * 10**6):
    even_fib, next_even_fib = 0, 2
    total = 0
    while next_even_fib < limit:
        total += next_even_fib
        even_fib, next_even_fib = next_even_fib, 4 * next_even_fib + even_fib
    return total


if __name__ == "__main__":
    print(PE_002_fast())
