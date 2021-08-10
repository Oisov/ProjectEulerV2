function PE_002(limit = 4*10^6)
    a, b = 0, 2
    while b < limit
        a, b = b, 4 * b + a
    end
    div(a + b - 2, 4)
end
