import timeit

def PE_002_naive_fast(limit=4*10**6, F_1=1, F_2=2):
    total = 0
    while F_2 < limit:
        total += F_2
        for _ in range(3):
            F_1, F_2 = F_2, F_1 + F_2
    return total


if __name__ == "__main__":

    print(PE_002_naive_fast())
    runs = 10**6
    print(timeit.timeit("PE_002_naive_fast()",
                        setup="from __main__ import PE_002_naive_fast",
                        number=runs)/float(runs))
    
