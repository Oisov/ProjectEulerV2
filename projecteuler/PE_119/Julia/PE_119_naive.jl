using Combinatorics

function combos_with_replacement(list, k)
    n = length(list)
    combos = []
    println(combinations([1:(n+k-1)],k))
    for c in combinations([1:(n+k-1)], k)
        println(c)
    end

    for c in combinations([1:(n+k-1)], k)
        push!(combos, [[list[c[i]-i+1] for i=1:length(c)]])
    end
    combos
end

function maxPower(digits, digitSum)
    power = length(digits) * log(10, digitSum)
    return (Int(floor(power)), Int(ceil(power)))
end

function isDigitPowerSum(listOfDigits)
    digitSum = sum(listOfDigits)
    digitSorted = sort(listOfDigits)
    for power in maxPower(listOfDigits, digitSum)
        digitSumSorted = sort(digits(digitSum^power))
        if digitSorted == digitSumSorted
            return true
        end
    end
    return false
end

function digitPowerSum(n)
    total = 0
    for listOfDigits in combos_with_replacement([0:9], n)
        println(listOfDigits)
        if isDigitPowerSum(listOfDigits)
            total += 1
        end
    end
    return total
end

# combos_with_replacement(["iced", "jam", "plain"], 3)
combos_with_replacement([3,2,1,1,2], 2)
