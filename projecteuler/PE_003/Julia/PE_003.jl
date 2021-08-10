using Primes

function PE_003(number=600851475143)
    maximum(keys(factor(number)))
end
