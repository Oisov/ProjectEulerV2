using Primes

function PE_010(stop=2*10^6, start=1)
    sum(primes(start, stop))
end
