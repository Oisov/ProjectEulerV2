function PE_009_naive(perimeter=1000)
    for a = 3:div(perimeter-3, 3)
        for b = (a+1):div(perimeter-1-a, 2)
            c = perimeter - a - b
            if c^2 == a^2 + b^2
                return prod([a, b, c])
            end
        end
    end
end

println(PE_009_naive())
