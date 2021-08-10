using Primes

function isSquareFree(number, primeList)
    for prime in primeList
        if number % prime^2 == 0
            return false
        end
    end
    return true
end

function PascalsTriangle(rows=8)

    prevCoefficients = [0, 1, 1, 0]
    uniqueCoefficients = Set()

    for n = 2:rows-1
        coefficients = [0]
        for k = 1:(n+1)
            push!(coefficients, prevCoefficients[k] + prevCoefficients[k+1])
        end
        push!(coefficients, 0)
        prevCoefficients = coefficients

        union!(uniqueCoefficients, Set(coefficients))
    end
    uniqueCoefficients
end

function PE_203(rows)
    squareFreeSum = 0
    primeList = primes(rows)
    for coefficient in PascalsTriangle(rows)
        if isSquareFree(coefficient, primeList)
            squareFreeSum += coefficient
        end
    end
    squareFreeSum
end
