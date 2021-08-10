function nimSum(heaps)
    total = xor(heaps[1], heaps[2])
    for index = 3:length(heaps)
        total = xor(total, heaps[index])
    end
    return total
end

total = 0
for n = 1:2^30
    if nimSum([n, 2*n, 3*n]) == 0
        total += 1
    end
end
println(total)
