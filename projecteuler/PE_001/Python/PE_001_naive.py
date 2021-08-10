import sys


def is_divisible(num: int, divisors: list) -> bool:
    return any(num % d == 0 for d in divisors)


def yield_divisible(numbers: list, divisors: list) -> int:
    for number in numbers:
        if is_divisible(number, divisors):
            yield number


def PE_001_naive(start: int, stop: int, divisors: list) -> int:
    numbers = range(start, stop)
    return sum(yield_divisible(numbers, divisors))


if __name__ == "__main__":

    if len(sys.argv) == 2:
        args = sys.argv[1].replace(" ", "").split("|")
        start, stop, divisors = int(args[0]), int(args[1]), eval(args[2])
    else:
        start, stop, divisors = [1, 1000, [3, 5]]

    print(PE_001_naive(start, stop, divisors))
