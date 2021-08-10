collatz_ = Dict(1 => 0)


function next_collatz_number(num)
    if num % 2 == 0
        div(num, 2)
    else
        3*num + 1
    end
end


function get_collatz_length(num, visited = [])
    collatz_key = get(collatz_, num, -1)
    push!(visited, num)
    if collatz_key == -1
        get_collatz_length(next_collatz_number(num), visited)
    else
        for (index, prev_num) in enumerate(reverse(visited))
            collatz_[prev_num] = collatz_key + index - 1
        end
        collatz_[visited[1]]
    end
end


function PE_014(limit=10^6, start=1)
    max_collatz = -Inf
    starting_number = nothing
    for number = start:limit
        collatz_length = get_collatz_length(number)
        if collatz_length > max_collatz
            starting_number = number
            max_collatz = collatz_length
        end
    end
    starting_number
end
