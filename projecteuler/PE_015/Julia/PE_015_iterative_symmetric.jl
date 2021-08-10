function PE_015_iterative_symmetric(n = 20, m = 20)
    rows, columns = n+1, m+1
    grid = ones(BigInt, rows, columns)

    for i = 2:rows
        for j = 2:i
            grid[i, j] = grid[i-1, j] + grid[i, j-1]
            grid[j, i] = grid[i, j]
        end
    end

    grid[rows, columns]
end
