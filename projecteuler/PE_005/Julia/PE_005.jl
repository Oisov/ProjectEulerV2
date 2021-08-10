using Primes

function PE_005(number=20)
    prod = 1

    sqrt_num = Int(floor(sqrt(number)))
    for prime in primes(1, sqrt_num)
        prod *= prime^floor(log(prime, number))
    end

    for prime in primes(sqrt_num+1, number)
        prod *= prime
    end
    BigInt(prod)
end
