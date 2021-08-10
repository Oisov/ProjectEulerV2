function squareRemainder(number, index)
    return ((number+1)^index + (number-1)^index) % number^2
end

function checkMaxRemainder(number)
    max_rem = 0

    checklist = [i for i=number:-1:(max(number-10,0))]

    half = div(number, 2)
    append!(checklist, [i for i=(half+3):-1:(max(0, half-3))])

    for index in checklist
        remainder = squareRemainder(BigInt(number) , index)
        if max_rem < remainder
            max_rem = remainder
        end
    end

    return max_rem
end

function max_remainder(number)
    max_rem = 0
    max_i = 0
    for i = 1:2:number
        remainder = squareRemainder(BigInt(number) , i)
        if max_rem < remainder
            max_rem = remainder
        end
    end
    return max_rem
end

function PE_120(limit=1000, minLimit = 3)
    max_rem = 0
    for a = minLimit:limit
        remainder = max_remainder(a)
        if max_rem < remainder
            max_rem = remainder
        end
    end
    return max_rem
end


# println(PE_120())
println(max_remainder(BigInt(947)))
println(BigInt(1000)^2)
