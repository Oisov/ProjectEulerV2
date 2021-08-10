function PE_015_recursive(rows=20, columns=20)
    path_sum = Dict{Any, BigInt}()

    function count_routes(m, n)
        if n == 0 || m == 0
            return 1
        end

        try
            return path_sum[(m, n)]
        end
        path_sum[(m, n)] = count_routes(m, n - 1) + count_routes(m - 1, n)
        return path_sum[(m, n)]
    end
    count_routes(rows, columns)
end
