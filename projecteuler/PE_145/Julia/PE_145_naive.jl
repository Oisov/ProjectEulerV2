function isOnlyOdd(num)
    for digit in digits(num)
        if digit % 2 == 0
            return false
        end
    end
    return true
end

function reversibleNumbers(limit=10^9)
    total = 0
    for num = 1:limit
        if num % 10 == 0
            continue
        end

        reversenum = parse(Int, reverse(string(num)))
        if isOnlyOdd(reversenum + num)
            total += 1
        end
    end
    total
end
