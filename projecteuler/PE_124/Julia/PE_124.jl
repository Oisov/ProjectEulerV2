using Primes

function rad(n)
    return prod(keys(factor(n)))
end

function PE_124(limit, target)
    radicals = []
    for n = 1:limit
        push!(radicals, (n, rad(n)))
    end
    sort!(radicals, by=x->x[2])
    return radicals[target][1]
end

println(PE_124(100000, 10000))
