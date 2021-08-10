function isPrime(n)
    if n % 5 == 0
        return false
    end

    for k = 1:div(ceil(n^.5), 6)
        if n % (6*k + 1) == 0
            return false
        elseif n % (6*k + 5) == 0
            return false
        end
    end

    true
end

function PE_010(limit)
    primeSum = 0
    if limit > 7
        primeSum += 2+3+5
    end

    for k = 1:div(limit-5, 6)
        for num in [6*k+1, 6*k+5]
            if isPrime(num)
                primeSum += num
            end
        end
    end

    next = 6*(1+div(limit-5, 6))+1
    if next < limit
        if isPrime(next)
            primeSum += next
        end
    end
    primeSum
end

println(isPrime(49))

println(PE_010(2*10^6))
