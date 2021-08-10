
function remove_non_coprime(divisors)
    new_divisors = []
    divisors = sort(unique(divisors))
    for divisor in divisors
        index = 1
        is_divisible = false
        len_divisors = length(new_divisors)

        while index < len_divisors
            if mod(divisor, divisors[index]) == 0
                is_divisible = true
                break
            else
                index += 1
            end
        end

        if !is_divisible
            push!(new_divisors, divisor)
        end
    end
    return new_divisors
end

"""
Iterates through the integers from start to stop and sums
the numbers divisible by atleast one of the numbers in divisors.

Two minor speedups are present in this code:
    The code breaks after a divisor has been found
    The code sorts the list of divisors in increasing numbers

Say we have the divisors [5, 3] then only 1/5 or 20% of the numbers would
 be stopped by the first loop. However writing the divisors in accending order
then 33% of all numbers are stopped in the first iteration.
"""
function PE_001_naive(divisors = [3, 5], stop=10^3, start=1)
    total = 0
    coprime_divisors = remove_non_coprime(divisors)
    for number in start:(stop-1)
        for divisor in divisors
            if mod(number, divisor) == 0
                total += number
                break
            end
        end
    end
    return total
end

println(PE_001_naive([2,3,5,7], 10^6))
