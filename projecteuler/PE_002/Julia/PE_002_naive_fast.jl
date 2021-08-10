function PE_002_naive_fast(limit=4*10^6, F_1=1, F_2=2)
    total = 0
    while F_2 < limit
        total += F_2
        for i = 1:3
            F_1, F_2 = F_2, F_1 + F_2
        end
    end
    total
end
