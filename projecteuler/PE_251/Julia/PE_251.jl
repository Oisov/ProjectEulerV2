function PE_251(limit)
    total = 0
    for a = 1:limit
        for b = 1:(limit-a)
            num = (a+1)^2*(8a-1)
            denom = 27*b^2

            if denom > num
                break
            end

            if num % denom == 0
                c = div(num, denom)
                if a + b + c < limit
                    total += 1
                end
            end
        end
    end
    total
end

println(PE_251(110000000))
# println(PE_251(1000))
