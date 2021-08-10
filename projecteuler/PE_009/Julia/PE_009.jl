function PE_009(perimeter=1000)

    s2 = div(perimeter, 2)
    for m = 2:Int(ceil(sqrt(s2))-1)
        if s2 % m != 0
            continue
        end

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
