function PE_025_naive(number_of_digits = 10^3)
    n = 1
    nth_fib, next_fib = (0,1)
    while ceil(log(10, next_fib)) < number_of_digits
        nth_fib, next_fib = (BigInt(next_fib), BigInt(nth_fib + next_fib))
        n += 1
    end
    n
end

function PE_025(number_of_digits = 10^3)
    """
    There exists the following closed form for the nth fibonacci number

        F   = PHI^n - (-PHI)^(-n)
         n       sqrt(5)

    Where PHI = (1 + sqrt(5))/2 represents the golden ratio. To find the number
    of digits in a number we compute log10(F_n). Thus, we are trying to find the
    lowest n such that

        log10(F_n) > num_of_digits

    A major simplification is that since PHI > 1 the expression

        (-PHI)^(-n)

    rappidly tends to zero as n increases. Thus, we can ignore it in the first
    formula above. So we are left with the equation

        log10(PHI^n / sqrt(5)) > number_of_digits

    Solving this expression for n yields

        n > number_of_digits + log(sqrt(5))
                    log10(PHI)

    To obtain the least integer n we replace num_of_digits with number of digits
    - 1 and round the right side up to the closest integer. This gives the code
    below
    """

    PHI = (1 + sqrt(5))/2
    trunc(Int, ceil((number_of_digits - 1 + log10(5)/2)/log10(PHI)))
end

println(PE_025())

