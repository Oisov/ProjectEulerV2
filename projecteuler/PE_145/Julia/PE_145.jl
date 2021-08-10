function PE_145(max_power = 9)
    total = 0
    for power = 1:max_power
        remainder = power % 4
        if remainder == 2
            total += 20 * 30^(max(div(power, 2) - 1, 0))
        elseif remainder == 1
            total += 100 * 500^(max(div(power, 4) - 1, 0))
        end
    end
    return total
end
