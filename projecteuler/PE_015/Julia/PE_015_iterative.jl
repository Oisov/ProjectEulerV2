function PE_015_iterative(n = 20, m = 20)
    rows, columns = n+1, m+1
    grid = ones(BigInt, rows, columns)

    for i = 2:rows
        for j = 2:columns
            grid[i, j] = grid[i-1, j] + grid[i, j-1]
        end
    end

    grid[rows, columns]
end
