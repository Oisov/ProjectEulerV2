function PE_015_symmetric(grid=[20, 20])
    rows, columns = grid
    if rows == columns
        total_ex = 1
        for index = 1:rows
            total_ex = div(BigInt(total_ex)*(rows+index), index)
        end
        total_ex
    end
end
