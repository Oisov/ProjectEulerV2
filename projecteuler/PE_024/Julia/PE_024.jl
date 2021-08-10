function list_2_num(number_list)
    parse(Int, join(map(string, number_list)))
end


function PE_024(elements=[i for i=0:9], nth_permutation=10^6)

    elements_length = length(elements)
    indices = [i for i = 1:elements_length]

    if nth_permutation > factorial(elements_length)
        return elements[reverse(indices)]
    end

    lexographical_index = []
    remainder = nth_permutation
    for i = elements_length-1:-1:1
        div, remainder = divrem(remainder, factorial(i))

        if remainder == 0
            div -= 1
            remainder += div*factorial(i)
        end

        push!(lexographical_index, indices[div+1])
        deleteat!(indices, div+1)
    end
    push!(lexographical_index, indices[1])
    elements[lexographical_index]
end
