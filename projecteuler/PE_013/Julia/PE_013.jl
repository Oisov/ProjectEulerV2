function first_n_digits(number, digits = 10)
    parse(Int64, string(number)[1:digits])
end

function PE_013(path="../PE_013_input.txt")
    total = 0
    f = open(path)
    for line in readlines(f)
        total += parse(Float64, line)
    end
    first_n_digits(BigInt(total))
end
