function digitSum(number)
    return sum(digits(number))
end

function isPowerDigitSum(number)
    power = log(digitSum(number), number)
    return ceil(power) == floor(power)
end

println(isPowerDigitSum(512))
println(6^2, ", ", 6^3)

total = 0
for i = 1:10^10
    if isPowerDigitSum(i)
        total += 1
        println(i, ", ", total)
    end
end
