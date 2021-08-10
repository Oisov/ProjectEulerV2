function PE_114(n)


    for i = (1:n)-1
        if n == 1
            return PE_114(n-1)
        else
            return PE_114(i) + PE_114(n-1-i)
        end
    end

end

for n=7:8
    println(PE_114(n))
end
