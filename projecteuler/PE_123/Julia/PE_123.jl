    using Primes

function numberOfDigits(number)
    return trunc(Int, log(10, number)+1)
end

function primeRemainder(index, p)
    return ((p-1)^index + (p+1)^index) % (p^2)
end

primeList = primes(10^0)
function PE_123(limit)
    for (index, prime) in enumerate(primes(10^7))
        remainder = primeRemainder(index, BigInt(prime))
        if remainder > limit
            return (prime, index)
        end
    end
end

println(PE_123(10^10))
