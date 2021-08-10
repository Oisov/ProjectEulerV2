using Primes

# function isNsmooth(number, primeList, smoothDict)
#     for prime in primeList
#         if number % prime == 0
#             if get(smoothDict, div(number, prime), 0) != 0
#                 smoothDict[number] = true
#                 return true
#             else
#                 return false
#             end
#         end
#     end
#     return false
# end

function nthTriangleNumber(n)
    return div(n*(n+1), 2)
end

function largestNSmoothTriangleNumber(N)
    n = 1
    primeList = primes(N)
    smoothDict = Dict(prime => true for prime in primeList)

    function isNsmooth(number, primeList, smoothDict, largestSmooth)
        for prime in primeList
            if number % prime == 0
                if get(smoothDict, div(number, prime), 0) != 0
                    smoothDict[number] = true
                    return true, smoothDict
                else
                    return false, smoothDict
                end
            end
        end
        return false, smoothDict
    end

    maxTriangle = -1
    limit = 100
    while n < limit
        nth = nthTriangleNumber(n)
        isSmooth, smoothDict = isNsmooth(nth, primeList, smoothDict)
        if isSmooth
            maxTriangle = n
        end
        n += 1
    end
    println(smoothDict)
    maxTriangle
end

println(largestNSmoothTriangleNumber(7))


