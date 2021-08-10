using Primes


function proper_divisors{T<:Integer}(n::T)
    0 < n || throw(ArgumentError("number to be factored must be ≥ 0, got $n"))
    1 < n || return T[]
    !isprime(n) || return T[one(T), n]
    f = factor(n)
    d = T[one(T)]
    for (k, v) in f
        c = T[k^i for i in 0:v]
        d = d*c'
        d = reshape(d, length(d))
    end
    sort!(d)
    return d[1:end-1]
end


function PE_009_primes(perimeter=1000)
    s2 = div(perimeter, 2)
    for m in proper_divisors(s2)
        println(m)
        sm = div(s2, m)
        while sm % 2 == 0
            sm = div(sm, 2)
        end

        if m % 2 == 1
            k = m + 2
        else
            k = m + 1
        end

        while k < 2*m && k <= sm
            if sm % k == 0 && gcd(k, m) == 1
                d = div(s2, k*m)
                n = k - m
                a = d*(m^2 - n^2)
                b = 2*d*m*n
                c = d*(m^2 + n^2)
                return ([a, b, c])
            end
            k += 2
        end
    end
end
