fib_ = Dict(1 => 0, 2 => 1)

function fib(n)
    try
        return fib_[n]
    end
    fib_[n] = fib(n-1) + fib(n-2)
    fib_[n]
end

function PE_002_memoization(limit=4*10^6)
    n = 1
    total = 0
    while fib(n) < limit
        if fib(n) % 2 == 0
            total += fib(n)
        end
        n += 1
    end
    total
end
